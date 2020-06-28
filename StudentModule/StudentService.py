from BaseCodeModule.BaseService import BaseService
from Protobuff.studentPb_pb2 import StudentPb


class StudentService(BaseService):

    def __init__(self):
        super(StudentService, self).__init__(StudentPb(),)

