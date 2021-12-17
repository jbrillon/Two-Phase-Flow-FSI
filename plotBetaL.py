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
n = 2000
betaLO = np.linspace(0.0,1.0,n)
alpha = np.linspace(0.0001,1.0,n)
betaL = np.zeros((n,n),dtype='float64')

for j in range(0,n):
    for i in range(0,n):
        betaL[i,j] = GetBetaL_betaLO(rhoL, rhoG, betaLO[j], alpha[i])

#-----------------------------------------------------
X, Y = np.meshgrid(alpha,betaLO)
Z = betaL

figure_title = "Contour plot"
figure_title_print = figure_title
print('Plotting: ' + figure_title_print)
fig= plt.figure(figure_title,figsize=(5,4))
# plt.title(figure_title)
plt.ylabel(r"$\beta_{l_{0}}$ ($1\phi$ Liquid)")
plt.xlabel(r"Void Fraction, $\alpha$")
# Limits
plt.xlim([0,1])
plt.ylim([0,1])
# cs = plt.contourf(X,Y,Z, np.linspace(np.min(Z),np.max(Z),1000),cmap='rainbow')
cs = plt.contourf(X,Y,np.transpose(Z), np.linspace(0.0,1.0,100),cmap='rainbow')
fig.colorbar(cs,label=r'$\beta_{l}$ ($2\phi$ Liquid)',ticks=np.arange(0,1.01,0.1))

# Fix for the white lines between contour levels
for c in cs.collections:
    c.set_edgecolor("face")

plt.tight_layout()
print('... Saving figure ...')
filename = "betaL_contourf"
figure_fileType = 'png'
subdirectory = subdirectories[1]
plt.savefig(subdirectory + filename + '.' + figure_fileType,format=figure_fileType,dpi=500)
plt.close()
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