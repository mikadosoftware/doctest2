#!/usr/bin/env python
#! -*- coding: utf-8 -*-

### Copyright Paul Brian 2013 

# This program is licensed, without  under the terms of the
# GNU General Public License version 2 (or later).  Please see
# LICENSE.txt for details

###

"""
:author:  paul@mikadosoftware.com <Paul Brian>

Part of doctest2 suite of helpful extras

doclit
======

I want to be able to write books in .rst and still have code examples
in them in Python.  Pah! Easy.

But then I want to import a code example I wrote in chapter 2 into
chapter 3 and run it in the examples there.

Errr... And so *doclit*


:mod:`doclit` will read a doctest-style file, and import all of that
code into a new module and present it to the current namespace.

How does it work?
-----------------

1. parse a file using doctest.DocTestParser
2. Write the "examples" into a temp file
3. import that temp file with :mod:`imp`
4. return the whole thing to current namespace.

The idea is that I want to write in doctest "import
some-other-doctestfile" Then I can write a working exmaple function in
one chapter and use it in the next

usage example
-------------

In a file called chapter1.rst we write ::

    Hello this is some content

    >>> x = 3

In another file, chapter2.rst we::

    Hello, still other content

    >>> from doctest2.doclit import import_docs
    >>> chapter1 = import_docs('chapter1.rst')
    >>> print chapter1.x
    3

And then we can run the below in a REPL::

    >>> import doctest
    >>> doctest.testfile('example2.rst')



"""

import doctest
import os, sys
import imp

##CONSTANTS
FLDR=".doclit"


def write_to_tmp_file(modname, contents):
    """
    Really dumb writing of file to tmp folder ".doclit"
    in pwd

    .. todo::
       I am pretty sure I should replace this is StirngIO
    
    .. todo::
       check that a "doctest" folder exists before wiritng into it
       other checks like .py suffix.
    
    """

    fldr = FLDR
    if not os.path.isdir(fldr):
        os.makedirs(fldr)
    path = os.path.join(fldr, modname + ".py")
    open(path, "w").write(contents)
    return path
    


def extract_from_docfile(f):
    """Read file f, extract doctest-examples and cat them into one

    return the 'plain python' equivvalent of
    the source code in the doctest file

    >>> t = '''
    ... >>> x = 'testing'
    ... '''
    >>> tt = extract_from_docfile(t)
    >>> assert tt.find("testing") > -1
    """
    p = doctest.DocTestParser()
    examples = p.parse(f)
    ez = [i.source for i in examples if hasattr(i, "source")]
    return ''.join(ez)



def import_mod(modname, fldr):
    """ """
    ### Find a module named modname, in the dirs named fldr
    try:
        found_module = imp.find_module(modname, [fldr,])
    except ImportError:
        print "No file named %s in %s" % (modname,
                                          str(fldr)
                                         )
        sys.exit(-1)

    #import the recipie
    try:
        filehandle, fpath, desc = found_module
        mymod = imp.load_module(modname, filehandle, fpath, desc)
    finally:
        filehandle.close()
    return mymod
        
def import_docs(srcfile, modname):
    """ Main function -

    .. todo::
       needs to be more robust re: files

    returns the module object, which should exist in sys.modules
    for the namespace __this__ module is in.
    
    """
    fldr=os.path.abspath(FLDR)
    examplestr = extract_from_docfile(open(srcfile).read())
    write_to_tmp_file(modname, examplestr)
    mymod = import_mod(modname, fldr)
    return mymod

if __name__ == '__main__':
    doctest.testmod()
