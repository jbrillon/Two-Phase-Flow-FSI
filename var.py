import numpy as np
#*****************************************************
# 				GENERAL VARIABLES
#*****************************************************
#=====================================================
# Common file parameters
#=====================================================
subdirectories = ['Data/','Figures/']
data_fileType = 'txt'
figure_fileType = 'pdf'
# End conditions -- do not change
EndCondNames = ['pinned-pinned','fixed-fixed','free-free','fixed-pinned','fixed-free']
#=====================================================
# Inputs
#=====================================================
EndCondIndex = 4 # starting from 0
EndCond = EndCondNames[EndCondIndex] # do not change
# Number of Modes
Nmodes = 11
# Velocity bounds
u_min = 0.0
u_max = 15.0
# Number of points
npoints = 1500
# velocity step
du = np.float128(u_max-u_min)/np.float128(npoints)
#-----------------------------------------------------
# Allocation
#-----------------------------------------------------
# Pre-allocate  
u_store = np.zeros(npoints,dtype='float64')
w_store = np.zeros((npoints,Nmodes),dtype='complex64')
eigvec_store = np.zeros((Nmodes,Nmodes,npoints),dtype='complex64')
w_scatter_store = np.zeros((npoints,2*Nmodes),dtype='complex64')
lambdas = np.zeros(Nmodes, dtype='float128')
#-----------------------------------------------------
# Eigenvalues
#-----------------------------------------------------
if(EndCond == 'fixed-free'):
	lambdas[0] = 1.87510406871196
	lambdas[1] = 4.69409113297417
	lambdas[2] = 7.85475743823761
	lambdas[3] = 10.9955407348754
	if(Nmodes > 4):
		lambdas[4] = 14.1372
		lambdas[5] = 17.2788
		lambdas[6] = 20.4204
		lambdas[7] = 23.5619
	if(Nmodes > 8):
		lambdas[8] = 26.7035
		lambdas[9] = 29.8451
	if(Nmodes > 10):
		lambdas[10] = 32.9867

elif((EndCond == 'fixed-fixed') or (EndCond == 'free-free')):
	lambdas[0] = 4.730041
	lambdas[1] = 7.853205
	lambdas[2] = 10.995608
	lambdas[3] = 14.137165
	if(Nmodes > 4):
		lambdas[4] = 17.2788
		lambdas[5] = 20.4204
		lambdas[6] = 23.5619
		lambdas[7] = 26.7035
	if(Nmodes > 8):
		lambdas[8] = 29.8451
		lambdas[9] = 32.9867
	if(Nmodes > 10):
		lambdas[10] = 36.1283

elif(EndCond == 'pinned-pinned'):
	for i in range(0,Nmodes):
		lambdas[i] = np.float128(np.pi)*np.float128(i+1)

elif(EndCond == 'fixed-pinned'):
	lambdas[0] = 3.926602
	lambdas[1] = 7.068583
	lambdas[2] = 10.210176
	lambdas[3] = 13.351768
	if(Nmodes > 4):
		lambdas[4] = 16.4934
		lambdas[5] = 19.635
		lambdas[6] = 22.7765
		lambdas[7] = 25.9181
	if(Nmodes > 8):
		lambdas[8] = 29.0597
		lambdas[9] = 32.2013
	if(Nmodes > 10):
		lambdas[10] = 35.3429
#-----------------------------------------------------
# Extended Galerkin Method -- move to sep file
#-----------------------------------------------------
# build b,c,d _sr --> Move to a standalone function
b_sr = np.zeros((Nmodes,Nmodes),dtype='float128')
c_sr = np.zeros((Nmodes,Nmodes),dtype='float128')
d_sr = np.zeros((Nmodes,Nmodes),dtype='float128')
e_sr = np.zeros((Nmodes,Nmodes),dtype='float128')
# Kronecker Delta
KD = np.eye(Nmodes,dtype='float128')
# Allocate
M = np.zeros((Nmodes,Nmodes),dtype='float128')
C = np.zeros((Nmodes,Nmodes),dtype='float128')
K = np.zeros((Nmodes,Nmodes),dtype='float128')
# K = np.zeros((Nmodes,Nmodes),dtype='complex128')
zeroMat = np.zeros((Nmodes,Nmodes),dtype='float128')
#=====================================================