import copy
from collections.abc import MutableSequence


class List(MutableSequence):

    def __init__(self, l=[]):
        if type(l) is not list:
            raise ValueError()
        self._inner_list = l
        self._inner_list.clear()

    def __len__(self):
        return len(self._inner_list)

    def __delitem__(self, index):
        self._inner_list.__delitem__(index)

    def insert(self, index, value):
        self._inner_list.insert(index, value)

    def __setitem__(self, index, value):
        self._inner_list.__setitem__(index, value)

    def __getitem__(self, index):
        return self._inner_list.__getitem__(index)

    def __append__(self, object):
        return self._inner_list.append(copy.copy(object))

    def __print__(self):
        print(list(self._inner_list))

    def __list__(self):
        return copy.copy(list(self._inner_list))

    def setList(self, list):
        self._inner_list.extend(list)
