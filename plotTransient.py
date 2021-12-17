# Julien K.L. Brillon
# Purdue University
#-----------------------------------------------------
# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.lines import Line2D
from matplotlib import rc as matplotlibrc
matplotlibrc('text.latex', preamble='\usepackage{color}')
matplotlibrc('text',usetex=True)
matplotlibrc('font', family='serif')
#-----------------------------------------------------
from var import subdirectories,data_fileType,figure_fileType
from responseVar import *
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

tau_max = 30.0
tau = tau[:np.argmin(abs(tau_max-tau))]
np_time = np.size(tau)
c = 1.0*tau
norm = mpl.colors.Normalize(vmin=c.min(), vmax=c.max())
cmap = mpl.cm.ScalarMappable(norm=norm, cmap=mpl.cm.jet)
cmap.set_array([])
cmap.set_clim([0, tau_max])

figure_fileName = 'transient_u%i' % (100.0*u_fixed)

figure_title = "Transient Pipe Motion"
print('Plotting: ' + figure_title)
fig, ax = plt.subplots(figsize=(6,6))
plt.grid()
# ax.set_title(figure_title,fontsize=12,fontweight='bold')
ax.set_ylabel(r'$y$-Coordinate, $\xi$',fontsize=14,rotation=90)
ax.set_xlabel(r'Transverse Deflection, $\eta(\xi,\tau)$',fontsize=14)
ax.set_ylim([0, np.max(xi)])
ax.set_xlim([ylimits[0], ylimits[1]])

i = 26
for k in range(10,np_time):
    if(i==26):
        ax.plot(eta[k,:],xi,linewidth='1.5',color=cmap.to_rgba(tau[k]))
        i = 0
    i += 1

plt.gca().invert_yaxis()

cbar = fig.colorbar(cmap)
cbar.set_label(label=r'Time, $\tau$',fontsize=14)
# plt.tight_layout()
print('\t ... Saving figure ...')
plt.savefig(subdirectories[1] + figure_fileName + '.' + figure_fileType,bbox_inches='tight',format=figure_fileType,dpi=ndpi)
plt.close()
print('-----------------------------------------------------')