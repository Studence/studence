from BaseCodeModule.BaseService import BaseService
from ClassModule.ClassComparetor import ClassComparetor
from ClassModule.ClassConvertor import ClassConvertor
from ClassModule.ClassTableName import ClassTableName
from ClassModule.ClassUpdator import ClassUpdator
from ClassModule.ClassUpdatorListner import ClassUpdateListner
from Protobuff.classPb_pb2 import ClassPb
from ServiceModule.ACreateEntity import ACreateEntity
from ServiceModule.AGetEntity import AGetEntity
from ServiceModule.AUpdateEntity import AUpdateEntity


class ClassService(BaseService):

    def __init__(self):
        super(ClassService, self).__init__(ClassPb(), ClassUpdator(), ClassConvertor(), ClassConvertor(),
                                           ClassUpdateListner(), ClassTableName())

    def create(self, classUiPb):
        return self.createEntity(uipb=classUiPb)

    def get(self, id):
        return self.getEntity(id=id)

    def update(self, id, classUiPb):
        return self.updateEntity(id=id, uipb=classUiPb)
