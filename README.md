# libgraphql cython port

Python2.7+ Python3.4+ class-based bindings to libgraphqlparser

See usage example in `examples/visitor_example.py`

Still **EXPERIMENTAL**


## Building from source

- download submodules with `git checkout --recursive`
- build libgraphql library in folder `./libgraphql` (python2.7 required for building)
(usually `pushd libgraphqlparser && cmake . && make && popd` works)
- generate source code with `python ast/build_ast.py`
- you can now switch to python 3
- install `cython`
- run `LDFLAGS="-L./libgraphqlparser" CFLAGS="-Ilibgraphqlparser/c -Ilibgraphqlparser" python setup.py build_ext`

To package with wheel:
- install wheel
- create wheelhouse `mkdir .wheelhouse`
- build with `pip wheel --wheel-dir=.wheelhouse .`


## Run

Make sure `libgraphql` is available to the loader in your `LD_LIBRARY_PATH`


## Known issues

- Only (lightly) tested on python3
- Unicode string handling not yet complete (a mixture of bytes and strings all over)
- Exceptions in the visitor's class callbacks are ignored
- libgraphqlparser is **dynamically** linked but It would be better if it was linked statically


## TODO

- build and upload wheels to pypi
- build more wheel packages for linux 32 bit and other platforms
