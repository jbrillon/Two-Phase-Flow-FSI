import numpy as np
from var import subdirectories,data_fileType
#*****************************************************
#               GENERAL VARIABLES
#*****************************************************
#=====================================================
# Common file parameters
#=====================================================
subsubdir_data = 'restabilization/eps010/response/'
subsubdir_fig = 'restable_spaceResponse/'
u_fixed_flag = 1 # 0 (OFF) or 1 (ON)
ylimits = [-3,3]
# ylimits = [-15,15]
data_fileName = 'u_store'
u_store = np.loadtxt(subdirectories[0]+subsubdir_data+data_fileName+'.'+data_fileType, unpack=False)
npoints = np.size(u_store)
iStart = 0
iEnd = u_store.size
# iStart = 0
# iEnd = 250
#-----------------
np_time = 301
np_space = 1000
tauF = 30.0
#-----------------------------------------------------
# for plotting two responses
#-----------------------------------------------------
# subsubdir_data_1p = 'lowvelocity/1p/'
# subsubdir_data_2p = 'lowvelocity/2p/'
subsubdir_data_1p = 'highvelocity/1p/'
subsubdir_data_2p = 'highvelocity/2p/'
#-----------------------------------------------------
# fixed velocity response
#-----------------------------------------------------
u_fixed = 15.85
if(u_fixed_flag == 1):
    k_fixed = np.argmin(abs(u_fixed-u_store))
    print('Fixed velocity: u = %.2f\n' % u_store[k_fixed])
    iStart = 1*k_fixed
    iEnd = iStart+1

