cimport cython

cdef extern from "mymax.h":
    float cmax(float, float)
    int chello()
