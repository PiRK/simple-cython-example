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


    
