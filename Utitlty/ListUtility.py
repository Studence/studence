from addict import Dict


class ListUtility():

    def merge(self, list1, list2):
        return list1 + list2

    def listToDict(self, *argv):
        dict = Dict()
        for list in argv:
            for element in list:
                dict[element.key] = element.value

        return dict
