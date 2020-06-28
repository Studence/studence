from CommonCode.strings import Strings
from Convertor.EntityPbConvertor import EntityPbConvertor
from Convertor.NamePbConvertor import NamePbConvertor
from Convertor.TimePbConvertor import TimePbConvertor
from Protobuff.organisationUiPb_pb2 import OrganisationUiPb


class OrganisationConvertor:
    m_entityPbConvertor = EntityPbConvertor()
    m_namePbConvertor = NamePbConvertor()
    m_timePbConvertor = TimePbConvertor()

    def convert(self, organisationPb):
        organisationUiPb = OrganisationUiPb()
        if (Strings.notEmpty(organisationPb.dbInfo.id)):
            self.m_entityPbConvertor.convert(pb=organisationPb.dbInfo, uipb=organisationUiPb.dbInfo)
        if (Strings.notEmpty(organisationPb.name.firstName)):
            self.m_namePbConvertor.convert(pb=organisationPb.name, uipb=organisationUiPb.name)
        if (organisationPb.time.milliseconds > 0):
            self.m_timePbConvertor.convert(pb=organisationPb.time, uipb=organisationUiPb.time)
        if (Strings.notEmpty(organisationPb.orgCode)):
            organisationUiPb.orgCode = organisationPb.orgCode
        return organisationUiPb
