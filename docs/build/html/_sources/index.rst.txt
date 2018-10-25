.. safepickle documentation master file, created by
   sphinx-quickstart on Wed Oct 24 20:52:16 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to safepickle's documentation!
======================================

.. toctree::
   :maxdepth: 1


safepickle
====================
.. automodule:: safepickle.safepickle
   :members:


types
=====

safepickle currently supports all types supported by pickle (https://docs.python.org/3/library/pickle.html#what-can-be-pickled-and-unpickled) with the following exceptions:

No support for:

- complex numbers
- functions defined at the top level of a module (using def, not lambda)
- built-in functions defined at the top level of a module
- classes that are defined at the top level of a module
- instances of such classes whose the result of calling getstate() is picklable