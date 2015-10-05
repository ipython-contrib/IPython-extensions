# encoding: utf-8

# Copyright (C) 2013  The IPython Development Team
# Copyright (c) IPython-extensions Development Team. 
# Distributed under the terms of the Modified BSD License. 

from IPython.core.magic import (Magics, magics_class, cell_magic)
from IPython.testing.skipdoctest import skip_doctest
from IPython.core.error import UsageError

@magics_class
class InactiveMagics(Magics):
    """Magic to *not* execute a cell.
    
    Useful for temporary deactivating a cell.    
    """

    @skip_doctest
    @cell_magic
    def inactive(self, parameter_s='', cell=None):
        """Magic to *not* execute a cell.
        
        This magic can be used to mark a cell (temporary) as inactive.
        
        Examples:
        ---------
        ::
        
            In [1]: %load_ext ipyext.inactive
            'inactive' magic loaded.

            In [2]: %%inactive
               ...: print("code not run...")
               ...:
            Cell inactive: not executed!
        """
        if cell is None:
            raise UsageError('empty cell, nothing to ignore :-)')
        print("Cell inactive: not executed!")
        

            
def load_ipython_extension(ip):
    ip.register_magics(InactiveMagics)
    print ("'inactive' magic loaded.")