from CommonCode.StringToIntConvertor import StringToIntConverter


class OrganisationHelper:
    m_stringToIntConvertor = StringToIntConverter()

    def getOrgCode(self, id, timeuipb):
        return timeuipb.year + timeuipb.month + self.m_stringToIntConvertor.convertToString(string=id)
