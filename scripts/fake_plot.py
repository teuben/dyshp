#! /usr/bin/env python
#
#  here Qbatch either saves png files
#

Qdysh  = True
Qbatch = False
Qmpl   = True

print('Qdysh, Qbatch, Qmpl:',Qdysh, Qbatch, Qmpl)

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
    import matplotlib.pyplot as plt
    plt.figure(11)
    plt.plot([0,3,1])
    if Qbatch:
        png = "fake_plot2.png"
        print(f"Written {png}")        
        plt.savefig(png)
    else:
        plt.show()
    # figure 12 doesn't show till 11 is gone
    plt.figure(12)
    plt.plot([1,2,4,2,1,3])
    if not Qbatch:
        plt.show()


if Qdysh:
    if Qbatch:
        png = "fake_plot_1.png"
        p1.savefig(png)
        print(f"Written {png}")

        png = "fake_plot_2.png"
        p2.savefig(png)
        print(f"Written {png}")
    else:
        # note that just any of the p's needs to be blocked, so p1 or p2 both work
        # how clicking on any of the p's to remove, will kill them all (new behavior)
        # also, sadly, the pure mpl doesn't show until....
        #print("hello")
        p2.show(block=True)



# Not running on IPython and trying to use the ShellGUI may result in unexpected behavior.
