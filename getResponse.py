# Julien K.L. Brillon
# Purdue University
#-----------------------------------------------------
# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib import rc as matplotlibrc
# matplotlibrc('text.latex', preamble='\usepackage{color}')
# matplotlibrc('text',usetex=True)
# matplotlibrc('font', family='serif')
#-----------------------------------------------------
from var import *
from polylib import *
from operations import *
from responseVar import *
#-----------------------------------------------------
# Plot parameters
#-----------------------------------------------------
clr = ['b','r','g','Nmodes','c','k','y']
mrkr = ['s','o','^','v','>','<','d']
#-----------------------------------------------------
Nmodes -= 1 # number of modes used for response
modes = range(1,Nmodes+1)
names = [None]*Nmodes
for l in range(0,Nmodes):
    names[l] = "Mode %i" % modes[l]
#-----------------------------------------------------
# load complex
data_fileName = 'real_w_store'
real_omega = np.loadtxt(subdirectories[0]+subsubdir_data+data_fileName+'.'+data_fileType, unpack=False)
data_fileName = 'imag_w_store'
imag_omega = np.loadtxt(subdirectories[0]+subsubdir_data+data_fileName+'.'+data_fileType, unpack=False)
omega = real_omega + (1.0j)*imag_omega
#-----------------------------------------------------
#*****************************************************
#           Get Roots of Frequency Equation
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
#           Build transverse tip deflection
#*****************************************************
tau = np.linspace(0.0,tauF,np_time,dtype='float64')
xi = np.linspace(0.0,1.0,np_space,dtype='float64')
if(u_fixed_flag == 0):
    eta = np.zeros((npoints,np_time),dtype='float64')
elif(u_fixed_flag == 1):
    eta = np.zeros((np_time,np_space),dtype='float64')

data_fileName = 'tau'
np.savetxt(subdirectories[0]+data_fileName+'.'+data_fileType, tau)
data_fileName = 'xi'
np.savetxt(subdirectories[0]+data_fileName+'.'+data_fileType, xi)

subsubdir_data += 'eigvec/'

for i in range(iStart,iEnd):
    data_fileName = getFigFileName(i)
    real_eigvec = np.loadtxt(subdirectories[0]+subsubdir_data+'real_'+data_fileName+'.'+data_fileType, unpack=False)
    imag_eigvec = np.loadtxt(subdirectories[0]+subsubdir_data+'imag_'+data_fileName+'.'+data_fileType, unpack=False)
    eigvec = real_eigvec + (1.0j)*imag_eigvec
    eigvec_store[:,:,i] = eigvec

if(u_fixed_flag == 0):
    print('Computing response for: ')
    for k in range(iStart,iEnd):
        print('\t n = %i:\tu = %.2f' % (k,u_store[k]))
        for i in range(0,np_time):
            eta[k,i] = 0.0
            for r in range(0,Nmodes):
                qr = 0.0
                for s in range(0,Nmodes):
                    qr += np.real(eigvec_store[s,r,k]*np.exp(1.0j*omega[k,s]*tau[i]))
                eta[k,i] += phi(r,1.0)*qr
    data_fileName = 'eta_tip'
    

elif(u_fixed_flag == 1):
    for k in range(0,np_time):
        print('\t n = %i:\t tau = %.2f' % (k,tau[k]))
        for i in range(0,np_space):
            eta[k,i] = 0.0
            for r in range(0,Nmodes):
                qr = 0.0
                for s in range(0,Nmodes):
                    qr += np.real(eigvec_store[s,r,k_fixed]*np.exp(1.0j*omega[k_fixed,s]*tau[k]))
                eta[k,i] += phi(r,xi[i])*qr
    data_fileName = 'eta_space'

np.savetxt(subdirectories[0]+data_fileName+'.'+data_fileType, eta)

print('-----------------------------------------------------')