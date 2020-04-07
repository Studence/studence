from enum import Enum

from CommonQueryExecutor.SearchQueryExecutor.SearchQueryExecutor import SearchQueryExecutor
from CommonQueryExecutor.SearchQueryExecutor.SearchQueryResultFormatter import SearchQueryResultFormatter


class State(Enum):
    CHECK_QUERY_IS_EMPTY = 0;
    SEARCH = 1;
    FORM_RESPONSE = 2
    DONE = 3;


class SearchQueryCF():
    m_responseUipb = None
    m_uipb = None;
    m_response = None;
    m_table = None
    m_subQuery = None
    m_respUipb = None

    def __init__(self, responseUipb, uipb, table):
        self.m_table = table
        self.m_responseUipb = responseUipb
        self.m_uipb = uipb;

    m_searchQueryExecutor = SearchQueryExecutor()

    def start(self, query):
        self.m_subQuery = query
        self.controlFlow(currentState=State.CHECK_QUERY_IS_EMPTY)

    def done(self):
        return self.m_respUipb

    def checkQueryIsEmpty(self):
        if (self.m_subQuery == None):
            assert True, "Query Cannot be Empty"
        else:
            self.controlFlow(currentState=State.SEARCH)

    def searchInDb(self):
        resp = self.m_searchQueryExecutor.search(query=self.m_subQuery,
                                                 table=self.m_table.tableName())
        if (resp != None):
            self.m_response = resp
            self.controlFlow(currentState=State.FORM_RESPONSE)
        else:
            # self.controlFlow(currentState=State.DONE)
            raise Exception('Search not Perform Error occured ' + self.m_subQuery)

    def formResponse(self):
        m_formResponse = SearchQueryResultFormatter(self.m_responseUipb, self.m_uipb)
        self.m_respUipb = m_formResponse.formResponse(response=self.m_response)
        if (self.m_respUipb == None):
            raise Exception('Error while Fromming Respinse' + self.m_response)
        else:
            self.controlFlow(currentState=State.DONE)

    def controlFlow(self, currentState):
        if (currentState == State.CHECK_QUERY_IS_EMPTY):
            self.checkQueryIsEmpty()
        elif (currentState == State.SEARCH):
            self.searchInDb()
        elif (currentState == State.FORM_RESPONSE):
            self.formResponse()
        elif (currentState == State.DONE):
            self.done()
