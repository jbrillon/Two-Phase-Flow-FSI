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
modes = range(1,Nmodes+1)
names = [None]*Nmodes
for l in range(0,Nmodes):
    names[l] = "Mode %i" % modes[l]

subdirectories[0] += 'beta1P_030/'
#-----------------------------------------------------
# Common
#-----------------------------------------------------
xlimits = [-1,65]
ylimits = [-5,26]
#-----------------------------------------------------
# Common
#-----------------------------------------------------
u_mkr_values = [2.0,4.0,8.0,12.0]
u_mkr_values = np.array(u_mkr_values)
u_mkr_values = list(u_mkr_values)
#-----------------------------------------------------
# Load paidoussis data
#-----------------------------------------------------
subsubdir = 'Paidoussis_1phase/'
data_fileType_pd = 'csv'
data_fileName = 'Paidoussis_1st_mode'
pd_mode1 = np.genfromtxt(subdirectories[0]+subsubdir+data_fileName+'.'+data_fileType_pd, unpack=True,delimiter=',')
data_fileName = 'Paidoussis_2nd_mode'
pd_mode2 = np.genfromtxt(subdirectories[0]+subsubdir+data_fileName+'.'+data_fileType_pd, unpack=True,delimiter=',')
data_fileName = 'Paidoussis_3rd_mode'
pd_mode3 = np.genfromtxt(subdirectories[0]+subsubdir+data_fileName+'.'+data_fileType_pd, unpack=True,delimiter=',')
data_fileName = 'Paidoussis_4th_mode'
pd_mode4 = np.genfromtxt(subdirectories[0]+subsubdir+data_fileName+'.'+data_fileType_pd, unpack=True,delimiter=',')
#-----------------------------------------------------
print("---------------------------------------------")

figure_fileName = 'argand_pd_comparison'
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

ax.plot(pd_mode1[0,:],pd_mode1[1,:],color='k',marker='o', markersize=6, mfc='None', linestyle='None')
ax.plot(pd_mode2[0,:],pd_mode2[1,:],color='k',marker='o', markersize=6, mfc='None', linestyle='None')
ax.plot(pd_mode3[0,:],pd_mode3[1,:],color='k',marker='o', markersize=6, mfc='None', linestyle='None')
ax.plot(pd_mode4[0,:],pd_mode4[1,:],color='k',marker='o', markersize=6, mfc='None', linestyle='None')

#-----------------------------------------------------
# Load data -- eps = 0.00
#-----------------------------------------------------
subsubdir = 'eps000/'
data_fileName = 'u_store'
u = np.loadtxt(subdirectories[0]+subsubdir+data_fileName+'.'+data_fileType, unpack=False)
# load complex
data_fileName = 'real_w_store'
real_omega = np.loadtxt(subdirectories[0]+subsubdir+data_fileName+'.'+data_fileType, unpack=False)
data_fileName = 'imag_w_store'
imag_omega = np.loadtxt(subdirectories[0]+subsubdir+data_fileName+'.'+data_fileType, unpack=False)
omega = real_omega + (1.0j)*imag_omega

# - - - - - - - - - - - - - - - - - - - - - - - - - - - 
#               Annotate velocities
# - - - - - - - - - - - - - - - - - - - - - - - - - - - 
data_fileName = 'u_crit'
u_crit = np.loadtxt(subdirectories[0]+subsubdir+data_fileName+'.'+data_fileType, unpack=False)
u_crit[u_crit==-1.0]=0.0
u_crit_flag = np.zeros((4,5),dtype='int64')
u_crit_flag[np.nonzero(u_crit)] = 1
u_crit = u_crit[np.nonzero(u_crit)]

u_mkrs = list(u_mkr_values)
u_mkrs.extend(list(u_crit))
u_mkrs.sort()
u_crit_index = np.argmin(abs(u_crit-u_mkrs))

u_mkrs_index = []
for i,u_val in enumerate(u_mkrs):
    index = np.argmin(abs(np.float64(u_val)-u))
    u_mkrs_index.append(index)

u_mkrs_xy = np.zeros((len(u_mkrs_index),2,4),dtype='float64')
for i in range(0,4):
    u_mkrs_xy[:,0,i] = np.real(omega[u_mkrs_index,i])
    u_mkrs_xy[:,1,i] = np.imag(omega[u_mkrs_index,i])

u_mkrs = np.array(u_mkrs,dtype='float64')

xshifts = 1.05*np.ones((np.size(u_mkrs),4),dtype='float64')
yshifts = 1.03*np.ones((np.size(u_mkrs),4),dtype='float64')

plot_flag = 1
for i in range(0,4):
    for k,u_val in enumerate(u_mkrs):
        if(k==u_crit_index):
            if(u_crit_flag[i,0]!=0):
                plot_flag = 1
            else:
                plot_flag = 0
        else:
            plot_flag = 1

        if(plot_flag != 0):
            xloc = xshifts[k,i]*u_mkrs_xy[k,0,i]
            yloc = yshifts[k,i]*u_mkrs_xy[k,1,i]
            if(((xloc>xlimits[0]) and (xloc<xlimits[1])) and ((yloc>ylimits[0]) and (yloc<ylimits[1]))):
                ax.plot(u_mkrs_xy[k,0,i],u_mkrs_xy[k,1,i],color='k',marker='o',markersize=4, mfc='k', linestyle='None')
                vel_name = '%.1f' % u_val
                t = ax.text(xloc, yloc, vel_name, fontsize=9, fontweight='bold',color='k')
                t.set_bbox(dict(boxstyle='square,pad=0',facecolor='white', alpha=0.7 , edgecolor='none'))
# - - - - - - - - - - - - - - - - - - - - - - - - - - - 

for i in range(0,4):
    ax.plot(np.real(omega[:,i]), np.imag(omega[:,i]),color='k')

#-----------------------------------------------------
# Load data -- eps = 0.01
#-----------------------------------------------------
subsubdir = 'eps001/'
data_fileName = 'u_store'
u = np.loadtxt(subdirectories[0]+subsubdir+data_fileName+'.'+data_fileType, unpack=False)
# load complex
data_fileName = 'real_w_store'
real_omega = np.loadtxt(subdirectories[0]+subsubdir+data_fileName+'.'+data_fileType, unpack=False)
data_fileName = 'imag_w_store'
imag_omega = np.loadtxt(subdirectories[0]+subsubdir+data_fileName+'.'+data_fileType, unpack=False)
omega = real_omega + (1.0j)*imag_omega
data_fileName = 'u_crit'
u_crit = np.loadtxt(subdirectories[0]+subsubdir+data_fileName+'.'+data_fileType, unpack=False)
u_crit[u_crit==-1.0]=0.0
u_crit = u_crit[np.nonzero(u_crit)]

for i in range(0,4):
    ax.plot(np.real(omega[:,i]), np.imag(omega[:,i]),color='b',linestyle='--')

#-----------------------------------------------------
# Load data -- eps = 0.4
#-----------------------------------------------------
subsubdir = 'eps040/'
data_fileName = 'u_store'
u = np.loadtxt(subdirectories[0]+subsubdir+data_fileName+'.'+data_fileType, unpack=False)
# load complex
data_fileName = 'real_w_store'
real_omega = np.loadtxt(subdirectories[0]+subsubdir+data_fileName+'.'+data_fileType, unpack=False)
data_fileName = 'imag_w_store'
imag_omega = np.loadtxt(subdirectories[0]+subsubdir+data_fileName+'.'+data_fileType, unpack=False)
omega = real_omega + (1.0j)*imag_omega

# - - - - - - - - - - - - - - - - - - - - - - - - - - - 
#               Annotate velocities -- more than 1 crit velocity
# - - - - - - - - - - - - - - - - - - - - - - - - - - - 
data_fileName = 'u_crit'
u_crit = np.loadtxt(subdirectories[0]+subsubdir+data_fileName+'.'+data_fileType, unpack=False)
u_crit[u_crit==-1.0]=0.0
u_crit_store = 1.0*u_crit
u_crit_flag = np.zeros((4,5),dtype='int64')
u_crit_flag[np.nonzero(u_crit)] = 1
u_crit = u_crit[np.nonzero(u_crit)]

u_mkrs = list(u_mkr_values)
u_mkrs.extend(list(u_crit))
u_mkrs.sort()

u_crit_index = []
for i,u_cr in enumerate(u_crit):
    u_crit_index.append(np.argmin(abs(u_cr-u_mkrs)))

u_mkrs_index = []
for i,u_val in enumerate(u_mkrs):
    index = np.argmin(abs(np.float64(u_val)-u))
    u_mkrs_index.append(index)

u_mkrs_xy = np.zeros((len(u_mkrs_index),2,4),dtype='float64')
for i in range(0,4):
    u_mkrs_xy[:,0,i] = np.real(omega[u_mkrs_index,i])
    u_mkrs_xy[:,1,i] = np.imag(omega[u_mkrs_index,i])

u_mkrs = np.array(u_mkrs,dtype='float64')

xshifts = 1.05*np.ones((np.size(u_mkrs),4),dtype='float64')
yshifts = 1.03*np.ones((np.size(u_mkrs),4),dtype='float64')

plot_flag = 1
for i in range(0,4):
    for k,u_val in enumerate(u_mkrs):
        if(k in u_crit_index):
            if(u_val in u_crit_store[i,:]):
                plot_flag = 1
            else:
                plot_flag = 0
        else:
            plot_flag = 1

        if(plot_flag != 0):
            xloc = xshifts[k,i]*u_mkrs_xy[k,0,i]
            yloc = yshifts[k,i]*u_mkrs_xy[k,1,i]
            if(((xloc>xlimits[0]) and (xloc<xlimits[1])) and ((yloc>ylimits[0]) and (yloc<ylimits[1]))):
                ax.plot(u_mkrs_xy[k,0,i],u_mkrs_xy[k,1,i],color='r',marker='o',markersize=4, mfc='r', linestyle='None')
                vel_name = '%.1f' % u_val
                t = ax.text(xloc, yloc, vel_name, fontsize=9, fontweight='bold',color='r')
                t.set_bbox(dict(boxstyle='square,pad=0',facecolor='white', alpha=0.7 , edgecolor='none'))
# - - - - - - - - - - - - - - - - - - - - - - - - - - - 

for i in range(0,4):
    ax.plot(np.real(omega[:,i]), np.imag(omega[:,i]),color='r',linestyle='-.')


legend_elements = [Line2D([0],[0], color='k', marker='o', markersize=6, mfc='None', linestyle='None',label=r'Paidoussis and Issid (1974)'),
                            Line2D([0],[0], color='k', label=r'Liquid only $(\epsilon=0)$'),
                             Line2D([0],[0], color='b', linestyle='--', label=r'Two-phase $(\epsilon=0.01)$'),
                              Line2D([0],[0], color='r', linestyle='-.', label=r'Two-phase $(\epsilon=0.4)$')]
leg = plt.legend(handles=legend_elements, loc='best', ncol=1, shadow=True, fancybox=True, fontsize=13)
plt.tight_layout()

print('\t ... Saving figure ...')
plt.savefig(subdirectories[1] + figure_fileName + '.' + figure_fileType,bbox_inches='tight',format=figure_fileType,dpi=500)
plt.close()

print('-----------------------------------------------------')