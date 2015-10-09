# IPython-extensions: more magic(s) for IPython

This package consists of various IPython extensions (mostly new %magics). It exists mainly to make installation of these extension easier: you only need to install and update one package to get multiple extensions. Also, the up-to-now used `%install_ext` magic is [deprecated and will be removed in a future version](https://github.com/ipython/ipython/pull/8763), so the only way to distribute extensions is via python packages.

Currently the following magic commands are included: 

* `%%writeandexecute`: write the content of a cell to a python file and then execute the cell -> male code reuse possible
* `%%inactive`: mark the current cell as (temporary) inactive, i.e. do not execute it

## Installing

**Installing via pip:**

```bash
pip install IPython-extensions
```

**Installing from git:**

```bash
git clone https://github.com/ipython-contrib/IPython-extensions.git
cd IPython-extensions
python setup.py install
```

## Running magics

The extensions are currently all available in the `ipyext` namespace. To make a magic command available in your IPython session, use `%load_ext ipyext.<extension_name>`:

```python
%load_ext ipyext.writeandexecute
```

## Contributing

You have an IPython extension (e.g. a `%magic` command) but it's too small to build your own package? You are welcome to contribute it to this repository!

To prevent bit rot, it should follow the guidelines outlined in [CONTRIBUTING.md](https://github.com/ipython-contrib/IPython-extensions/blob/master/CONTRIBUTING.md), meaning:

* it should be IPython centric (notebook centric extensions belong to the [jupyter notebook extension repo](https://github.com/ipython-contrib/IPython-notebook-extensions))
* it should have proper documentation (preferable in [numpydoc style](https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt))
* it should have a few tests of the functionality (see examples in this repository or in [IPython](https://github.com/ipython/ipython/blob/master/IPython/core/tests/test_magic.py)

[![Build Status](https://travis-ci.org/ipython-contrib/IPython-extensions.svg?branch=master)](https://travis-ci.org/ipython-contrib/IPython-extensions)
