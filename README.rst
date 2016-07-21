simple-cython-example
---------------------

Basic example of how to wrap a C function with cython.

To install this python module, use::

    git clone https://github.com/PiRK/simple-cython-example.git
    cd simple-cython-example
    pip install . --user
    
Then, in a python interactive shell::

    >>> import mymax
    >>> dir(mymax)
    ['__builtins__', '__doc__', '__file__', '__name__', '__package__', '__test__', 'pyhello', 'pymax']
    >>> mymax.pymax(12, 15.1)
    print from python function wrapping a c function
    print from c function
    >>> mymax.pyhello()
    Hello World
    3.141593 2.718282
    print from c function
    max of e and pi is approximately 3.141593

This example includes 2 .c files, 1 .h file, 1 .pyx file, 1 .pxd file and a `setup.py` file.

The `.pyx` contains the cython function definition.

The `.pxd` file wraps the .c functions (through their declaration in the .h file).

The `setup.py` file is a standard way of building and installing python libraries
(read https://docs.python.org/3/distutils/setupscript.html or
http://python-packaging.readthedocs.io/en/latest/minimal.htmlfor more information on this).
The less standard part of this file is the `from Cython.Distutils import build_ext` import.
This replaces the standard *setuptools* or *distutils* `build_ext` command with a version
that can handle conversion of cython code into standard C code that uses the `Python.h"
library and that can be compiled by `setuptools`.
