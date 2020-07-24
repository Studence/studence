from CommonCode.StringToIntConvertor import StringToIntConverter
from Protobuff.genericRefUiPb_pb2 import GenericRefUiPb


class StudentHelper:
    m_stringToIntConvertor = StringToIntConverter()

    def studentnUiPbToRef(self, studentnUiPb):
        organisationRef = StudentUi
        organisationRef.id = organiationUiPb.dbInfo.id
        organisationRef.name.CopyFrom(organiationUiPb.name)
        organisationRef.code = organiationUiPb.orgCode
        return organisationRef

    def getStudentCode(self, orgid, schid, clshid, timeUipb):
        return timeUipb.year + timeUipb.month + self.m_stringToIntConvertor.convertToString(
            string=orgid) + self.m_stringToIntConvertor.convertToString(
            string=schid) + self.m_stringToIntConvertor.convertToString(string=clshid)
