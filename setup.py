from distutils.core import setup
from distutils.extension import Extension
import os

from Cython.Build import cythonize

LIBGRAPHQLPARSER_HOME = os.environ.get('LIBGRAPHQLPARSER_HOME', './libgraphqlparser')


setup(
    name='graphqlparser',
    version='0.0.1',
    author='Marco Paolini',
    author_email='markopaolini@gmail.com',
    description='Python bindings for libgraphqlparser (Cython-based)',
    url='https://github.com/elastic-coders/py-graphqlparser',
    ext_modules=cythonize(
        Extension("grahpql_parser",
                  ["graphql_parser/GraphQLParser.pyx",
                   "graphql_parser/GraphQLAstVisitor.pyx",
                   "graphql_parser/GraphQLAst.pyx",
                   "graphql_parser/GraphQLAstNode.pyx"],
                  libraries=['graphqlparser'],
                  library_dirs=[LIBGRAPHQLPARSER_HOME]
              )
    ),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
