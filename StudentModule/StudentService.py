from BaseCodeModule.BaseService import BaseService
from Protobuff.studentPb_pb2 import StudentPb
from StudentModule.StudentTableName import StudentTableName


class StudentService(BaseService):

    def __init__(self):
        super(StudentService, self).__init__(StudentPb(), StudentUpdator(), StudentConvertor(),
                                                  StudentComparetor(), StudentUpdateListner(),
                                                  StudentTableName())

    def create(self, studentUiPb):
        return self.createEntity(uipb=studentUiPb)

    def get(self, id):
        return self.getEntity(id=id)

    def update(self, id, studentUipb):
        return self.updateEntity(id=id, uipb=studentUipb)

    #def search(self, organisationSearchRequestUipb):
        #return self.m_aSearchEntity.search(reqUipb=organisationSearchRequestUipb)

