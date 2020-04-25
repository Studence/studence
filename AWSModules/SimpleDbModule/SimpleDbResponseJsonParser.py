import json


class SimpleDbResponseJsonParser:

    def parseJson(self, response):
        return json.loads(json.dumps(response))
