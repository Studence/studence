from CacheModule.CacheLoader import CacheLoader
from StudentModule.StudentService import StudentService


class StudentCache(CacheLoader):

    def __init__(self):
        super(StudentCache, self).__init__(service=StudentService())
