from ServiceModule.ACreateEntity import ACreateEntity
from ServiceModule.AGetEntity import AGetEntity
from ServiceModule.AUpdateEntity import AUpdateEntity


class BaseService:
    m_aCreateEnity = None
    m_aGetEntity = None
    m_aUpdateEntity = None

    def __init__(self, pbInstance, updator, convertor, comparetor, updateListner, tableName):
        self.m_aCreateEnity = ACreateEntity(updator, convertor, pbInstance,
                                            updateListner, tableName)
        self.m_aGetEntity = AGetEntity(convertor, pbInstance, tableName)
        self.m_aUpdateEntity = AUpdateEntity(updator, convertor, comparetor,
                                             pbInstance, tableName, updateListner)
        # should be modify
        # m_aSearchEntity = ASearchEntity(OrganisationSearcher(), OrganisationSearchResponseUiPb(), OrganisationUiPb(),
        # OrganisationTableName());

    def createEntity(self, uipb):
        return self.m_aCreateEnity.create(uipb=uipb)

    def getEntity(self, id):
        return self.m_aGetEntity.get(id=id)

    def updateEntity(self, id, uipb):
        return self.m_aUpdateEntity.update(id=id, uipb=uipb)

    # def search(self, SearchRequestUipb):
    # return self.m_aSearchEntity.search(reqUipb=organisationSearchRequestUipb)
