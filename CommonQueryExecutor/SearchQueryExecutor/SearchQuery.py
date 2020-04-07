from CommonQueryExecutor.SearchQueryExecutor.SearchQueryCF import SearchQueryCF


class SearchQuery:
    m_table = None;
    m_responseUipb = None
    m_uipb = None

    def __init__(self, responseUipb, uipb, table):
        self.m_table = table
        self.m_responseUipb = responseUipb
        self.m_uipb = uipb

    def search(self, query):
        searchQuerycf = SearchQueryCF(self.m_responseUipb, self.m_uipb, self.m_table)
        searchQuerycf.start(query=query)
        return searchQuerycf.done();
