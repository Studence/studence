from CommonCode.strings import Strings
from Protobuff.organisationPb_pb2 import OrganisationPb
from Updators.EntityUiPbUpdator import EntityUiPbUpdator
from Updators.NameUiPbUpdator import NameUipbUpdator
from Updators.TimeUipbUpdator import TimeUpdator


class OrganisationUpdator:
    m_entityUpdator = EntityUiPbUpdator()
    m_nameUpdator = NameUipbUpdator()
    m_timeUpdator = TimeUpdator()

    def update(self, organisationUiPb):
        organisationPb = OrganisationPb()
        if (Strings.notEmpty(organisationUiPb.dbInfo.id)):
            self.m_entityUpdator.update(pb=organisationPb.dbInfo, uipb=organisationUiPb.dbInfo)
        if (Strings.notEmpty(organisationUiPb.name.firstName)):
            self.m_nameUpdator.update(pb=organisationPb.name, uipb=organisationUiPb.name)
        if (organisationUiPb.time.milliseconds > 0):
            self.m_timeUpdator.update(pb=organisationPb.time, uipb=organisationUiPb.time)
        return organisationPb
