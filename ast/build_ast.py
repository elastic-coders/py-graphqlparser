"""Generate source code using libgraphql AST utilities"""
import os
import sys
import subprocess

AST_GENERATED_FILES = [
    ('ast_cython_c', 'cGraphQLAst.pxd'),
    ('ast_cython',  'GraphQLAst.pxd'),
    ('ast_cython_impl', 'GraphQLAst.pyx'),
    ('ast_cython_visitor', 'cGraphQLAstVisitor.pxd'),
    ('ast_cython_visitor_impl', 'GraphQLAstVisitor.pyx'),
]


def get_libgraphqlparser_ast_home():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'libgraphqlparser', 'ast'))


def get_my_ast_home():
    return os.path.abspath(os.path.join(os.path.dirname(__file__)))


def get_my_target_home():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'graphql_parser'))


def main():
    cwd = get_libgraphqlparser_ast_home()
    target_home = get_my_target_home()
    env = os.environ.copy()
    env['PYTHONPATH'] = env.get('PYTHONPATH', '') + os.path.pathsep + get_my_ast_home()
    for language, target in AST_GENERATED_FILES:
        with open(os.path.join(target_home, target), 'wb') as target_f:
            contents = subprocess.check_output([sys.executable, 'ast.py', language, 'ast.ast'],
                                               cwd=cwd, env=env)
            target_f.write(contents)


if __name__ == '__main__':
    main()
