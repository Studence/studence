from CacheModule.CacheLoader import CacheLoader
from SchoolModule.SchoolService import SchoolService


class ClassCache(CacheLoader):
    
    def __init__(self):
        super(ClassCache, self).__init__(service=SchoolService())
