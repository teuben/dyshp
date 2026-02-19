#! /usr/bin/env python
#

import matplotlib.pyplot as plt

from dysh.spectra.spectrum import Spectrum
f = Spectrum.fake_spectrum()
p = f.plot()

png = "fake_plot.png"
p.savefig(png)
print(f"Written {png}")

# plt.show()
# Not running on IPython and trying to use the ShellGUI may result in unexpected behavior.
