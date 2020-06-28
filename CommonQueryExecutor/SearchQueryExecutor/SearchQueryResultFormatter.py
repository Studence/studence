import copy

from CommonCode.convertJSONTOPb import ConvertJSONToPb


class SearchQueryResultFormatter:
    m_responseUipb = None
    m_uipb = None
    m_list = list()
    m_converterJsonToPb = ConvertJSONToPb()

    def __init__(self, responseUipb, uiPb):
        self.m_responseUipb = responseUipb
        self.m_uipb = uiPb
        self.m_list.clear()

    def formResponse(self, response):
        self.m_responseUipb.summary.totalHits = len(response)
        responseuipb = None
        for index, resp in enumerate(response):
            try:
                self.m_list.append(copy.copy(self.m_converterJsonToPb.converjsontoPBProper(response=resp[0],
                                                                                           instanceType=self.m_uipb)))
            except ValueError:
                pass
        self.m_responseUipb.results.extend(self.m_list)
        return self.m_responseUipb
