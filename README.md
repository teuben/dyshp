#  DYSHP:  peter's frontend for installing and loading dysh

This is how I install my developer environment for dysh.

By default, a new fresh anacona3 will be installed here.  `version=` is optional,
but as of the plotting overhaul early 2026, only python 3.13 and up seem to be
working for me.

Here you can only pick between a few installs:


1. `install1`:  install using `uv`, source the `dysh/.venv` , no need to use `uv run`
2. `install2`:  install using `pip`
3. `install3`:  install using `pip`, but dysh in `dysh/venv`
4. `install4`:  install using `pip` as user install. no source code.


## Issues

1.  spyder doesn't know dysh, even if you use uv run - side effect of a venv ?
2.  install2 doesn't do plotting in spyder or notebook, is ok in dysh CLI
3.  the `uv tool install dysh[all]` will muck with your ~/.local/bin and populate - don't use it for development
4.  in spyder need `%gui tk` to make it plot, or make sure tkinter is your graphics output
    (and the new in_notebook())

## Notes

Install notes in dysh/README.md and
https://dysh.readthedocs.io/en/latest/for_developers/install.html


## Installing uv

Following https://docs.astral.sh/uv/getting-started/installation/
use either one of:

```
   curl -LsSf https://astral.sh/uv/install.sh | sh
   wget -qO- https://astral.sh/uv/install.sh | sh
   pipx install uv
   pip install uv
```

For those using bash, this bash completion tool might be useful for uv:
```
    echo 'eval "$(uv generate-shell-completion bash)"' >> ~/.bashrc
```



## testing

Some testing command for graphics. See also `test_dysh.ipynb`

```

import dysh

import sys
sys.path.append('/home/teuben/GBT/dyshp/dysh/.venv/lib/python3.12/site-packages')
sys.path.append('/home/teuben/GBT/dyshp/dysh/src')

import matplotlib
matplotlib.get_backend()

%gui tk


from dysh.spectra.spectrum import Spectrum
sp = Spectrum.fake_spectrum()
sp.plot()
```

### Graphics

As of version 0.12.x **spyder** settings may need to be adjusted 

```
   spyder -> Preferences -> IPython console -> Graphics
   -> tkinter
```

whereas for `inline` you would need `%gui tk` to make the dysh graphics appear.

