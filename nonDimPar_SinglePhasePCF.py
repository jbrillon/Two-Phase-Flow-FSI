import numpy as np
#-----------------------------------------------------
# Nondimensional Parameters
#-----------------------------------------------------
alpha = 0.0
sigma_const = 0.0
beta = 0.295
k_const = 0.0
Gamma = 0.0 # captital gamma
Pi = 0.0
nu_const = 1.0
delta_const = 1.0
gamma = 10.0
#-----------------------------------------------------
# Convert parameters to 128 bit
#-----------------------------------------------------
alpha = np.float128(alpha)
sigma_const = np.float128(sigma_const)
beta = np.float128(beta)
k_const = np.float128(k_const)
Gamma = np.float128(Gamma)
Pi = np.float128(Pi)
nu_const = np.float128(nu_const)
delta_const = np.float128(delta_const)
gamma = np.float128(gamma)