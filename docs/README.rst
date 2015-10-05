IPython Documentation
---------------------

This directory contains the documentation for IPython-extensions. 


Requirements
------------
The following tools are needed to build the documentation:

sphinx numpydoc 

The documentation gets built using ``make``, and comes in several flavors.

``make html`` - build the API (both Javascript and Python) and narrative 
documentation web pages, this is the the default ``make`` target, so 
running just ``make`` is equivalent to ``make html``. 

``make pdf`` will compile a pdf from the documentation.

You can run ``make help`` to see information on all possible make targets.



