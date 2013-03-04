import unittest
import dt

from doctest import *

tl = unittest.TestLoader()
tsuite = tl.loadTestsFromModule(dt)
print tsuite

unittest.TextTestRunner(verbosity=2).run(tsuite)
