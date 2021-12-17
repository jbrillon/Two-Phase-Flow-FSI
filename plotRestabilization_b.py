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
from var import *
#-----------------------------------------------------
# Plot parameters
#-----------------------------------------------------
clr = ['b','r','g','tab:purple','c','k','y']
mrkr = ['s','o','^','v','>','<','d']
#-----------------------------------------------------
# Common
#-----------------------------------------------------
xlimits = [-1,82]
ylimits = [-2.5,10]
#-----------------------------------------------------
# Common
#-----------------------------------------------------
# u_mkr_values = [2.0,4.0,8.0,12.0]
u_mkr_values = []
u_mkr_values = np.array(u_mkr_values)
u_mkr_values = list(u_mkr_values)
#-----------------------------------------------------
modes = range(1,Nmodes+1)
names = [None]*Nmodes
for l in range(0,Nmodes):
    names[l] = "Mode %i" % modes[l]

subdirectories[0] += 'restabilization/'
#-----------------------------------------------------
print("---------------------------------------------")

figure_fileName = 'argand_restable_b'
figure_title = 'Argand Plot'
print('Plotting: ' + figure_title)
fig, ax = plt.subplots(figsize=(6,6))
plt.grid()
# ax.set_title(figure_title,fontsize=12,fontweight='bold')
ax.set_xlabel(r'Re$(\omega)$',fontsize=14)
ax.set_ylabel(r'Im$(\omega)$',rotation=90,fontsize=14)
ax.set_xlim(xlimits)
ax.set_ylim(ylimits)
ax.axhline(y=0, color='k', linestyle='--')
#-----------------------------------------------------
# Load data -- eps = 0.00
#-----------------------------------------------------
subsubdir = 'eps083/'
data_fileName = 'u_store'
u = np.loadtxt(subdirectories[0]+subsubdir+data_fileName+'.'+data_fileType, unpack=False)
# load complex
data_fileName = 'real_w_store'
real_omega = np.loadtxt(subdirectories[0]+subsubdir+data_fileName+'.'+data_fileType, unpack=False)
data_fileName = 'imag_w_store'
imag_omega = np.loadtxt(subdirectories[0]+subsubdir+data_fileName+'.'+data_fileType, unpack=False)
omega = real_omega + (1.0j)*imag_omega

for i in range(0,4):
    ax.plot(np.real(omega[:,i]), np.imag(omega[:,i]),color=clr[i],linestyle='--')

#-----------------------------------------------------
# Load data -- eps = 0.01
#-----------------------------------------------------
subsubdir = 'eps085/'
data_fileName = 'u_store'
u = np.loadtxt(subdirectories[0]+subsubdir+data_fileName+'.'+data_fileType, unpack=False)
# load complex
data_fileName = 'real_w_store'
real_omega = np.loadtxt(subdirectories[0]+subsubdir+data_fileName+'.'+data_fileType, unpack=False)
data_fileName = 'imag_w_store'
imag_omega = np.loadtxt(subdirectories[0]+subsubdir+data_fileName+'.'+data_fileType, unpack=False)
omega = real_omega + (1.0j)*imag_omega

for i in range(0,4):
    ax.plot(np.real(omega[:,i]), np.imag(omega[:,i]),color=clr[i],linestyle='-.')

plt.text(1, 1, r'\textbf{Mode 1}', {'color': clr[0], 'fontsize': 13})
plt.text(24, 1, r'\textbf{Mode 2}', {'color': clr[1], 'fontsize': 13})
plt.text(67, 1, r'\textbf{Mode 3}', {'color': clr[2], 'fontsize': 13})
# plt.text(121, -1.5, r'\textbf{Mode 4}', {'color': clr[3], 'fontsize': 13})

legend_elements = [Line2D([0],[0], color='k', linestyle='--', label=r'Two-phase $(\epsilon=0.83)$'),
                    Line2D([0],[0], color='k', linestyle='-.', label=r'Two-phase $(\epsilon=0.85)$')]
leg = plt.legend(handles=legend_elements, loc='best', ncol=1, shadow=True, fancybox=True, fontsize=13)
plt.tight_layout()

print('\t ... Saving figure ...')
plt.savefig(subdirectories[1] + figure_fileName + '.' + figure_fileType,bbox_inches='tight',format=figure_fileType,dpi=500)
plt.close()
print('-----------------------------------------------------')