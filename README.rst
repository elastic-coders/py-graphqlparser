Graphql parser based  on libgraphqlparser
=========================================

Python2.7+ Python3.4+ class-based bindings to libgraphqlparser

Still **EXPERIMENTAL**


Installing
----------

Precompiled wheels are usually available on github https://github.com/elastic-coders/py-graphqlparser/releases/

Make sure you pick the right wheel for your platform and python version, then install them using pip::

  pip install https://github.com/elastic-coders/py-graphqlparser/releases/download/v0.0.3/graphqlparser-0.0.3-cp27-none-linux_x86_64.whl


Installing from source is a bit more complex. The main steps are

- Install ``cython``
- Download and build ``libgraphqlparser``
- set an env var ``$GRAPHQL_HOME`` to the folder where libgraphqlparser is
- compile with::

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

    LDFLAGS="-L./libgraphqlparser" CFLAGS="-Ilibgraphqlparser/c -Ilibgraphqlparser" python setup.py build_extx


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
