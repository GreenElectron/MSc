import numpy as np
import math
from matplotlib import rc, use, get_backend
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
_2016_07_14_21_23_15_8311 = np.genfromtxt('./2016_07_14_21_23_15_8311/results/density_ns4_n2_l1.00.dat')    #   exact
_2016_07_15_16_21_24_1201 = np.genfromtxt('./2016_07_15_16_21_24_1201/results/density_ns4_n2_l1.00.dat')    #   gkba+soa
_2016_07_15_16_21_55_1201 = np.genfromtxt('./2016_07_15_16_21_55_1201/results/density_ns4_n2_l1.00.dat')    #   gkba+tpp
rc('font', family='serif')
rc('font', serif = 'cmr10')
rc('font', size=12)
rc('text', usetex=True)
fig, ax = plt.subplots()
size = fig.get_size_inches()
fig.set_size_inches((0.7*size[0],0.6*size[1]))
plt.subplots_adjust(left=0.13,right=0.97,top=0.92,bottom=0.15)
ax.set_xlabel(r'time $t$')
ax.set_ylabel(r'density on site 1')
ax.plot(_2016_07_14_21_23_15_8311[:,0],_2016_07_14_21_23_15_8311[:,1],color='DarkRed',dashes=(None,None),marker='',markersize=2.0,markeredgecolor= 'r',markerfacecolor= 'r',markevery=(0,30),label=r'$\mathrm{Exact}$')
ax.plot(_2016_07_15_16_21_24_1201[:,0],_2016_07_15_16_21_24_1201[:,1],color='r',dashes=(None,None),marker='',markersize=2.0,markeredgecolor= 'DarkOrange',markerfacecolor= 'DarkOrange',markevery=(0,30),label=r'$\mathrm{GKBA+SOA}$')
ax.plot(_2016_07_15_16_21_55_1201[:,0],_2016_07_15_16_21_55_1201[:,1],color='DarkOrange',dashes=(None,None),marker='',markersize=2.0,markeredgecolor= 'DarkRed',markerfacecolor= 'DarkRed',markevery=(0,30),label=r'$\mathrm{GKBA+TPP}$')
#depends_project:2016_07_14_21_23_15_8311
#depends_project:2016_07_15_16_21_24_1201
#depends_project:2016_07_15_16_21_55_1201
ax.set_xlim(0,50)
ax.grid(color='grey')
ax.legend(fancybox=True,loc='best',ncol=1,fontsize=8,numpoints=1)
#user: green
plt.savefig('tr_methods_damping_gkba.pdf')