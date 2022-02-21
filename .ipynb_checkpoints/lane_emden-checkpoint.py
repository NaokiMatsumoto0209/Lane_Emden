import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,7))
for j in range(0,5):
    filename = 'lnem_' + str("{:01d}".format(j))
    i, r, v, d = np.loadtxt('../lane_emden/' + filename + '.dat', comments='#', unpack=True)
    plt.plot(r, d, label='$n=$' + str("{:01d}".format(j)))

"""
filename = 'lnem_1.5'
i, r, v, d = np.loadtxt('../lane_emden/' + filename + '.dat', comments='#', unpack=True)
plt.plot(r, d, label='$n=1.5$')
"""

plt.title("Numerical solution of Lane-Emden equation");
plt.xlabel("$r/r_0$")
plt.ylabel("$D$")

plt.xlim(0.0, 20.0)
plt.ylim(0.0, 1.0)

plt.grid()

plt.legend()

plt.show()

fig.savefig('fig_lnem.png')
