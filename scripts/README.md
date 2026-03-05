# 1. Python scripts trying mpl and dysh type plotting

mpl_simple1.py  shows one plot, will also save as png.  Uses optional --batch.
mpl_simple2.py  shows two plots at the same time, so you can interact with both
mpl_batch.py    show how to plot or create plotfile using --batch

dysh_plot1.py   shows one plot, --batch also available. always writes png
dysh_plot2.py   shows two plots, just to show it can interact with both.

fake_plot.py    show both 2 dysh plots and 2 mpl plots.  --batch optional

In the  mpl approach, ctrl-W closes one window at the time, or click on the 'X' to close window

in the current dysh approach, ctrl-W doesnt work. clicking 'X" works, but killing one, will kill them all.
Also, there is a message
     Not running on IPython and trying to use the ShellGUI may result in unexpected behavior.
