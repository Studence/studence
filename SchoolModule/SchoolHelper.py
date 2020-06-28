from CommonCode.StringToIntConvertor import StringToIntConverter


class SchoolHelper:
    m_stringToIntConvertor = StringToIntConverter()

    def getSchoolCode(self, orgid, schid, timeUipb):
        return timeUipb.year + timeUipb.month + self.m_stringToIntConvertor.convertToString(
            string=orgid) + self.m_stringToIntConvertor.convertToString(string=schid)
