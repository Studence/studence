import copy

from CommonCode.List.List import List


class ListPbConvertor:
    m_convertor = None

    def __init__(self, convertor):
        self.m_convertor = convertor

    def listConvertor(self, uipbList, pbList):
        if (len(pbList) > 0):
            myuipbList = List()
            for pb in pbList:
                uipb = uipbList.add()
                self.m_convertor.convert(uipb, pb)
                del uipb
            return
