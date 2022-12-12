# Implement the functions given below and plot two cycles of them. Plot scatter plot to
# study their relationship.
# f1(t) = sint
# f2(t) = cost

import matplotlib.pyplot as plt
import numpy as np

t=np.arange(0,4*np.pi,0.5)
f1=np.sin(t)
f2=np.cos(t)

plt.scatter(t,f1,c='b')
plt.scatter(t,f2,c='r')
plt.legend(["sin t","cos t"], loc="best")

plt.show()