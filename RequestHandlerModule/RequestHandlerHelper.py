import json

from flask import Response

from CommonCode.convertPbToJSON import ConvertPbToJSON
from CommonCode.strings import Strings
from Protobuff.errorTypeUiPb_pb2 import JSON_VALIDATION_ERROR


class ResponseHandlerHelper:
    m_convertToJson = ConvertPbToJSON()

    def getProtobufToJSON(self, uipb):
        return json.dumps(json.loads(self.m_convertToJson.converPbtojson(uipb)), separators=(',', ':'))

    def sendValidResponse(self, uipb):
        return Response(self.getProtobufToJSON(uipb),
                        status=200,
                        mimetype='application/json')

    def getRequestData(self, request):
        if (not "query" in str(request.full_path)):
            data = request.full_path.replace(request.path, '')
            return data.replace("?", '')
        else:
            return request.args.get('query')

    def isJson(self, json):
        if (Strings.isEmpty(str(json))):
            return None;
        elif ("{" in str(json)):
            if (self.json_validator(json)):
                return True
            else:
                return JSON_VALIDATION_ERROR
        else:
           return False

    def json_validator(data):
        try:
            json.loads(data)
            return True
        except ValueError as error:
            return False
