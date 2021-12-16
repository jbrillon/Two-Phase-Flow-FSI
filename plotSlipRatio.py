# Import libraries
import numpy as np # NumPy: contains basic numerical routines
import scipy # SciPy: contains additional numerical routines to numpy
import matplotlib.pyplot as plt # Matlab-like plotting
import scipy.sparse as scysparse
import scipy.sparse.linalg
#-----------------------------------------------------
from matplotlib.lines import Line2D
from matplotlib import rc as matplotlibrc
matplotlibrc('text.latex', preamble='\usepackage{color}')
matplotlibrc('text',usetex=True)
matplotlibrc('font', family='serif')
#-----------------------------------------------------
subdirectories = ['Data/','Figures/']
data_fileType = 'txt'
figure_fileType = 'pdf'	
clr = ['b','r','g','m','c','k','y']
mrkr = ['s','o','^','v','>','<','d']
#-----------------------------------------------------
from nonDimPar_TwoPhasePCF import *
eps = np.linspace(0.0001,1.0,10000)
Ks = GetSlipRatio(eps)
alpha = GetVoidFrac(Ks, eps)
#-----------------------------------------------------
# print("---------------------------------------------")
# y_label_L = '$K_{s}$'
# x_label = r'$\epsilon_{G}$'
# y_label_R = r'$\alpha_{G}$'
# figure_fileName = 'correct_ks'
# figure_title = 'Correct Slip Ratio'
# print('Plotting: ' + figure_title)
# fig, ax1 = plt.subplots(figsize=(7,7))
# plt.grid()
# # ax.set_title(figure_title,fontsize=12,fontweight='bold')
# ax1.set_xlabel(x_label,fontsize=14)
# ax1.set_ylabel(y_label_L,rotation=90,fontsize=14,color=clr[0])
# ax1.plot(epsG, Ks_correct, color=clr[0])

# ax2 = ax1.twinx()
# ax2.set_ylabel(y_label_R,rotation=90,fontsize=14,color=clr[1])
# ax2.plot(epsG, alphaG_Ks_correct, color=clr[1])

# print('\t ... Saving figure ...')
# plt.savefig(subdirectories[1] + figure_fileName + '.' + figure_fileType,bbox_inches='tight',format=figure_fileType,dpi=500)
# plt.close()
#-----------------------------------------------------
print("---------------------------------------------")
y_label_L = 'Slip Ratio, $K_{s}$'
y_label_R = r'Void Fraction, $\alpha$'
x_label = r'Volumetric Quality, $\epsilon$'
figure_fileName = 'ks_alpha_vs_eps'
figure_title = 'Slip Ratio and Void Fraction'
print('Plotting: ' + figure_title)
fig, ax1 = plt.subplots(figsize=(6,6))
plt.grid()
# ax.set_title(figure_title,fontsize=12,fontweight='bold')
ax1.set_xlabel(x_label,fontsize=14)
# ax1.set_ylabel(y_label_L,rotation=90,fontsize=14,color=clr[0])
ax1.set_ylabel(y_label_L,rotation=90,fontsize=14,color=clr[0])
ax1.plot(eps, Ks, color=clr[0])
ax1.tick_params(axis='y', labelcolor=clr[0])
ax1.set_xlim(0,1)
ax1.set_ylim(0,10)

ax2 = ax1.twinx()
ax2.set_ylabel(y_label_R,fontsize=14,color=clr[1])
ax2.plot(eps, alpha, color=clr[1])
ax2.tick_params(axis='y', labelcolor=clr[1])
ax2.set_ylim(0,1)

print('\t ... Saving figure ...')
plt.savefig(subdirectories[1] + figure_fileName + '.' + figure_fileType,bbox_inches='tight',format=figure_fileType,dpi=500)
plt.close()
#-----------------------------------------------------