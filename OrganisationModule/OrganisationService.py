from OrganisationModule.OrganisationComparetor import OrganisationComparetor
from OrganisationModule.OrganisationConvertor import OrganisationConvertor
from OrganisationModule.OrganisationSearcher import OrganisationSearcher
from OrganisationModule.OrganisationTableName import OrganisationTableName
from OrganisationModule.OrganisationUpdator import OrganisationUpdator
from Protobuff.organisationPb_pb2 import OrganisationPb
from Protobuff.organisationUiPb_pb2 import OrganisationUiPb, OrganisationSearchResponseUiPb
from ServiceModule.ACreateEntity import ACreateEntity
from ServiceModule.AGetEntity import AGetEntity
from ServiceModule.ASearchEntity import ASearchEntity
from ServiceModule.AUpdateEntity import AUpdateEntity


class OrganisationService:
    m_aCreateEnity = ACreateEntity(OrganisationUpdator(),OrganisationConvertor(), OrganisationPb(), OrganisationTableName())
    m_aGetEntity = AGetEntity(OrganisationConvertor(), OrganisationPb(), OrganisationTableName())
    m_aUpdateEntity = AUpdateEntity(OrganisationUpdator(), OrganisationConvertor(), OrganisationComparetor(),
                                    OrganisationPb(), OrganisationTableName())
    m_aSearchEntity = ASearchEntity(OrganisationSearcher(), OrganisationSearchResponseUiPb(), OrganisationUiPb(),
                                    OrganisationTableName());

    def create(self, organisationUiPb):
        return self.m_aCreateEnity.create(uipb=organisationUiPb)

    def get(self, id):
        return self.m_aGetEntity.get(id=id)

    def update(self, id, organisationUipb):
        return self.m_aUpdateEntity.update(id=id, uipb=organisationUipb)

    def search(self, organisationSearchRequestUipb):
        return self.m_aSearchEntity.search(reqUipb=organisationSearchRequestUipb)
