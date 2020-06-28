from itertools import zip_longest

from CommonCode.List.List import List


class ListPbComapretor:
    m_comparetor = None

    def __init__(self, comparetor):
        self.m_comparetor = comparetor

    def compareList(self, newPbList, oldPbList):
        if (len(newPbList) == 0):
            return
        myNewPbList = List()
        myNewPbList.clear()
        for newPb, oldPb in zip_longest(newPbList, oldPbList):
            if (oldPb != None):
                self.m_comparetor.compare(newPb, oldPb)
                myNewPbList.__append__(oldPb)
            else:
                if (newPb != None):
                    myNewPbList.__append__(newPb)
        del oldPbList[:]
        oldPbList.extend(myNewPbList)
