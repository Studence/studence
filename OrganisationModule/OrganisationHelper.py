from CommonCode.StringToIntConvertor import StringToIntConverter
from Protobuff.genericRefUiPb_pb2 import GenericRefUiPb


class OrganisationHelper:
    m_stringToIntConvertor = StringToIntConverter()

    def getOrgCode(self, id, timeuipb):
        return timeuipb.year + timeuipb.month + self.m_stringToIntConvertor.convertToString(string=id)

    def organisationUiPbToRef(self, organiationUiPb):
        organisationRef = GenericRefUiPb()
        organisationRef.id = organiationUiPb.dbInfo.id
        organisationRef.name.CopyFrom(organiationUiPb.name)
        organisationRef.code = organiationUiPb.orgCode
        return organisationRef
