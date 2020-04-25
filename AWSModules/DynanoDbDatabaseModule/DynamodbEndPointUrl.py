class DynamodbEndPointUrl:

    def getEndPointUrl(self, awsRegionEnum):
        return "https://dynamodb." + awsRegionEnum.value + ".amazonaws.com"
