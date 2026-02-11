#  DYSHP:  peter's frontend for installing and loading dysh

This is how I install my developer environment for dysh.

By default, a new fresh anacona3 will be installed here.  `version=` is optional.
Here you can only pick between three installs:


1. `install1`:  install using `uv`, but use the `.venv` , not `uv run`
2. `install2`:  install using `pip`
3. `install3`:  install using `pip`, but dysh in dysh/venv


## Issues

1.  spyder doesn't know dysh, even if you use uv run - side effect of a venv ?
2.  install2 doesn't do plotting in spyder or notebook, is ok in dysh CLI
3.  the `uv tool install dysh[all]` will muck with your ~/.local/bin and populate
4.  in spyder need `%gui tk` to make it plot

## Notes

Install notes in dysh/README.md and
https://dysh.readthedocs.io/en/latest/for_developers/install.html


For those using bash, this bash completion tool might be useful:
```
    echo 'eval "$(uv generate-shell-completion bash)"' >> ~/.bashrc
```


## Installing uv

Following https://docs.astral.sh/uv/getting-started/installation/
use either one of:

```
   curl -LsSf https://astral.sh/uv/install.sh | sh
   wget -qO- https://astral.sh/uv/install.sh | sh
   pipx install uv
   pip install uv
```

