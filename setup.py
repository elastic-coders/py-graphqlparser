# coding: utf-8

from setuptools import setup, Extension

from Cython.Build import cythonize

extensions = cythonize([
    Extension('graphql_parser.{}'.format(cls_name),
              ['graphql_parser/{}.pyx'.format(cls_name)],
              libraries=['graphqlparser'],
              include_dirs=['.'])
    for cls_name in ['GraphQLParser', 'GraphQLAstVisitor',
                     'GraphQLAst', 'GraphQLAstNode']
])

setup(
    name='graphqlparser',
    version='0.0.3',
    author='Marco Paolini',
    author_email='markopaolini@gmail.com',
    description='Python bindings for libgraphqlparser (Cython-based)',
    long_description='\n\n'.join([open('README.rst', 'r').read(),
                                  '-----', '-----',
                                  open('NEWS.rst', 'r').read()]),
    url='https://github.com/elastic-coders/py-graphqlparser',
    packages=['graphql_parser'],
    install_requires=['cython'],
    package_data={'graphql_parser': ['*.pxd', '*.pyx']},
    include_package_data=True,
    ext_modules=extensions,
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
