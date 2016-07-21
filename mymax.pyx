cimport cython

from mymax_wrapper cimport *  # (import functions exposed in mymax_wrapper.pxd)

# alternatively, we could have used `cimport mymax_wrapper`, then
# called the functions as mymax_wrapper.cmax and mymax_wrapper.chello

def pymax(float a, float b):
    print("print from python function wrapping a c function")
    return cmax(a, b)


def pyhello():
    chello()
