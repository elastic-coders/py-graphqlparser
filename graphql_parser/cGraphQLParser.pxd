cdef extern from "GraphQLParser.h":
    struct GraphQLAstNode:
      pass

    GraphQLAstNode* graphql_parse_string(const char* text, const char** error)
