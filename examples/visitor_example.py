import sys

from graphql_parser import GraphQLAstVisitor
from graphql_parser import GraphQLParser


class Visitor(GraphQLAstVisitor.GraphQLAstVisitor):

    def __init__(self):
        self.level = 0

    def visit_document(self, node):
        print('document start')
        return 1

    def visit_operation_definition(self, node):
        print(node.__class__, node.get_operation())
        return 1

    def visit_variable_definition(self, node):
        print(node.__class__)
        return 1

    def visit_selection_set(self, node):
        print(node.__class__)
        return 1

    def visit_selection(self, node):
        print(node.__class__)
        return 1

    def visit_field(self, node):
        print(node.__class__, node.get_name().get_value(), node.get_alias())
        return 1

    def visit_argument(self, node):
        print(node.__class__, node.get_name().get_value())
        return 1

    def visit_fragment_spread(self, node):
        print(node.__class__, node.get_name().get_value())
        return 1

    def visit_inline_fragment(self, node):
        print(node.__class__, node.get_name().get_value())
        return 1

    def visit_fragment_definition(self, node):
        print(node.__class__, node.get_name().get_value())
        return 1

    def visit_variable(self, node):
        print(node.__class__, node.get_name().get_value())
        return 1

    def visit_object_field(self, node):
        print(node.__class__, node.get_name().get_value())
        return 1

    def visit_directive(self, node):
        print(node.__class__, node.get_name().get_value())
        return 1

    def visit_int_value(self, node):
        print(node.__class__, node.get_value())
        return 1

    def visit_string_value(self, node):
        print(node.__class__, node.get_value())
        return 1

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='GraphQL parser example')
    parser.add_argument('query')
    args = parser.parse_args()
    node = GraphQLParser.graphql_parse_string(args.query)
    Visitor().visit_node(node)
