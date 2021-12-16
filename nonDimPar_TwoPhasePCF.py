import numpy as np
#=====================================================
# Nondimensional Relations
#=====================================================
def GetSlipRatio(epsG):
	# Ks = 1.0/((1.0-epsG*(1.0-(rhoG/rhoL)))**0.5) # upward pipe
	Ks_val = (epsG/(1.0-epsG))**0.5 # Hanging pipe
	return Ks_val
#-----------------------------------------------------
def GetVoidFrac(Ks, epsG):
	if((Ks==0.0) and (epsG==0.0)):
		alpha_val = 0.0 # to avoid div by zero
	else:
		alpha_val = epsG/(epsG + Ks*(1.0-epsG))
	return alpha_val
#-----------------------------------------------------
def GetBetaL_betaLO(rhoL, rhoG, betaLO, alpha):
	# Equivalent 2P betaL
	betaL_val = rhoL*(1.0 - alpha)*betaLO
	betaL_val /= rhoL*(1.0-betaLO) + rhoL*(1.0 - alpha)*betaLO + rhoG*alpha*betaLO
	return betaL_val
#-----------------------------------------------------
#=====================================================
# Nondimensional Parameters
#=====================================================
eps = 0.0
rhoG = 1.2
rhoL = 1000.0
betaLO = 0.645
gamma = 0.0
mu = 0.0

# Slip ratio
Ks = GetSlipRatio(eps) # hanging pipe

# Void fraction
alpha = GetVoidFrac(Ks, eps)

# Equivalent 2P betaL
betaL = GetBetaL_betaLO(rhoL, rhoG, betaLO, alpha)
#-----------------------------------------------------
# Convert external parameters to 128 bit
#-----------------------------------------------------
eps = np.float128(eps)
rhoG = np.float128(rhoG)
rhoL = np.float128(rhoL)
betaL = np.float128(betaL)
Ks = np.float128(Ks)
gamma = np.float128(gamma)
mu = np.float128(mu)