import numpy as np
from var import *
#-----------------------------------------------------
# Parameters
#-----------------------------------------------------
from nonDimPar_TwoPhasePCF import *
#=====================================================
# 				EQUATION OF MOTION
#=====================================================
# Description: From 2019 JFS
#-----------------------------------------------------
# mass matrix element
#-----------------------------------------------------
def M_sr(s,r):
	val = KD[s,r]
	return val
#-----------------------------------------------------
# damping matrix element
#-----------------------------------------------------
def C_sr(s,r,uL):
	val = 2.0*np.sqrt(betaL)*uL*(1.0 + (rhoG/rhoL)*(eps/(1.0-eps)))*b_sr[s,r]
	return val
#-----------------------------------------------------
# stiffness matrix element
#-----------------------------------------------------
def K_sr(s,r,uL):
	# val = (1.0+mu*1.0j)*(lambdas[r]**4.0)*KD[s,r]
	val = (lambdas[r]**4.0)*KD[s,r]
	val += (uL**2.0)*(1.0 + Ks*(rhoG/rhoL)*(eps/(1.0-eps)))*c_sr[s,r]
	val += gamma*e_sr[s,r]
	return val
#=====================================================