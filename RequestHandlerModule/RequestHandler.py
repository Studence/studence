from RequestHandlerModule.RequestHandlerCF import RequestHandlerCF


class RequestHandler:
    m_service = None
    m_uiPb = None
    m_searchUipb = None

    def __init__(self, service, uipb, searchRequest):
        self.m_service = service
        self.m_uiPb = uipb
        self.m_searchUipb = searchRequest

    def handle(self, request):
        requestHandlercf = RequestHandlerCF(self.m_service, self.m_uiPb,self.m_searchUipb)
        requestHandlercf.start(request=request)
        return requestHandlercf.done()
