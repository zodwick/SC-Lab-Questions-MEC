# Read the given csv file: ‘waveform2.csv’ as an array and plot it. Plot its histogram with an
# appropriate bin size.
# Download the csv file from this link:


# You can save your NumPy arrays to CSV files using the savetxt() function. 
# This function takes a filename and array as arguments and saves the array into CSV format.
# You must also specify the delimiter; this is the character used to separate each variable in the file, 
# most commonly a comma.


# We can load this data later as a NumPy array using the loadtext() function 
# and specify the filename and the same comma delimiter.

import matplotlib.pyplot as plt
import numpy as np
import math 

x = np.arange(0,4,0.01)

y=np.loadtxt("waveform.csv",delimiter=',')

# plt.plot(x,y)

plt.hist(y,bins=30,edgecolor='r')
plt.show()
