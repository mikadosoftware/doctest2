Now I want to use the foo() function defined in 
another non-python file

>>> from doctest2.doclit import doclit
>>> example1 = doclit.import_docs("example1.rst", "example1")
>>> example1.foo()
'Hello world'

Now run this in doctest normally. all should be well.

