import numpy as np
from var import *
from polylib import *
#-----------------------------------------------------
# Parameters
#-----------------------------------------------------
from nonDimPar_SinglePhasePIAF import *
#=====================================================
#               EQUATION OF MOTION
#=====================================================
# Description: Cantilever pipe in axial flow with tapered end
#-----------------------------------------------------
# mass matrix element
#-----------------------------------------------------
def M_sr(s,r):
    val = (1.0+(X-1.0)*beta)*KD[s,r]+(1.0+(f*X-1.0)*beta)*Xe*phi(s,1.0)*phi(r,1.0)
    return val
#-----------------------------------------------------
# damping matrix element
#-----------------------------------------------------
def C_sr(s,r,u):
    val = (alpha*lambdas[r]**4.0+0.5*epsilon*c_n*np.sqrt(beta)*u + 0.5*epsilon*c*np.sqrt(beta))*KD[s,r]
    val += 2.0*X*np.sqrt(beta)*u*b_sr[s,r]
    val += -(X*f-0.5*Xe_nom*epsilon*c_n)*np.sqrt(beta)*u*phi(r,1.0)*phi(s,1.0)
    val += Xe*X*f*np.sqrt(beta)*u*phi(s,1.0)*dphi(r,1.0)
    return val
#-----------------------------------------------------
# stiffness matrix element
#-----------------------------------------------------
def K_sr(s,r,u):
    val = (lambdas[r]**4.0)*KD[s,r]+(X-0.5*c_b)*(u**2.0)*c_sr[s,r]
    val += (0.5*(epsilon*c_n+epsilon*c_t*h)*u**2.0+gamma)*b_sr[s,r]
    val += (0.5*epsilon*c_t*(u**2.0)*(1.0+h)+gamma)*(d_sr[s,r]-c_sr[s,r])
    val += (0.5*(epsilon*c_n*Xe_nom+epsilon*c_t*h*Xe)*(u**2.0)-X*f*(u**2.0)+gamma*Xe)*phi(s,1.0)*dphi(r,1.0)
    return val
#=====================================================