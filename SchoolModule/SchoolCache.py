from CacheModule.CacheLoader import CacheLoader
from SchoolModule.SchoolService import SchoolService


class SchoolCache(CacheLoader):

    def __init__(self):
        super(SchoolCache, self).__init__(service=SchoolService())
