from distutils.core import setup,Extension
from Cython.Build import cythonize

mod=Extension(
    "pystack",
    sources=["pystack.pyx","c_stack.cpp"],
    language="c++"
)

setup(ext_modules = cythonize(mod))