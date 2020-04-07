from CommonCode.strings import Strings
from CommonQueryExecutor.SearchQueryExecutor.SearcherConfig import SearcherConfig


class CommonSearchHelper:

    def getSearchSubQuery(self, keys, values):
        maplist = self.getMapToList(keys=keys, values=values)
        return self.getSubQuery(list(maplist))

    def getSubQuery(self, list):
        subQuery = '';
        i = 0
        for data in list:
            subQuery = " " + subQuery + " " + data
            if len(list) - 1 == i:
                continue
            subQuery = " " + subQuery + " " + SearcherConfig.AND.name
            i = i + 1
        return subQuery

    def getEqualTO(self, first, second):
        return first + " = " + Strings.qoutedString(second)

    def getMapToList(self, keys, values):
        return map(self.getEqualTO, keys, values)
