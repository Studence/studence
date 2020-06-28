from enum import Enum


class AWSRegionsEnum(Enum):
    US_EAST_1 = "us-east-1"


class EndPointUrl:

    def getEndUrl(self, awsRegionsEnum):
        if (awsRegionsEnum == AWSRegionsEnum.US_EAST_1):
            return "https://dynamodb.us-east-1.amazonaws.com"
