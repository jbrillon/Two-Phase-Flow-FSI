import numpy as np
from var import lambdas, EndCond, Nmodes
#*****************************************************
#           BASIS FUNCTIONS SUBROUTINES
#*****************************************************
#=====================================================
def freqEq(x):
    if((EndCond == 'fixed-fixed') or (EndCond == 'free-free')):
        return np.cos(x)*np.cosh(x)-1.0
    elif(EndCond == 'fixed-pinned'):
        return np.tan(x)-np.tanh(x)
    elif(EndCond == 'fixed-free'):
        return np.cos(x)*np.cosh(x)+1.0
    elif(EndCond == 'pinned-pinned'):
        return np.sin(x)
#=====================================================
def dfreqEq_dx(x):
    if((EndCond == 'fixed-fixed') or (EndCond == 'free-free') or (EndCond == 'fixed-free')):
        return np.cos(x)*np.sinh(x)-np.sin(x)*np.cosh(x)
    elif(EndCond == 'fixed-pinned'):
        return ((1.0/np.cos(x))**2.0) - ((1.0/np.cosh(x))**2.0)
    elif(EndCond == 'pinned-pinned'):
        return np.cos(x)
#=====================================================
def GetEigenValues_FreqEq():
    for i in range(0,Nmodes):
        x1 = 1.0*lambdas[i]
        if(i==0):
            x0 = 0.0
        else:
            x0 = lambdas[i-1]
        
        # Newton's root finding method
        while(np.abs(x1-x0)>=(1.0e-15)):
            x0 = 1.0*x1
            x1 = x0 - freqEq(x0)/dfreqEq_dx(x0)

        lambdas[i] = 1.0*x1
#=====================================================
def sigma(r):
    if(EndCond == 'fixed-free'):
        return (np.sinh(lambdas[r])-np.sin(lambdas[r]))/(np.cosh(lambdas[r])+np.cos(lambdas[r]))
    elif((EndCond == 'fixed-fixed') or (EndCond == 'free-free')):
        return (np.cosh(lambdas[r])-np.cos(lambdas[r]))/(np.sinh(lambdas[r])-np.sin(lambdas[r]))
    elif(EndCond == 'pinned-pinned'):
        return 0.0
    elif(EndCond == 'fixed-pinned'):
        return np.float128(1.0)/np.tan(lambdas[r])
#=====================================================
def phi(r,x):
    if(EndCond == 'free-free'):
        return np.cosh(lambdas[r]*x)+np.cos(lambdas[r]*x)-sigma(r)*(np.sinh(lambdas[r]*x)+np.sin(lambdas[r]*x))
    elif((EndCond == 'fixed-free') or ((EndCond == 'fixed-fixed') or (EndCond == 'fixed-pinned'))):
        return np.cosh(lambdas[r]*x)-np.cos(lambdas[r]*x)-sigma(r)*(np.sinh(lambdas[r]*x)-np.sin(lambdas[r]*x))
    elif(EndCond == 'pinned-pinned'):
        return np.sin(lambdas[r]*x)
#=====================================================
def dphi(r,x):
    if(EndCond == 'free-free'):
        return (lambdas[r])*np.sinh(lambdas[r]*x)-(lambdas[r])*np.sin(lambdas[r]*x)-sigma(r)*((lambdas[r])*np.cosh(lambdas[r]*x)+(lambdas[r])*np.cos(lambdas[r]*x))
    elif((EndCond == 'fixed-free') or ((EndCond == 'fixed-fixed') or (EndCond == 'fixed-pinned'))):
        return (lambdas[r])*np.sinh(lambdas[r]*x)+(lambdas[r])*np.sin(lambdas[r]*x)-sigma(r)*((lambdas[r])*np.cosh(lambdas[r]*x)-(lambdas[r])*np.cos(lambdas[r]*x))
    elif(EndCond == 'pinned-pinned'):
        return lambdas[r]*np.cos(lambdas[r]*x)
#=====================================================
def ddphi(r,x):
    if(EndCond == 'free-free'):
        return (lambdas[r]**2.0)*np.cosh(lambdas[r]*x)-(lambdas[r]**2.0)*np.cos(lambdas[r]*x)-sigma(r)*((lambdas[r]**2.0)*np.sinh(lambdas[r]*x)-(lambdas[r]**2.0)*np.sin(lambdas[r]*x))
    elif((EndCond == 'fixed-free') or ((EndCond == 'fixed-fixed') or (EndCond == 'fixed-pinned'))):
        return (lambdas[r]**2.0)*np.cosh(lambdas[r]*x)+(lambdas[r]**2.0)*np.cos(lambdas[r]*x)-sigma(r)*((lambdas[r]**2.0)*np.sinh(lambdas[r]*x)+(lambdas[r]**2.0)*np.sin(lambdas[r]*x))
    elif(EndCond == 'pinned-pinned'):
        return -(lambdas[r]**2.0)*np.sin(lambdas[r]*x)
#=====================================================
def b_sr_integrand(s,r,x):
    return phi(s,x)*dphi(r,x)
#=====================================================
def c_sr_integrand(s,r,x):
    return phi(s,x)*ddphi(r,x)
#=====================================================
def d_sr_integrand(s,r,x):
    return phi(s,x)*x*ddphi(r,x)
#=====================================================
def e_sr_integrand(s,r,x):
    return phi(s,x)*(dphi(r,x) + (x-np.float128(1.0))*ddphi(r,x))
#=====================================================
def evaluate_stdel_intgrals(s,r):
    # standard element domain limits
    a = np.float128(0.0)
    b = np.float128(1.0)

    # number of divisions
    n = 1000

    # Composite Trapezoidal Rule
    h = np.float128(b-a)/np.float128(n)
    sum_b = np.float128(0.0)
    sum_c = np.float128(0.0)
    sum_d = np.float128(0.0)
    sum_e = np.float128(0.0)

    for i in range(1,n):
        x = a + np.float128(i)*h
        sum_b = sum_b+b_sr_integrand(s,r,x)
        sum_c = sum_c+c_sr_integrand(s,r,x)
        sum_d = sum_d+d_sr_integrand(s,r,x)
        sum_e = sum_e+e_sr_integrand(s,r,x)

    b_sr_val = h*(b_sr_integrand(s,r,a)+np.float128(2.0)*sum_b+b_sr_integrand(s,r,b))/np.float128(2.0)
    c_sr_val = h*(c_sr_integrand(s,r,a)+np.float128(2.0)*sum_c+c_sr_integrand(s,r,b))/np.float128(2.0)
    d_sr_val = h*(d_sr_integrand(s,r,a)+np.float128(2.0)*sum_d+d_sr_integrand(s,r,b))/np.float128(2.0)
    e_sr_val = h*(e_sr_integrand(s,r,a)+np.float128(2.0)*sum_e+e_sr_integrand(s,r,b))/np.float128(2.0)

    return [b_sr_val, c_sr_val, d_sr_val, e_sr_val]
#=====================================================