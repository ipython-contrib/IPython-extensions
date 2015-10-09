## Contributing new extensions

A contributed magic should be IPython centric, meaning that the 
extension should need python parts and not only display some 
javascript/html. Such notebook centric extensions are better contributed 
in the [jupyter-notebook-extensions repo](https://github.com/ipython-contrib/IPython-notebook-extensions).

A contributed magic should also have:

* A numpydoc docstring, which describes all options and gives an example. For 
  examples, see the current magics or the ones 
  [in IPython](https://github.com/ipython/ipython/blob/master/IPython/core/magics/basic.py)). 
  The docs are build by changing into the docs subdir and running `make html`. 
  You need to install `numpydoc` and `sphinx` to build the docs.
* Tests (see ipyext.tests for examples). Running the testsuite can be done by 
  changing to the checked out dir and run `python test.py`.


## Opening an Issue

When opening a new Issue, please take the following steps:

1. Search GitHub and/or Google for your issue to avoid duplicate reports.
   Keyword searches for your error messages are most helpful.
2. If possible, try updating to master and reproducing your issue,
   because we may have already fixed it.
3. Try to include a minimal reproducible test case
4. Include relevant system information.  Start with the output of:

        python -c "import IPython; print(IPython.sys_info()); import ipyext; print(ipyext.__version__)"


## Pull Requests

Some guidelines on contributing to IPython:

* All work is submitted via Pull Requests.
* Pull Requests can be submitted as soon as there is code worth discussing.
  Pull Requests track the branch, so you can continue to work after the PR is submitted.
  Review and discussion can begin well before the work is complete,
  and the more discussion the better.
  The worst case is that the PR is closed.
* Pull Requests should generally be made against master
* Pull Requests should be tested, if feasible:
    - bugfixes should include regression tests
    - new behavior should at least get minimal exercise
* New features and backwards-incompatible changes should be documented by adding
  a entry in docs/whatnew/.
* Don't make 'cleanup' pull requests just to change code style.
  We don't follow any style guide strictly, and we consider formatting changes
  unnecessary noise.
  If you're making functional changes, you can clean up the specific pieces of
  code you're working on.

[Travis](http://travis-ci.org/#!/ipython-contrib/ipython-extensions) does a pretty good 
job testing IPython-extensions and Pull Requests, but it may make sense to manually 
perform tests.

For more detailed information, see our [GitHub Workflow](https://github.com/ipython/ipython/wiki/Dev:-GitHub-workflow).

