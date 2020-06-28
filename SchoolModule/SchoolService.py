from BaseCodeModule.BaseService import BaseService
from Protobuff.schoolPb_pb2 import SchoolPb
from SchoolModule.SchoolComparetor import SchoolComparetor
from SchoolModule.SchoolConvertor import SchoolConvertor
from SchoolModule.SchoolTableName import SchoolTableName
from SchoolModule.SchoolUpdateListner import SchoolUpdateListner
from SchoolModule.SchoolUpdator import SchoolUpdator


class SchoolService(BaseService):

    def __init__(self):
        super(SchoolService, self).__init__(SchoolPb(), SchoolUpdator(), SchoolConvertor(), SchoolComparetor(),
                                            SchoolUpdateListner(), SchoolTableName())

    def create(self, schoolUiPb):
        return self.createEntity(uipb=schoolUiPb)

    def get(self, id):
        return self.getEntity(id=id)

    def update(self, id, schoolUipb):
        return self.updateEntity(id=id, uipb=schoolUipb)
