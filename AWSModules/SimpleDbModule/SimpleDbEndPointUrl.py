class SimpleDbEndPointUrl:

    def getEndPointUrl(self, awsRegionEnum):
        return "https://sdb." + awsRegionEnum.value + ".amazonaws.com"
