# Julien K.L. Brillon
# Purdue University
#-----------------------------------------------------
# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib import rc as matplotlibrc
matplotlibrc('text.latex', preamble='\usepackage{color}')
matplotlibrc('text',usetex=True)
matplotlibrc('font', family='serif')
#-----------------------------------------------------
from var import subdirectories,data_fileType,figure_fileType
from responseVar import *
from operations import *
#-----------------------------------------------------
# load response
data_fileName = 'eta_tip'
eta_1p = np.loadtxt(subdirectories[0]+subsubdir_data_1p+data_fileName+'.'+data_fileType, unpack=False)
data_fileName = 'tau'
tau_1p = np.loadtxt(subdirectories[0]+subsubdir_data_1p+data_fileName+'.'+data_fileType, unpack=False)
# load response
data_fileName = 'eta_tip'
eta_2p = np.loadtxt(subdirectories[0]+subsubdir_data_2p+data_fileName+'.'+data_fileType, unpack=False)
data_fileName = 'tau'
tau_2p = np.loadtxt(subdirectories[0]+subsubdir_data_2p+data_fileName+'.'+data_fileType, unpack=False)
#-----------------------------------------------------
#*****************************************************
#           Plot deflection at tip
#*****************************************************
print("---------------------------------------------")
for k in range(iStart,iEnd):
    figure_fileName = getFigFileName(k)
    figure_title = 'n = %i' % k
    print('Plotting: ' + figure_title)
    fig, ax = plt.subplots(1,2,figsize=(12,6))
    ax[0].set_title(r'$1\phi$ ($\epsilon=0$)',fontsize=14,fontweight='bold')
    ax[1].set_title(r'$2\phi$ ($\epsilon=0.05$)',fontsize=14,fontweight='bold')
    vel_name = r'$u_{l}=%.2f$' % u_store[k]
    for i in range(0,2):
        ax[i].set_xlabel(r'Time, $\tau$',fontsize=14)
        ax[i].set_ylabel(r'Transverse Tip Deflection, $\eta(1,\tau)$',rotation=90,fontsize=14)
        
        ax[i].set_ylim([ylimits[0], ylimits[1]])
        ax[i].grid()
        t = ax[i].text(0.8, 0.95, vel_name, transform=ax[i].transAxes, fontsize=14)
        t.set_bbox(dict(facecolor='white', alpha=1.0, edgecolor='none'))
    
    ax[0].set_xlim([0, np.max(tau_1p)])
    ax[1].set_xlim([0, np.max(tau_2p)])
    # ax.axhline(y=0, color='k', linestyle='-',linewidth='0.5')
    
    # fig.suptitle(vel_name, fontsize=14)
    ax[0].plot(tau_1p, eta_1p[k,:],color='k',linewidth='0.75')
    ax[1].plot(tau_2p, eta_2p[k,:],color='k',linewidth='0.75')
    # leg = plt.legend(loc='upper right', ncol=1, shadow=False, fancybox=True, fontsize=13)
    plt.tight_layout()
    print('\t ... Saving figure ...')
    plt.savefig(subdirectories[1] + subsubdir_fig + figure_fileName + '.' + figure_fileType,bbox_inches='tight',format=figure_fileType,dpi=500)
    plt.close()

print('-----------------------------------------------------')