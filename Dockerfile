FROM ubuntu:16.04

RUN apt-get update -qy
RUN apt-get install -qy build-essential python python3 python3-pip python3-dev git cmake bison flex pkg-config
RUN pip3 install cython

RUN mkdir /tmp/build
COPY libgraphqlparser /tmp/build/libgraphqlparser
COPY ast /tmp/build/ast
COPY examples /tmp/build/examples
COPY graphql_parser /tmp/build/graphql_parser
COPY setup.py *.rst /tmp/build/


RUN cd /tmp/build/libgraphqlparser && \
    cmake . && \
    make && \
    cp libgraphqlparser.so /usr/local/lib
RUN cd /tmp/build && \
    python2 ast/build_ast.py && \
    LDFLAGS="-L./libgraphqlparser" CFLAGS="-Ilibgraphqlparser/c -Ilibgraphqlparser" \
      python3 setup.py build_ext && \
    pip3 install .
ENV LD_LIBRARY_PATH=/usr/local/lib

ENTRYPOINT ["python3", "/tmp/build/examples/visitor_example.py"]
