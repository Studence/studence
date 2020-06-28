from enum import Enum

from switchlang import switch

from CommonCode.convertJSONTOPb import ConvertJSONToPb
from CommonCode.strings import Strings
from ErrorModule.ErrorResponder import ErrorResponder
from Protobuff.errorTypeUiPb_pb2 import INPUT_ERROR, INPUT_VALIDATION_ERROR, JSON_VALIDATION_ERROR, UN_EXPECTED_ERROR, \
    INVALID_RESPONSE
from RequestHandlerModule.RequestHandlerHelper import ResponseHandlerHelper


class RequestTypeEnum(Enum):
    GET = 0;
    CREATE = 1;
    UPDATE = 2
    SEARCH = 3;


class RequestMethodTypeEnum(Enum):
    GET = 0;
    PUT = 1;
    POST = 2
    DELETE = 3;


class State(Enum):
    CHECK_IS_REQ_EMPTY = 0;
    CHECK_TYPE_OF_REQ_METHOD = 1;
    IF_GET_CHECK_REQ_JSON = 2
    VALIDATE_JSON = 3;
    COVERT_TO_UIPB = 4;
    DO_WORK = 5
    RETURN_RESPONSE = 6
    DONE = 7;


class RequestHandlerCF(ErrorResponder):
    m_request = None
    m_service = None
    m_response = None
    m_finalresponse = None
    m_searchRequest = None
    m_uipb = None;
    m_method = None
    m_requestType = None
    m_requestData = None
    m_error = None
    m_requestUiPb = None

    m_requestHandlerHelper = ResponseHandlerHelper()
    m_convertToUipb = ConvertJSONToPb()

    def __init__(self, service, uipb, searchRequestUipb):
        self.m_service = service
        self.m_uipb = uipb
        self.m_searchRequest = searchRequestUipb

    def start(self, request):
        self.m_request = request
        self.controlFlow(currentState=State.CHECK_TYPE_OF_REQ_METHOD)

    def done(self):
        if (self.m_finalresponse == None):
            return self.m_error
        else:
            return self.m_finalresponse

    def checkReqEmpty(self):
        if (Strings.isEmpty(self.m_request.full_path)):
            self.m_error = self.throw(errorTypeEnum=INPUT_ERROR, errorString="Input cannot be Empty or Wrong")
            self.controlFlow(currentState=State.DONE)
        else:
            self.m_requestData = self.m_requestHandlerHelper.getRequestData(request=self.m_request)
            self.controlFlow(currentState=State.IF_GET_CHECK_REQ_JSON)

    def checkTypeOfMethod(self):
        self.m_method = self.m_request.method
        if (Strings.areEquals(self.m_method, RequestMethodTypeEnum.PUT.name)):
            self.m_requestType = RequestTypeEnum.UPDATE
            self.controlFlow(currentState=State.COVERT_TO_UIPB)
        elif (Strings.areEquals(self.m_method, RequestMethodTypeEnum.POST.name)):
            self.m_requestType = RequestTypeEnum.CREATE
            self.controlFlow(currentState=State.COVERT_TO_UIPB)
        self.controlFlow(currentState=State.CHECK_IS_REQ_EMPTY)

    def checkIsJsonAndValid(self):
        data = self.m_requestHandlerHelper.isJson(json=self.m_requestData)
        if (data == None):
            self.m_error = self.throw(errorTypeEnum=INPUT_VALIDATION_ERROR,
                                      errorString="Input cannot be Empty or Wrong")
            self.controlFlow(currentState=State.DONE)
        elif (data == True):
            self.m_requestType = RequestTypeEnum.SEARCH
            self.controlFlow(currentState=State.COVERT_TO_UIPB)
        elif (data == JSON_VALIDATION_ERROR):
            self.m_error = self.throw(errorTypeEnum=JSON_VALIDATION_ERROR,
                                      errorString="Wrong Json")
            self.controlFlow(currentState=State.DONE)
        elif (data == False):
            self.m_requestType = RequestTypeEnum.GET
            self.controlFlow(currentState=State.DO_WORK)

    def convertToUipb(self):
        if (self.m_requestType == RequestTypeEnum.SEARCH):
            self.m_requestUiPb = self.m_convertToUipb.converjsontoPBProper(response=self.m_requestData,
                                                                           instanceType=self.m_searchRequest)
        elif (self.m_requestType == RequestTypeEnum.UPDATE):
            self.m_requestUiPb = self.m_convertToUipb.converjsontoPBProper(response=self.m_request.json,
                                                                           instanceType=self.m_uipb)
        elif (self.m_requestType == RequestTypeEnum.CREATE):
            self.m_requestUiPb = self.m_convertToUipb.converjsontoPBProper(response=self.m_request.json,
                                                                           instanceType=self.m_uipb)
        else:
            self.m_requestUiPb = self.m_convertToUipb.converjsontoPBProper(response=self.m_requestData,
                                                                           instanceType=self.m_uipb)
        self.controlFlow(currentState=State.DO_WORK)

    def doWork(self):
        if (self.m_requestType == RequestTypeEnum.GET):
            self.m_response = self.m_service.get(id=self.m_requestData)
            self.controlFlow(currentState=State.RETURN_RESPONSE)
        elif (self.m_requestType == RequestTypeEnum.UPDATE):
            self.m_response = self.m_service.update(self.m_requestUiPb.dbInfo.id, self.m_requestUiPb)
            self.controlFlow(currentState=State.RETURN_RESPONSE)
        elif (self.m_requestType == RequestTypeEnum.CREATE):
            self.m_response = self.m_service.create(self.m_requestUiPb)
            self.controlFlow(currentState=State.RETURN_RESPONSE)
        elif (self.m_requestType == RequestTypeEnum.SEARCH):
            self.m_response = self.m_service.search(self.m_requestUiPb)
            self.controlFlow(currentState=State.RETURN_RESPONSE)
        else:
            self.m_error = self.throw(errorTypeEnum=UN_EXPECTED_ERROR,
                                      errorString="No such type of service")
            self.controlFlow(currentState=State.DONE)

    def returnResponse(self):
        if (self.m_response != None):
            self.m_finalresponse = self.m_requestHandlerHelper.sendValidResponse(uipb=self.m_response)
        else:
            self.m_error = self.throw(errorTypeEnum=INVALID_RESPONSE,
                                      errorString="Invalid response formed");
        self.controlFlow(currentState=State.DONE)

    def controlFlow(self, currentState):
        with switch(currentState) as s:
            s.case(State.CHECK_IS_REQ_EMPTY, self.checkReqEmpty)
            s.case(State.CHECK_TYPE_OF_REQ_METHOD, self.checkTypeOfMethod)
            s.case(State.IF_GET_CHECK_REQ_JSON, self.checkIsJsonAndValid)
            s.case(State.COVERT_TO_UIPB, self.convertToUipb)
            s.case(State.DO_WORK, self.doWork)
            s.case(State.RETURN_RESPONSE, self.returnResponse)
            s.default(self.done)
