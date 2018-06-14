# distutils: language=c++
# distutils: sources = c_stack.cpp

from cpython.ref cimport PyObject

cdef extern from 'c_stack.h':
    cdef cppclass C_Stack:
        PyObject* peek();

        void push(object val);

        PyObject* pop();

class StackEmpty(Exception):
    pass

cdef class Stack:
    cdef C_Stack _c_stack

    cpdef object peek(self):
        val=self._c_stack.peek()
        if val==NULL:
            raise StackEmpty
        return <object>val
    
    cpdef void push(self,object val):
        self._c_stack.push(val)
    
    cpdef object pop(self):
        val=self._c_stack.pop()
        if val==NULL:
            raise StackEmpty
        return <object>val