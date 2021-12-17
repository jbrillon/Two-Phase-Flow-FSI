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
xlimits = [-1,15]
ylimits = [-1,65]
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

subdirectories[0] += 'clamped/'
#-----------------------------------------------------
print("---------------------------------------------")

figure_fileName = 'argand_clampled_real_vs_u'
figure_title = 'Argand Plot'
print('Plotting: ' + figure_title)
fig, ax = plt.subplots(figsize=(6,6))
plt.grid()
# ax.set_title(figure_title,fontsize=12,fontweight='bold')
ax.set_xlabel(r'$u_{l}$',fontsize=14)
ax.set_ylabel(r'Re$(\omega)$',rotation=90,fontsize=14)
ax.set_xlim(xlimits)
ax.set_ylim(ylimits)
# ax.axhline(y=0, color='k', linestyle='--')
#-----------------------------------------------------
# Load data -- one phase
#-----------------------------------------------------
subsubdir = '1p/'
data_fileName = 'u_store'
u = np.loadtxt(subdirectories[0]+subsubdir+data_fileName+'.'+data_fileType, unpack=False)
# load complex
data_fileName = 'real_w_store'
real_omega = np.loadtxt(subdirectories[0]+subsubdir+data_fileName+'.'+data_fileType, unpack=False)
data_fileName = 'imag_w_store'
imag_omega = np.loadtxt(subdirectories[0]+subsubdir+data_fileName+'.'+data_fileType, unpack=False)
omega = real_omega + (1.0j)*imag_omega

for i in range(0,2):
    ax.plot(u, np.real(omega[:,i]),color=clr[i],linestyle='-')

#-----------------------------------------------------
# Load data -- two phase
#-----------------------------------------------------
subsubdir = '2p/'
data_fileName = 'u_store'
u = np.loadtxt(subdirectories[0]+subsubdir+data_fileName+'.'+data_fileType, unpack=False)
# load complex
data_fileName = 'real_w_store'
real_omega = np.loadtxt(subdirectories[0]+subsubdir+data_fileName+'.'+data_fileType, unpack=False)
data_fileName = 'imag_w_store'
imag_omega = np.loadtxt(subdirectories[0]+subsubdir+data_fileName+'.'+data_fileType, unpack=False)
omega = real_omega + (1.0j)*imag_omega

for i in range(0,2):
    ax.plot(u, np.real(omega[:,i]),color=clr[i],linestyle='--')

plt.text(1, 15, r'\textbf{Mode 1}', {'color': clr[0], 'fontsize': 13})
plt.text(1, 53, r'\textbf{Mode 2}', {'color': clr[1], 'fontsize': 13})
# plt.text(67, 1, r'\textbf{Mode 3}', {'color': clr[2], 'fontsize': 13})
# plt.text(67, 1, r'\textbf{Mode 4}', {'color': clr[2], 'fontsize': 13})

legend_elements = [Line2D([0],[0], color='k', linestyle='-', label=r'Liquid only $(\epsilon=0)$'),
                    Line2D([0],[0], color='k', linestyle='--', label=r'Two-phase $(\epsilon=0.4)$')]
leg = plt.legend(handles=legend_elements, loc='best', ncol=1, shadow=True, fancybox=True, fontsize=13)
plt.tight_layout()

print('\t ... Saving figure ...')
plt.savefig(subdirectories[1] + figure_fileName + '.' + figure_fileType,bbox_inches='tight',format=figure_fileType,dpi=500)
plt.close()
print('-----------------------------------------------------')