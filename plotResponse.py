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
if(u_fixed_flag == 0):
    data_fileName = 'eta_tip'
    eta = np.loadtxt(subdirectories[0]+subsubdir_data+data_fileName+'.'+data_fileType, unpack=False)
    data_fileName = 'tau'
    tau = np.loadtxt(subdirectories[0]+subsubdir_data+data_fileName+'.'+data_fileType, unpack=False)
elif(u_fixed_flag == 1):
    subsubdir_data += 'space/'
    data_fileName = 'eta_space'
    eta = np.loadtxt(subdirectories[0]+subsubdir_data+data_fileName+'.'+data_fileType, unpack=False)
    data_fileName = 'tau'
    tau = np.loadtxt(subdirectories[0]+subsubdir_data+data_fileName+'.'+data_fileType, unpack=False)
    data_fileName = 'xi'
    xi = np.loadtxt(subdirectories[0]+subsubdir_data+data_fileName+'.'+data_fileType, unpack=False)
#-----------------------------------------------------
ndpi = 500 # set to 500
#*****************************************************
#           Plot deflection at tip
#*****************************************************
print("---------------------------------------------")
if(u_fixed_flag == 0):
    for k in range(iStart,iEnd):
        figure_fileName = getFigFileName(k)
        figure_title = 'n = %i' % k
        print('Plotting: ' + figure_title)
        fig, ax = plt.subplots(figsize=(6,6))
        plt.grid()
        # ax.set_title(figure_title,fontsize=12,fontweight='bold')
        ax.set_xlabel(r'Time, $\tau$',fontsize=14)
        ax.set_ylabel(r'Transverse Tip Deflection, $\eta(1,\tau)$',rotation=90,fontsize=14)
        ax.set_xlim([0, np.max(tau)])
        ax.set_ylim([ylimits[0], ylimits[1]])
        # ax.axhline(y=0, color='k', linestyle='-',linewidth='0.5')
        vel_name = r'$u_{l}=%.2f$' % u_store[k]
        ax.set_title(vel_name,fontsize='14')
        ax.plot(tau, eta[k,:],color='k',linewidth='0.75')
        # leg = plt.legend(loc='upper right', ncol=1, shadow=False, fancybox=True, fontsize=13)
        plt.tight_layout()
        print('\t ... Saving figure ...')
        plt.savefig(subdirectories[1] + subsubdir_fig + figure_fileName + '.' + figure_fileType,bbox_inches='tight',format=figure_fileType,dpi=ndpi)
        plt.close()
elif(u_fixed_flag == 1):
    for k in range(0,np_time):
        figure_fileName = getFigFileName(k)
        figure_title = 'n = %i' % k
        print('Plotting: ' + figure_title)
        fig, ax = plt.subplots(figsize=(6,6))
        plt.grid()
        # ax.set_title(figure_title,fontsize=12,fontweight='bold')
        ax.set_xlabel(r'$x$-Coordinate, $\xi$',fontsize=14)
        ax.set_ylabel(r'Transverse Deflection, $\eta(\xi,\tau)$',rotation=90,fontsize=14)
        ax.set_xlim([0, np.max(xi)])
        ax.set_ylim([ylimits[0], ylimits[1]])
        # ax.axhline(y=0, color='k', linestyle='-',linewidth='0.5')
        vel_name = r'$\tau=%.1f$' % tau[k]
        ax.set_title(vel_name,fontsize='14')
        ax.plot(xi, eta[k,:],color='k',linewidth='1.5')
        # leg = plt.legend(loc='upper right', ncol=1, shadow=False, fancybox=True, fontsize=13)
        plt.tight_layout()
        print('\t ... Saving figure ...')
        plt.savefig(subdirectories[1] + subsubdir_fig + figure_fileName + '.' + figure_fileType,bbox_inches='tight',format=figure_fileType,dpi=ndpi)
        plt.close()

print('-----------------------------------------------------')