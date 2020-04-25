import json

from CommonCode.DecimalEncoder import DecimalEncoder


class DynamodbResponseJsonParser:

    def parseJson(self, response):
        return json.loads(json.dumps(response), cls=DecimalEncoder)
