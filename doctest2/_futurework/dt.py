import mymod
from doctestsupport import *


__doc__ = """

>>> import mymod
>>> print mymod.myfunc(4)
[0, 1, 2, 3]



"""
  

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(__name__, 
                   checker=MyOutputChecker()))
    return tests

