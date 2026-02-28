#! /usr/bin/env python
#
#  matplotlib:   plotting interactive vs. batch
#  export MPLBACKEND=Agg


import matplotlib
print("mpl backend: ",matplotlib.get_backend())

# supposed to set MPLBACKEND=Agg
import matplotlib.pyplot as plt


fig, ax = plt.subplots(num=1)
ax.plot([0,3,1])
ax.set_title("Plot #1/2")
#plt.show()     # this would block fig 2
    
fig, ax = plt.subplots(num=2)
ax.plot([1,2,4,2,1,3])
ax.set_title("Plot #2/2")

# wait for all
plt.show()
