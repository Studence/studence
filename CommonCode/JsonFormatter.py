import json

from google.protobuf.json_format import MessageToJson


class JsonFormatter:

    @staticmethod
    def printToString(message):
        return json.dumps(json.loads(MessageToJson(message)), separators=(',', ':'))
