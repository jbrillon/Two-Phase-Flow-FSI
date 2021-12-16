import numpy as np
from var import *
#-----------------------------------------------------
# Parameters
#-----------------------------------------------------
from nonDimPar_SinglePhasePCF import *
#=====================================================
# 				EQUATION OF MOTION
#=====================================================
# Description: From 2014 Paidoussis Book, Eq.(3.91)
#-----------------------------------------------------
# mass matrix element
#-----------------------------------------------------
def M_sr(s,r):
	val = KD[s,r]
	return val
#-----------------------------------------------------
# damping matrix element
#-----------------------------------------------------
def C_sr(s,r,u):
	val = (alpha*(lambdas[r]**4.0) + sigma_const)*KD[s,r]
	val += 2.0*np.sqrt(beta)*u*b_sr[s,r]
	return val
#-----------------------------------------------------
# stiffness matrix element
#-----------------------------------------------------
def K_sr(s,r,u):
	val = (lambdas[r]**4.0 + k_const)*KD[s,r]
	val += ((u**2.0) - Gamma + Pi*(1.0-2.0*nu_const*delta_const) - gamma)*c_sr[s,r]
	val += gamma*b_sr[s,r] + gamma*d_sr[s,r]
	return val
#=====================================================