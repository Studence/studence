class ListUiPbUpdator:
    m_updator = None

    def __init__(self, updator):
        self.m_updator = updator

    def listUpdator(self, pbList, uipbList):
        if (len(uipbList) > 0):
            for uipb in uipbList:
                pb = pbList.add()
                self.m_updator.update(pb, uipb)
            return
