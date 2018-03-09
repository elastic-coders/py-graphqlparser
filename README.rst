Graphql parser based  on libgraphqlparser
=========================================

.. image:: https://circleci.com/gh/elastic-coders/py-graphqlparser.svg?style=svg
    :target: https://circleci.com/gh/elastic-coders/py-graphqlparser

Python2.7+ Python3.4+ class-based bindings to libgraphqlparser; just a thin layer on top of ``libgraphqlparser`` C API.

Still **EXPERIMENTAL**


Installing
----------

First install ``libgraphqlparser`` following instructions on `libgraphqlparser github page`_ .

Next you can install ``graphqlparser``. The easiest way is using precompiled wheels which are usually available
on `graphqlparser github releases`_

Pick the right wheel for your platform and python version, then install it using pip::

  pip install https://github.com/elastic-coders/py-graphqlparser/releases/download/v0.0.4/graphqlparser-0.0.4-cp36-cp36m-linux_x86_64.whl


As an alternative you can install ``graphqlparser`` from source distribution:

- Install ``cython``
- Set an env var ``$GRAPHQL_HOME`` to the folder where ``libgraphqlparser.so`` and ``Ast.h`` are
- Install ``graphqlparser`` with pip::

    LDFLAGS="-L$GRAPHQL_HOME" CFLAGS="-I$GRAPHQL_HOME/c -I$GRAPHQL_HOME" pip install graphqlparser


Usage
-----

Make sure ``libgraphqlparser`` is available to the loader. You can add its base dir to  ``LD_LIBRARY_PATH``.

Then you can start parsing by creating your custom visitor class:

.. code-block:: python

  from graphql_parser import GraphQLAstVisitor

  class MyVisitor(GraphQLAstVisitor.GraphQLAstVisitor):

      def visit_field(self, node):
          print('start field %s visit' % node)
          # Return 1 to keep visiting children, 0 to skip them
          return 1

      def end_visit_field(self, node):
          print('end field %s visit' % node)

And using it to visit a parsed query:

.. code-block:: python

  from graphql_parser import GraphQLParser

  query = '{query{}}'
  node = GraphQLParser.graphql_parse_string(query)
  MyVisitor().visit_node(node)

See also ``examples`` folder.


Building from source checkout
-----------------------------

Rebuild the generated cython files from the libgraphql AST (usually not needed)

- download submodules with ``git checkout --recursive``
- build libgraphql library in folder ``./libgraphqlparser`` (python2.7 required for building)
  (usually ``pushd libgraphqlparser && cmake . && make && popd`` works)
- generate source code with ``python ast/build_ast.py``
- you can now switch to python 3
- install ``cython``
- run::

    LDFLAGS="-L./libgraphqlparser" CFLAGS="-Ilibgraphqlparser/c -Ilibgraphqlparser" python setup.py build_ext


To create a wheel distribution:

- install wheel: ``pip install wheel``
- create wheelhouse ``mkdir .wheelhouse``
- build with ``pip wheel --wheel-dir=.wheelhouse .``


Known issues
------------

- Only (lightly) tested on python3
- Unicode string handling not yet complete (a mixture of bytes and strings all over)
- Exceptions in the visitor's class callbacks are ignored
- libgraphqlparser is **dynamically** linked but It would be better if it was linked statically


TODO
----

- build more wheel packages for linux 32 bit and other platforms


.. _libgraphqlparser github page: https://github.com/graphql/libgraphqlparser
.. _graphqlparser github releases:  https://github.com/elastic-coders/py-graphqlparser/releases/
