#! /usr/bin/env python
#
#  matplotlib:   plotting interactive vs. batch
#  export MPLBACKEND=Agg
#
#  non-interactive backends in mpl:   agg, pdf, pgf, ps, svg, cairo, template

import sys
Qbatch = '--batch' in sys.argv       # cheap CLI parsing solution
print("batch:",Qbatch)

import matplotlib
print("mpl backend",matplotlib.get_backend())

import matplotlib.pyplot as plt
print("interactive:",plt.isinteractive())  # ion/ioff

plt.figure()
plt.plot([0,3,1])
plt.title("single plot")

png = "mpl_simple1.png"
plt.savefig(png)                     # always save a figure?
print(f"Saved {png}")

if not Qbatch:
    plt.show()                       # not needed in batch mode
