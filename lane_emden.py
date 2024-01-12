import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Times New Roman' 
plt.rcParams['mathtext.fontset'] = 'stix' 
plt.rcParams["font.size"] = 25 
plt.rcParams['xtick.direction'] = 'in' 
plt.rcParams['ytick.direction'] = 'in' 
plt.rcParams['axes.grid'] = True
plt.rcParams['grid.color'] = 'gray'
plt.rcParams['grid.alpha'] = 0.7
plt.rcParams['grid.linestyle'] = 'dashed'
plt.rcParams['axes.grid.axis'] = 'both'
plt.rcParams['axes.grid.which'] = 'major'
plt.rcParams['ytick.minor.visible'] = 'True'
plt.rcParams['ytick.left'] = 'True'
plt.rcParams['ytick.right'] = 'True'
plt.rcParams['xtick.minor.visible'] = 'True'
plt.rcParams['xtick.bottom'] = 'True'
plt.rcParams['xtick.top'] = 'True'
plt.rcParams['axes.linewidth'] = 1.0 
plt.rcParams["legend.handlelength"] = 1.0
plt.rcParams["legend.markerscale"] = 1.0
plt.rcParams["legend.fancybox"] = False # 丸角
plt.rcParams["legend.framealpha"] = 1 # 透明度の指定、0で塗りつぶしなし
plt.rcParams["figure.subplot.left"] = 0.14  # 余白
plt.rcParams["figure.subplot.bottom"] = 0.14# 余白
plt.rcParams["figure.subplot.right"] =0.90  # 余白
plt.rcParams["figure.subplot.top"] = 0.91   # 余白
plt.rcParams["figure.subplot.wspace"] = 0.20# 図が複数枚ある時の左右との余白
plt.rcParams["figure.subplot.hspace"] = 0.20# 図が複数枚ある時の上下との余白
plt.rcParams['savefig.dpi'] = 500
plt.rcParams['savefig.bbox'] = 'tight'
plt.rcParams['savefig.pad_inches'] = 0.05

plt.figure(figsize=(10,7))
for j in range(0,7):
    filename = 'lnem_' + str("{:01d}".format(j))
    i, r, v, d = np.loadtxt('../lane_emden/' + filename + '.dat', comments='#', unpack=True)
    plt.plot(r, d, lw=2.0, zorder=1.0, label='$n=$' + str("{:01d}".format(j)))

plt.hlines(y=0.0,xmin=-0.1,xmax=20.1,ls='dashed',colors='gray',lw=1.0,zorder=-0.1)

plt.title("Numerical solution of Lane-Emden equation", fontsize=25)
plt.xlabel("$r/r_0$", fontsize=25)
plt.ylabel("$D$", fontsize=25)

plt.xlim(0.0, 20.0)
plt.ylim(-0.25, 1.0)

plt.legend(loc='upper right', fontsize=25, ncol=2)

plt.savefig('./fig_lnem.png')

plt.show()
plt.close('all')
