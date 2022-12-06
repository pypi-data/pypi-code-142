# dynamodb resource creation
DYDB_RESOURCE_NAME = "dynamodb"
DYDB_RESOURCE_REGION_KEY = "region_name"
DYDB_RESOURCE_ITEM_KEY = "Item"

# dynamo db table resource schema
TABLE_SCHEMA_ATTRIBUTE_KEY = "KeyType"
TABLE_SCHEMA_ATTRIBUTE_NAME = "AttributeName"
ATTRIBUTE_HASH_KEY = "HASH"
ATTRIBUTE_RANGE_KEY = "RANGE"

# TableBaseModel constants
META_CLASS_NAME = "Meta"
META_HASH_VARIABLE = "primary_key"
META_RANGE_VARIABLE = "secondary_key"
DEFAULT_RANGE_KEY = "__EMPTY__"
ITEMS = "Items"
ITEM = "Item"
EMPTY_BINARY_JSON = b"{}"

# Attribute Types
BINARY = "B"
BINARY_SET = "BS"
BOOLEAN = "BOOL"
LIST = "L"
MAP = "M"
NULL = "NULL"
NUMBER = "N"
NUMBER_SET = "NS"
STRING = "S"
STRING_SET = "SS"

type_to_str_mapping = {
    bin: BINARY,
    list: LIST,
    dict: MAP,
    str: STRING,
    int: NUMBER,
}

str_to_type_mapping = {v: k for k, v in type_to_str_mapping.items()}
