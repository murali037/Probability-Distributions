#%% changing shape parameter with same rate parameter
import numpy as np
import scipy.stats as stats
from matplotlib import pyplot as plt

n = np.linspace (0, 10, 1000)
y1 = stats.gamma.pdf(n, a=1, scale=1)
y2 = stats.gamma.pdf(n, a=2, scale=1)
y3 = stats.gamma.pdf(n, a=3, scale=1)
y4 = stats.gamma.pdf(n, a=4, scale=1)
plt.plot(n, y1, 'r-', n, y2, 'b-', n, y3, 'g-', n, y4, 'y-')
#plt.ylim([0,1])
#plt.xlim([0,10])
plt.show()

#%% keeping scale as constant and varying rate

n = np.linspace (0, 25, 1000)
y1 = stats.gamma.pdf(n, a=3, scale=1)
y2 = stats.gamma.pdf(n, a=3, scale=2)
y3 = stats.gamma.pdf(n, a=3, scale=3)
y4 = stats.gamma.pdf(n, a=3, scale=4)
plt.plot(n, y1, 'r-', n, y2, 'b-', n, y3, 'g-', n, y4, 'y-')

plt.show()