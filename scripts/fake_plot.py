#! /usr/bin/env python
#
#     
#
import sys
Qbatch = '--batch' in sys.argv       # cheap CLI parsing solution
print("batch:",Qbatch)

Qdysh  = True
Qmpl   = True

print('Qbatch, Qdysh, Qmpl:',Qbatch, Qdysh, Qmpl)

if Qbatch and Qmpl:
    import matplotlib
    matplotlib.use("Agg")

if Qdysh:
    from dysh.spectra.spectrum import Spectrum
    f = Spectrum.fake_spectrum()

    # bring up two plots from dysh
    p1 = f.plot()
    p2 = f.plot(xaxis_unit="km/s")

if Qmpl:
    # bring up 2 plots from matplotlib
    import matplotlib.pyplot as plt
    # figure 3
    plt.figure(3)
    plt.plot([0,3,1])
    if Qbatch:
        png = "fake_plot3.png"
        print(f"Written {png}")        
        plt.savefig(png)
    # figure 4
    plt.figure(4)
    plt.plot([1,2,4,2,1,3])


if Qdysh:
    if Qbatch:
        png = "fake_plot1.png"
        p1.savefig(png)
        print(f"Written {png}")

        png = "fake_plot2.png"
        p2.savefig(png)
        print(f"Written {png}")
    else:
        # note that just any of the p's needs to be blocked, so p1 or p2 both work
        # how clicking on any of the p's to remove, will kill them all (new behavior)
        # also, sadly, the pure mpl doesn't show until....
        #print("hello")
        p2.show(block=True)


if not Qbatch:
    plt.show()
        


# Not running on IPython and trying to use the ShellGUI may result in unexpected behavior.
