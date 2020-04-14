from Protobuff.entityUiPb_pb2 import StatusEnum
from SchoolModule.SchoolSearchConfig import SchoolSearchConfig


class SchoolSearcher:
    m_keys = list()
    m_values = list()

    def handler(self, schoolSearchRequestUipb):
        self.m_keys.clear()
        self.m_values.clear()
        self.addRequiredExpression()
        if (schoolSearchRequestUipb == None):
            assert True, "Search request is Empty"

        return self.m_keys, self.m_values

    def addRequiredExpression(self):
        self.m_keys.append(SchoolSearchConfig.LIFETIME.value)
        self.m_values.append(StatusEnum.Name(StatusEnum.ACTIVE))
