# Julien K.L. Brillon
# Purdue University
#-----------------------------------------------------
# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib import rc as matplotlibrc
# matplotlibrc('text.latex', preamble='\usepackage{color}')
# matplotlibrc('text',usetex=True)
# matplotlibrc('font', family='serif')
#-----------------------------------------------------
from var import *
#-----------------------------------------------------
# Plot parameters
#-----------------------------------------------------
clr = ['b','r','g','Nmodes','c','k','y']
mrkr = ['s','o','^','v','>','<','d']
#-----------------------------------------------------
modes = range(1,Nmodes+1)
names = [None]*Nmodes
for l in range(0,Nmodes):
	names[l] = "Mode %i" % modes[l]
#-----------------------------------------------------
# Load data
#-----------------------------------------------------
data_fileName = 'u_store'
u = np.loadtxt(subdirectories[0]+data_fileName+'.'+data_fileType, unpack=True)
# load complex
data_fileName = 'real_w_store'
real_omega = np.loadtxt(subdirectories[0]+data_fileName+'.'+data_fileType, unpack=False)
data_fileName = 'imag_w_store'
imag_omega = np.loadtxt(subdirectories[0]+data_fileName+'.'+data_fileType, unpack=False)
omega = real_omega + (1.0j)*imag_omega
data_fileName = 'real_w_scatter_store'
real_omega_scatter = np.loadtxt(subdirectories[0]+data_fileName+'.'+data_fileType, unpack=False)
data_fileName = 'imag_w_scatter_store'
imag_omega_scatter = np.loadtxt(subdirectories[0]+data_fileName+'.'+data_fileType, unpack=False)
omega_scatter = real_omega_scatter + (1.0j)*imag_omega_scatter
#-----------------------------------------------------
print("---------------------------------------------")
figure_fileName = 'argand'
figure_title = 'Argand Plot'
print('Plotting: ' + figure_title)
fig, ax = plt.subplots(figsize=(7,7))
plt.grid()
# ax.set_title(figure_title,fontsize=12,fontweight='bold')
ax.set_xlabel(r'$Re(\omega)$',fontsize=14)
ax.set_ylabel(r'$Im(\omega)$',rotation=90,fontsize=14)
ax.set_xlim([-1, 60])
ax.set_ylim([-25, 25])
ax.axhline(y=0, color='k', linestyle='--')
for i in range(0,4):
	ax.plot(np.real(omega[:,i]), np.imag(omega[:,i]),label=names[i])
# leg = plt.legend(loc='best', ncol=1, shadow=True, fancybox=True, fontsize=13)
# ax.plot(x_axis_plot,np.zeros(npoints),'k')
print('\t ... Saving figure ...')
plt.savefig(subdirectories[1] + figure_fileName + '.' + figure_fileType,bbox_inches='tight',format=figure_fileType,dpi=500)
plt.close()
#-----------------------------------------------------
print("---------------------------------------------")
x_lim = u_max
x_axis_plot = np.linspace(0,x_lim,npoints)
figure_fileName = 'velocity_imag'
figure_title = 'Velocity Plot'
print('Plotting: ' + figure_title)
fig, ax = plt.subplots(figsize=(7,7))
plt.grid()
# ax.set_title(figure_title,fontsize=12,fontweight='bold')
ax.set_xlabel(r'$u$',fontsize=14)
ax.set_ylabel(r'$Im(\omega)$',rotation=90,fontsize=14)
ax.set_xlim([0, x_lim])
ax.set_ylim([-20, 20])
# ax.plot(x_axis_plot,np.zeros(npoints),'k')
# ax.axhline(y=0, color='k', linestyle='-')
for i in range(0,Nmodes):
	ax.plot(u, np.imag(omega[:,i]),label=('%i'%i),linestyle='--')
# leg = plt.legend(loc='best', ncol=3, shadow=True, fancybox=True, fontsize=13)
print('\t ... Saving figure ...')
plt.savefig(subdirectories[1] + figure_fileName + '.' + figure_fileType,bbox_inches='tight',format=figure_fileType,dpi=500)
plt.close()
#-----------------------------------------------------
print("---------------------------------------------")
x_lim = u_max
x_axis_plot = np.linspace(0,x_lim,npoints)
figure_fileName = 'velocity_real'
figure_title = 'Velocity Plot'
print('Plotting: ' + figure_title)
fig, ax = plt.subplots(figsize=(7,7))
plt.grid()
# ax.set_title(figure_title,fontsize=12,fontweight='bold')
ax.set_xlabel(r'$u$',fontsize=14)
ax.set_ylabel(r'$Re(\omega)$',rotation=90,fontsize=14)
ax.set_xlim([0, x_lim])
ax.set_ylim([-1, 125])
# ax.plot(x_axis_plot,np.zeros(npoints),'k')
# ax.axhline(y=0, color='k', linestyle='-')
for i in range(0,Nmodes):
	ax.plot(u, np.real(omega[:,i]),label=('%i'%i),linestyle='--')
# leg = plt.legend(loc='best', ncol=3, shadow=True, fancybox=True, fontsize=13)
print('\t ... Saving figure ...')
plt.savefig(subdirectories[1] + figure_fileName + '.' + figure_fileType,bbox_inches='tight',format=figure_fileType,dpi=500)
plt.close()

exit()
#-----------------------------------------------------
print("---------------------------------------------")
x_axis_plot = np.linspace(0,x_lim,npoints)
figure_fileName = 'argand_full'
figure_title = 'Argand Plot'
print('Plotting: ' + figure_title)
fig, ax = plt.subplots(figsize=(7,7))
plt.grid()
# ax.set_title(figure_title,fontsize=12,fontweight='bold')
ax.set_xlabel(r'$Re(\omega)$',fontsize=14)
ax.set_ylabel(r'$Im(\omega)$',rotation=90,fontsize=14)
ax.set_xlim([0, 130])
ax.set_ylim([-20, 30])
ax.set_aspect(1.2)
ax.axhline(y=0, color='k', linestyle='--')
for i in range(0,4):
	ax.plot(np.real(omega[:,i]), np.imag(omega[:,i]),label=names[i])
leg = plt.legend(loc='best', ncol=1, shadow=True, fancybox=True, fontsize=13)
# ax.plot(x_axis_plot,np.zeros(npoints),'k')
print('\t ... Saving figure ...')
plt.savefig(subdirectories[1] + figure_fileName + '.' + figure_fileType,bbox_inches='tight',format=figure_fileType,dpi=500)
plt.close()

print("---------------------------------------------")
x_axis_plot = np.linspace(0,x_lim,npoints)
figure_fileName = 'argand_full_scatter'
figure_title = 'Argand Plot'
print('Plotting: ' + figure_title)
fig, ax = plt.subplots(figsize=(7,7))
plt.grid()
# ax.set_title(figure_title,fontsize=12,fontweight='bold')
ax.set_xlabel(r'$Re(\omega)$',fontsize=14)
ax.set_ylabel(r'$Im(\omega)$',rotation=90,fontsize=14)
ax.set_xlim([0, 130])
ax.set_ylim([-20, 30])
ax.set_aspect(1.2)
ax.axhline(y=0, color='k', linestyle='--')
for i in range(0,Nmodes):
	ax.scatter(np.real(omega_scatter[:,i]), np.imag(omega_scatter[:,i]))
# leg = plt.legend(loc='best', ncol=1, shadow=True, fancybox=True, fontsize=13)
# ax.plot(x_axis_plot,np.zeros(npoints),'k')
print('\t ... Saving figure ...')
plt.savefig(subdirectories[1] + figure_fileName + '.' + 'pdf',bbox_inches='tight',format=figure_fileType,dpi=500)
plt.close()

# exit()
#-----------------------------------------------------
print("---------------------------------------------")
x_lim = u_max
x_axis_plot = np.linspace(0,x_lim,npoints)
figure_fileName = 'velocity_imag'
figure_title = 'Velocity Plot'
print('Plotting: ' + figure_title)
fig, ax = plt.subplots(figsize=(7,7))
plt.grid()
# ax.set_title(figure_title,fontsize=12,fontweight='bold')
ax.set_xlabel(r'$u$',fontsize=14)
ax.set_ylabel(r'$Im(\omega)$',rotation=90,fontsize=14)
ax.set_xlim([0, x_lim])
ax.set_ylim([-20, 20])
# ax.plot(x_axis_plot,np.zeros(npoints),'k')
ax.axhline(y=0, color='k', linestyle='--')
for i in range(0,Nmodes):
	ax.plot(u, np.imag(omega[:,i]),label=names[i])
leg = plt.legend(loc='best', ncol=1, shadow=True, fancybox=True, fontsize=13)
print('\t ... Saving figure ...')
plt.savefig(subdirectories[1] + figure_fileName + '.' + figure_fileType,bbox_inches='tight',format=figure_fileType,dpi=500)
plt.close()
#-----------------------------------------------------
print("---------------------------------------------")
x_lim = u_max
x_axis_plot = np.linspace(0,x_lim,npoints)
figure_fileName = 'velocity_real'
figure_title = 'Velocity Plot'
print('Plotting: ' + figure_title)
fig, ax = plt.subplots(figsize=(7,7))
plt.grid()
# ax.set_title(figure_title,fontsize=12,fontweight='bold')
ax.set_xlabel(r'$u$',fontsize=14)
ax.set_ylabel(r'$Re(\omega)$',rotation=90,fontsize=14)
ax.set_xlim([0, x_lim])
ax.set_ylim([-20, 20])
# ax.plot(x_axis_plot,np.zeros(npoints),'k')
ax.axhline(y=0, color='k', linestyle='--')
for i in range(0,Nmodes):
	ax.plot(u, np.real(omega[:,i]),label=names[i])
leg = plt.legend(loc='best', ncol=1, shadow=True, fancybox=True, fontsize=13)
print('\t ... Saving figure ...')
plt.savefig(subdirectories[1] + figure_fileName + '.' + figure_fileType,bbox_inches='tight',format=figure_fileType,dpi=500)
plt.close()

print('-----------------------------------------------------')