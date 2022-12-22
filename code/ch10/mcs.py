import math

import numpy as np
from pylab import mpl, plt
plt.style.use('seaborn')
mpl.rcParams['font.family'] = 'serif'

M = 100 # number of time points
I = 20 # number of simulation paths

S0 = 36.
T = 1.0
r = 0.06
sigma = 0.2

def mcs_simulation_py(p):
    M, I = p
    dt = T / M
    S = np.zeros((M + 1, I))
    S[0] = S0
    rn = np.random.standard_normal(S.shape)
    for t in range(1, M + 1):
        for i in range(I):
            S[t, i] = S[t-1, i] * math.exp((r - sigma ** 2 / 2) * dt +
                                         sigma * math.sqrt(dt) * rn[t, i])
    return S

S = mcs_simulation_py((M, I))

ST_simulation = S[-1].mean()
print(ST_simulation)

ST_true_value = S0 * math.exp(r * T)
print(ST_true_value)

K = 40.

C0 = math.exp(-r * T) * np.maximum(K - S[-1], 0).mean()
print(C0)

# A histogram is a graphical representation of the distribution of data given by the user.
# The towers or bars of a histogram are called bins.
# The height of each bin shows how many values from that data fall into that range.
plt.figure(figsize=(10, 6))
plt.hist(S[-1], bins=35, label='frequency')
plt.axvline(S[-1].mean(), color='r', label='mean value')
plt.legend(loc=0)
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(S)
plt.xlabel('t')
plt.ylabel('S')
plt.legend(loc=0)
plt.show()