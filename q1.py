# Implement the function given below and plot its two cycles. Plot its histogram also.
# f(t) = cost cos5t + cos5t

import matplotlib.pyplot as plt
import numpy as np

# two cycles means 0 to 4pi

t=np.arange(0,4*np.pi,0.01)
y=(np.cos(t)*np.cos(5*t))+np.cos(5*t)



# fig , axis =plt.subplot(1,1)
figure, axis = plt.subplots(1,2)
axis[0].plot(t,y)
axis[0].set_title("line graph")
axis[1].hist(y)
axis[1].set_title("histogram")
plt.show()