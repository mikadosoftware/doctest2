doclit
======

Doclit is fairly simple - I just want a way to write documentation,
and say define a function in that documentation as an example.

Then I want to write some another chapter which references the fuinction 
above.

chapter1.rst::

    This is an example of a chapter using doclit::


	>>> def foo():
	...     return "Hello world"

    And some more text as part of the chapter.


chapter2::

    Now I want to use the foo() function defined in 
    another non-python file in chapter2.rst ::

	>>> from doctest2.doclit import doclit
	>>> example1 = doclit.import_docs("example1.rst", "example1")
	>>> example1.foo()
	'Hello world'


Now run this in doctest normally. all should be well. ::

    >>> doctest.testfile("chapter2.rst")
