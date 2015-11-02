from setuptools import setup, find_packages
import os
pjoin = os.path.join
repo_root = os.path.dirname(os.path.abspath(__file__))

try:
    execfile
except NameError:
    def execfile(fname, globs, locs=None):
        locs = locs or globs
        exec(compile(open(fname).read(), fname, "exec"), globs, locs)


try:
    # make this optional, but it's better for PyPI uploads
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
    long_description = long_description.replace("\r","")
except:
    print("!!! DON'T UPLOAD TO PyPI, DESCRIPTION IS WRONG FORMAT")
    import io
    with io.open('README.md', encoding="utf-8") as f:
        long_description = f.read()

# _version.py contains __version__.
execfile(pjoin(repo_root, 'ipyext','_version.py'), globals())
        
        
setup(
    name='ipyext',
    version=__version__,
    license='BSD',
    description='IPython-extensions: more magic(s) for IPython',
    long_description=long_description,
    author='IPython-extensions Development Team',
    author_email='jupyter@googlegroups.org',
    url='https://github.com/ipython-contrib/IPython-extensions',
    packages = find_packages(exclude=['*test*']),
    install_requires=['ipython']
)
