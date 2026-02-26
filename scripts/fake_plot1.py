#! /usr/bin/env python
#
#    one simple dysh plot in batch mode

import sys
Qbatch = '--batch' in sys.argv       # cheap CLI parsing solution
print("batch:",Qbatch)

from dysh.spectra.spectrum import Spectrum
f = Spectrum.fake_spectrum()
p = f.plot()

png = 'fake_plot1.png'
p.savefig(png)
print(f"Wrote {png}")

if not Qbatch:
    p.show(block=True)   # oddly, False is the default
