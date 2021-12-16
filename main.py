#=====================================================
# Department of Mechanical Engineering, Purdue University
# ME 506: Two-Phase Flow and Heat Transfer
# Fall 2019
# Final: Two-Phase Flow Induced Vibrations
# Julien Brillon | 031064624
# Python 2.7.15
#=====================================================
# Import libraries
import numpy as np
import scipy
import matplotlib.pyplot as plt
import scipy.sparse as scysparse
import scipy.sparse.linalg
from scipy.optimize import fsolve
#=====================================================
from var import *
from polylib import *
from operations import *
#=====================================================
#				Equation of Motion
#=====================================================
# from EoM_SinglePhasePCF import *
from EoM_TwoPhasePCF import *
# from EoM_SinglePhasePIAF import *
#*****************************************************
# 			Display Problem Setup
#*****************************************************
print('\nSETUP:')
print('--------------------------')
print('End conditions: %s' % EndCond)
print('Number of modes: %i' % Nmodes)
print('--------------------------\n')

print('\nPARAMETERS:')
print('--------------------------')
print('rhoG = %f' % rhoG)
print('rhoL = %f' % rhoL)
print('eps = %f' % eps)
print('alpha = %f' % alpha)
print('Ks = %f' % Ks)
print('betaLO = %f' % betaLO)
print('betaL = %f' % betaL)
print('gamma = %f' % gamma)
print('mu = %f' % mu)
print('--------------------------\n')
#*****************************************************
# 			Get Roots of Frequency Equation
#*****************************************************
print('BEFORE root finding:')
for i in range(0,Nmodes):
	print('i = %i\t lambda = %.12f\t err = %.5e' % (i,lambdas[i],freqEq(lambdas[i])))

if(EndCond != 'pinned-pinned'):
	GetEigenValues_FreqEq()

print('AFTER root finding:')
for i in range(0,Nmodes):
	print('i = %i\t lambda = %.12f\t err = %.5e' % (i,lambdas[i],freqEq(lambdas[i])))
#*****************************************************
# 				Build Galerkin matrices
#*****************************************************
for k in range(0,Nmodes):
	for l in range(0,Nmodes):
		[b_sr[k,l], c_sr[k,l], d_sr[k,l], e_sr[k,l]] = evaluate_stdel_intgrals(k,l)
#*****************************************************
# 					SOLVER
#*****************************************************
print('-------------- Solver Starting ----------------\n')
# Initialize
u = np.float128(u_min)
for i in range(0,npoints):
	# Update velocity
	u = u + du
	u_store[i] = u

	# Update Matrices
	for k in range(0,Nmodes):
		for l in range(0,Nmodes):
			M[k,l] = M_sr(k,l)
			C[k,l] = C_sr(k,l,u)
			K[k,l] = K_sr(k,l,u)
	
	# Method of Solution: Concatenated Matrices
	B = concatenate4matrices(zeroMat, M, M, C)
	E = concatenate4matrices(-M, zeroMat, zeroMat, K)
	B = np.float64(B)
	E = np.float64(E)
	Y = np.matmul(-np.linalg.inv(B),E) # preferred to np.dot()

	Val, Vec = np.linalg.eig(Y)
	# Val = np.linalg.eigvals(Y)
	omega = Val*(-1.0j)
	# print(Val)
	# print(Vec)
	Vec = Vec.T

	w_scatter_store[i,:] = omega

	# eigenvalue sorting
	omega_plus = np.zeros(2*Nmodes,dtype='complex64')
	eigvec_plus = np.zeros((2*Nmodes,2*Nmodes),dtype='complex64')
	for k in range(0,2*Nmodes):
		if(np.real(omega[k])>=0.0):
			omega_plus[k] = omega[k]
			eigvec_plus[k,:] = Vec[k,:]
	
	# print('----------')
	# print(omega_plus)
	# print(eigvec_plus)
	# print('----------')
	# print('- - -- - -')
	# print(np.nonzero(omega_plus)[0])
	# print('- - -- - -')
	# print('----------')
	# print(eigvec_plus[0,:])
	eigvec_plus = eigvec_plus[np.nonzero(omega_plus)[0],:]
	eigvec_plus = eigvec_plus[:,np.nonzero(omega_plus)[0]]
	# print(eigvec_plus)
	# print('----------')
	# print('----------')

	# Keep only non-zeros
	omega_plus = omega_plus[np.nonzero(omega_plus)]
	if(i==0):
		# print()
		# print('- - -- - -')
		w_store[i,:] = np.sort(omega_plus)
		# print(np.argsort(omega_plus))
		# print(omega_plus)
		eigvec_plus = eigvec_plus[np.argsort(omega_plus),:]
		# print()
		# print(eigvec_plus)
		# eigvec_plus = eigvec_plus[:,np.argsort(omega_plus)]
		# print()
		# print(eigvec_plus)
		# print(w_store[i,:])
		eigvec_store[:,:,i] = eigvec_plus
		# print('- - -- - -')
	else:
		l_min_store = np.zeros(Nmodes,dtype='int64')
		dummy_index = 0
		for l in range(0,Nmodes):
			l_min = np.argmin(np.abs(w_store[i-1,l]-omega_plus))
			w_store[i,l] = omega_plus[l_min]
			l_min_store[dummy_index] = l_min
			dummy_index += 1
		# print('* * * * * * * * * * *')
		# print(omega_plus)
		# print(w_store[i,:])
		# print(l_min_store)
		# print('* * * * * * * * * * *')
		# print()
		# print(eigvec_plus)
		eigvec_plus = eigvec_plus[l_min_store,:]
		# print()
		# print(eigvec_plus)
		eigvec_plus = eigvec_plus[:,l_min_store]
		# print()
		# print(eigvec_plus)
		# print('* * * * * * * * * * *')
		eigvec_store[:,:,i] = eigvec_plus
print('-------------- Solver Converged ---------------\n')
#-----------------------------------------------------
# 				Critical Velocities
#-----------------------------------------------------
u_crit = -np.ones((Nmodes,100),dtype='float64')
for i in range(0,Nmodes):
	u_crit_index=-1
	for l in range(0,(npoints-1)):
		if(np.imag(w_store[l+1,i])*np.imag(w_store[l,i]) < 0.0):
			u_crit_index = u_crit_index+1
			u_crit[i,u_crit_index]=u_store[l]
#-----------------------------------------------------
# Store data
#-----------------------------------------------------
# Store velocities
data_fileName = 'u_store'
np.savetxt(subdirectories[0]+data_fileName+'.'+data_fileType, u_store)
data_fileName = 'u_crit'
np.savetxt(subdirectories[0]+data_fileName+'.'+data_fileType, u_crit)
# Store complex values
real_w_store = np.real(w_store)
imag_w_store = np.imag(w_store)
data_fileName = 'real_w_store'
np.savetxt(subdirectories[0]+data_fileName+'.'+data_fileType, real_w_store)
data_fileName = 'imag_w_store'
np.savetxt(subdirectories[0]+data_fileName+'.'+data_fileType, imag_w_store)
# Store complex values
real_w_scatter_store = np.real(w_scatter_store)
imag_w_scatter_store = np.imag(w_scatter_store)
data_fileName = 'real_w_scatter_store'
np.savetxt(subdirectories[0]+data_fileName+'.'+data_fileType, real_w_store)
data_fileName = 'imag_w_scatter_store'
np.savetxt(subdirectories[0]+data_fileName+'.'+data_fileType, imag_w_store)

# Store eigenvectors
subsubdir = 'eigvec/'
for i in range(0,npoints):
	data_fileName = getFigFileName(i)
	np.savetxt(subdirectories[0]+subsubdir+'real_'+data_fileName+'.'+data_fileType, np.real(eigvec_store[:,:,i]))
	np.savetxt(subdirectories[0]+subsubdir+'imag_'+data_fileName+'.'+data_fileType, np.imag(eigvec_store[:,:,i]))
print('-----------------------------------------------------')