#! /usr/bin/env python
#
#    two dysh plots

from dysh.spectra.spectrum import Spectrum
f = Spectrum.fake_spectrum()
p1 = f.plot()
p2 = f.plot(xaxis_unit="km/s")

p1.show(block=True)   # clicking one graph kills both
