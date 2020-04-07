from enum import Enum

from google.protobuf.json_format import MessageToJson

from CommonCode.CommonSearchHelper import CommonSearchHelper
from CommonQueryExecutor.GetQueryExecutor.GetQuery import GetQuery
from CommonQueryExecutor.SearchQueryExecutor.SearchQuery import SearchQuery


class State(Enum):
    CHECK_UIPB_IS_NOT_EMPTY = 0;
    BUILD_QUERY = 1
    PERFORM_SEARCH = 2;
    DONE = 3;


class ASearchEntityCF():
    m_requipb = None;
    m_searcher = None;
    m_response = None;
    m_responseUipb = None
    m_subQuery = None
    m_instance = None
    m_table = None

    m_commonSearchHelper = CommonSearchHelper()

    def __init__(self, searcher, responseUipb, instance, table):
        self.m_responseUipb = responseUipb;
        self.m_searcher = searcher
        self.m_instance = instance
        self.m_table = table

    def start(self, reqUipb):
        self.m_requipb = reqUipb
        self.controlFlow(currentState=State.BUILD_QUERY)

    def done(self):
        return self.m_response

    def checkuipbIsEmpty(self):
        if (self.m_responseUipb == None):
            assert True, "Search request Cannot be Empty"
            self.controlFlow(currentState=State.DONE)
        else:
            self.controlFlow(currentState=State.BUILD_QUERY)

    def buildQuery(self):
        keys, values = self.m_searcher.handler(self.m_requipb)

        if (len(keys) > 0 and len(values) > 0):
            self.m_subQuery = self.m_commonSearchHelper.getSearchSubQuery(keys=keys, values=values)
            if (self.m_subQuery == None):
                raise Exception('Error occured while Building Query to String')
            else:
                self.controlFlow(currentState=State.PERFORM_SEARCH)
        else:
            raise Exception('Error occured while Building Query in Searcher')

    def performSearch(self):
        searchQuery = SearchQuery(self.m_responseUipb, self.m_instance, self.m_table)
        resp = searchQuery.search(self.m_subQuery)
        if (resp == None):
            raise Exception('Error while Converting to Uipb ' + MessageToJson(self.m_pb))
        else:
            self.m_response = resp;
            self.controlFlow(currentState=State.DONE)

    def controlFlow(self, currentState):
        if (currentState == State.CHECK_UIPB_IS_NOT_EMPTY):
            self.checkuipbIsEmpty()
        elif (currentState == State.BUILD_QUERY):
            self.buildQuery()
        elif (currentState == State.PERFORM_SEARCH):
            self.performSearch()
        elif (currentState == State.DONE):
            self.done()
