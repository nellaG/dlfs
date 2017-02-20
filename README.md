# dlfs
The studying documentation of Deep Learning from Scratch.

```
# installation

$ virtualfish new -p python3.5 {your_venv_name}

# (install fish shell: https://fishshell.com/)
```

## troubleshooting on mac os x
```
# resolves this error:
/Users/{censored}/.virtualenvs/dlfs/lib/python3.5/site-packages/matplotlib/font_manager.py:280: UserWarning: Matplotlib is building the font cache using fc-list. This may take a moment.
  'Matplotlib is building the font cache using fc-list. '
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/{censored}/.virtualenvs/dlfs/lib/python3.5/site-packages/matplotlib/pyplot.py", line 115, in <module>
    _backend_mod, new_figure_manager, draw_if_interactive, _show = pylab_setup()
  File "/Users/{censored}/.virtualenvs/dlfs/lib/python3.5/site-packages/matplotlib/backends/__init__.py", line 32, in pylab_setup
    globals(),locals(),[backend_name],0)
  File "/Users/{censored}/.virtualenvs/dlfs/lib/python3.5/site-packages/matplotlib/backends/backend_macosx.py", line 19, in <module>
    from matplotlib.backends import _macosx
RuntimeError: Python is not installed as a framework. The Mac OS X backend will not be able to function correctly if Python is not installed as a framework. See the Python documentation for more information on installing Python as a framework on Mac OS X. Please either reinstall Python as a framework, or try one of the other backends. If you are using (Ana)Conda please install python.app and replace the use of 'python' with 'pythonw'. See 'Working with Matplotlib on OSX' in the Matplotlib FAQ for more information.

$ echo "backend: TKAgg" > $HOME/.matplotlib/matplotlibrc
```

## using flake8
```
$ flake8 --ignore=E111 chapter_1/chapter1.py  # --ignore is optional.
```