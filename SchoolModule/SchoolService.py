from Protobuff.schoolPb_pb2 import SchoolPb
from Protobuff.schoolUiPb_pb2 import SchoolUiPb, SchoolSearchResponseUiPb
from SchoolModule.SchoolComparetor import SchoolComparetor
from SchoolModule.SchoolConvertor import SchoolConvertor
from SchoolModule.SchoolSearcher import SchoolSearcher
from SchoolModule.SchoolTableName import SchoolTableName
from SchoolModule.SchoolUpdator import SchoolUpdator
from ServiceModule.ACreateEntity import ACreateEntity
from ServiceModule.AGetEntity import AGetEntity
from ServiceModule.ASearchEntity import ASearchEntity
from ServiceModule.AUpdateEntity import AUpdateEntity


class SchoolService:
    m_aCreateEnity = ACreateEntity(SchoolUpdator(), SchoolConvertor(), SchoolPb(), SchoolTableName())
    m_aGetEntity = AGetEntity(SchoolConvertor(), SchoolPb(), SchoolTableName())
    m_aUpdateEntity = AUpdateEntity(SchoolUpdator(), SchoolConvertor(), SchoolComparetor(),
                                    SchoolPb(), SchoolTableName())
    m_aSearchEntity = ASearchEntity(SchoolSearcher(), SchoolSearchResponseUiPb(), SchoolUiPb(),
                                    SchoolTableName());

    def create(self, schoolUiPb):
        return self.m_aCreateEnity.create(uipb=schoolUiPb)

    def get(self, id):
        return self.m_aGetEntity.get(id=id)

    def update(self, id, schoolUipb):
        return self.m_aUpdateEntity.update(id=id, uipb=schoolUipb)

    def search(self, schoolSearchRequestUipb):
        return self.m_aSearchEntity.search(reqUipb=schoolSearchRequestUipb)
