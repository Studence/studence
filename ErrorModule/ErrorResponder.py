import json

from flask import Response

from Protobuff.errorTypeUiPb_pb2 import ErrorUiPb
from RequestHandlerModule.RequestHandlerHelper import ResponseHandlerHelper


class ErrorResponder:
    m_convertToJson = ResponseHandlerHelper()

    def genreateError(self, errorUiPb):
        return Response(self.m_convertToJson.getProtobufToJSON(errorUiPb),
                        status=errorUiPb.status,
                        mimetype='application/json')

    def throw(self, errorTypeEnum, errorString):
        return self.genreateError(errorUiPb=self.getInputError(errorString=errorString, errorEnum=errorTypeEnum))

    def getInputError(self, errorString, errorEnum):
        errorUiPb = ErrorUiPb()
        errorUiPb.status = 400
        errorUiPb.error = errorString
        errorUiPb.errorType = errorEnum
        return errorUiPb
