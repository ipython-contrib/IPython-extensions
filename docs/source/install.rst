IPython-extensions requires Python 2.7 or 3.3+.

.. seealso::

   `Installing IPython <http://ipython.readthedocs.org/en/latest/install/index.html>`__
     How to install IPython
   
   `Installing the Jupyter notebook <http://jupyter.readthedocs.org/en/latest/install.html>`__
     The Notebook, nbconvert, and many other former pieces of IPython are now
     part of Project Jupyter.


Installation
============

     
Quickstart
----------

If you have :mod:`pip`,
the quickest way to get up and running with IPython is:

.. code-block:: bash

    $ pip install ipyext


Installing the development version
----------------------------------

It is also possible to install the development version of 
IPython-extensions from our `Git <http://git-scm.com/>`_ source code 
repository. To do this you will need to have Git installed on your 
system. Then do: 

.. code-block:: bash

    $ git clone https://github.com/ipython-contrib/IPython-extensions.git
    $ cd IPython-extensions
    $ python setup.py install

Some users want to be able to follow the development branch as it changes.  If
you have :mod:`pip`, you can replace the last step by:

.. code-block:: bash

    $ pip install -e .

This creates links in the right places and installs the command line script to
the appropriate places. 

Then, if you want to update your IPython at any time, do:

.. code-block:: bash

    $ git pull

.. _dependencies:

Dependencies
------------

IPython-extensions relies on a number of other Python packages. 
Installing using a package manager like pip or conda will ensure the 
necessary packages are installed. If you install manually, it's up to 
you to make sure dependencies are installed. They're not listed here, 
because they may change from release to release, so a static list will 
inevitably get out of date. 

