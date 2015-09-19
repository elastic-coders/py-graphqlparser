import pytest


def test_parse_ok():
    from graphql_parser import GraphQLParser
    assert GraphQLParser.graphql_parse_string('{query {id}}')


def test_parse_bad():
    from graphql_parser import GraphQLParser
    with pytest.raises(GraphQLParser.GraphQLParseError):
        assert GraphQLParser.graphql_parse_string('{query {id')
