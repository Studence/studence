from CommonCode.StringToIntConvertor import StringToIntConverter


class ClassHelper:
    m_stringToIntConvertor = StringToIntConverter()

    def getClassCode(self, schoolCode, id):
        return schoolCode + self.m_stringToIntConvertor.convertToString(string=id)
