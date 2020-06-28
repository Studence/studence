from enum import Enum


class DynamoDbKeyTypeEnum(Enum):
    HASH_KEY = 'HASH'
    RANGE_KEY = 'RANGE_KEY'
