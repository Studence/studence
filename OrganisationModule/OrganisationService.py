from BaseCodeModule.BaseService import BaseService
from OrganisationModule.OrganisationComparetor import OrganisationComparetor
from OrganisationModule.OrganisationConvertor import OrganisationConvertor
from OrganisationModule.OrganisationSearcher import OrganisationSearcher
from OrganisationModule.OrganisationTableName import OrganisationTableName
from OrganisationModule.OrganisationUpdateListner import OrganisationUpdateListner
from OrganisationModule.OrganisationUpdator import OrganisationUpdator
from Protobuff.organisationPb_pb2 import OrganisationPb
from Protobuff.organisationUiPb_pb2 import OrganisationUiPb, OrganisationSearchResponseUiPb


class OrganisationService(BaseService):

    def __init__(self):
        super(OrganisationService, self).__init__(OrganisationPb(), OrganisationUpdator(), OrganisationConvertor(),
                                                  OrganisationComparetor(), OrganisationUpdateListner(),
                                                  OrganisationTableName())

    def create(self, organisationUiPb):
        return self.createEntity(uipb=organisationUiPb)

    def get(self, id):
        return self.getEntity(id=id)

    def update(self, id, organisationUipb):
        return self.updateEntity(id=id, uipb=organisationUipb)

    #def search(self, organisationSearchRequestUipb):
        #return self.m_aSearchEntity.search(reqUipb=organisationSearchRequestUipb)
