======
ahocorasick-python
======

this project is a aho-corasick automaton implementation by python

Usage
=====

1.simple search
------
.. code-block:: python

    import  ahocorasick    # or import hive
    tree=ahocorasick.AhoCorasick("test","book","oo","ok")
    tree.search("test book")


2.search result with index
------
.. code-block:: python

    import  ahocorasick    # or import hive
    tree=ahocorasick.AhoCorasick("test","book","oo","ok")
    tree.search("test book",True)