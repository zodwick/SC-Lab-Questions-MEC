# Realize the function y=2+5sin(2πft) for f=1KHz and plot it. Write values of the function as a
# csv file such that the sampling time should be the first value followed by its samples.


import matplotlib.pyplot as plt
import numpy as np
import math 

t=np.arange(0,2*np.pi,0.01)
f=1
y=2+(5*np.sin(2*np.pi*f*t))
plt.plot(t,y)
plt.show()


np.savetxt("wvfrmq5.csv",np.transpose((t,y)),delimiter=",")
