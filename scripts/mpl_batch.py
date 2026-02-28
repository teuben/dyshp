#! /usr/bin/env python
#
#  matplotlib:   plotting interactive vs. batch
#
import sys
Qbatch = '--batch' in sys.argv       # cheap CLI parsing solution
print("batch:",Qbatch)


Qdysh  = True
Qmpl   = True

if Qbatch:
    # specify a backend, like Agg, 
    import matplotlib
    matplotlib.use("Agg")

import matplotlib.pyplot as plt

# figure 1
plt.figure(1)
plt.plot([0,3,1])
if Qbatch:
    png = "mpl_plot1.png"
    print(f"Written {png}")        
    plt.savefig(png)
    
# figure 2 
plt.figure()
plt.plot([1,2,4,2,1,3])


# not saving this figure
if not Qbatch:
    plt.show()


# Not running on IPython and trying to use the ShellGUI may result in unexpected behavior.
