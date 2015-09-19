import pytest


def test_parse_ok():
    import GraphQLParser
    assert GraphQLParser.graphql_parse_string('{query {id}}')


def test_parse_bad():
    import GraphQLParser
    with pytest.raises(GraphQLParser.GraphQLParseError):
        assert GraphQLParser.graphql_parse_string('{query {id')
