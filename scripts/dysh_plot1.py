#! /usr/bin/env python
#
#    one simple dysh plot, switching between interactive and batch mode

import sys
Qbatch = '--batch' in sys.argv       # cheap CLI parsing solution
print("batch:",Qbatch)

# make a plot
from dysh.spectra.spectrum import Spectrum
f = Spectrum.fake_spectrum()
p = f.plot()

# save the plot regardless of mode
png = 'fake_plot1.png'
p.savefig(png)
print(f"Wrote {png}")

# running as script, blocking is needed to show the figure on screen
if not Qbatch:
    p.show(block=True)   # oddly, False is the default
