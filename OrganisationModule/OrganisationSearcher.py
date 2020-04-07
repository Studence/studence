from OrganisationModule.OrganisationSearchConfig import OrganisarionSearchConfig
from Protobuff.entityUiPb_pb2 import StatusEnum


class OrganisationSearcher:
    m_keys = list()
    m_values = list()

    def handler(self, organisationSearchRequestUiPb):
        self.m_keys.clear()
        self.m_values.clear()
        self.addRequiredExpression()
        # if (organisationSearchRequestUiPb == None):
        # assert True, "Search request is Empty"

        return self.m_keys, self.m_values

    def addRequiredExpression(self):
        self.m_keys.append(OrganisarionSearchConfig.LIFETIME.value)
        self.m_values.append(StatusEnum.Name(StatusEnum.ACTIVE))
