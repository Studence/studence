from CommonCode.strings import Strings
from OrganisationModule.OrganisationHelper import OrganisationHelper
from Protobuff.organisationPb_pb2 import OrganisationPb
from Updators.EntityUiPbUpdator import EntityUiPbUpdator
from Updators.NameUiPbUpdator import NameUipbUpdator
from Updators.TimeUiPbUpdator import TimeUiPbUpdator
from Utitlty.TimeUtility import TimeUtility


class OrganisationUpdator:
    m_entityUpdator = EntityUiPbUpdator()
    m_nameUpdator = NameUipbUpdator()
    m_timeUpdator = TimeUiPbUpdator()
    m_timeUtility = TimeUtility()
    m_organisationHelper = OrganisationHelper()

    def update(self, organisationUiPb):
        organisationPb = OrganisationPb()
        if (Strings.notEmpty(organisationUiPb.dbInfo.id)):
            self.m_entityUpdator.update(pb=organisationPb.dbInfo, uipb=organisationUiPb.dbInfo)
        else:
            assert True, "DbInfo id  Cannot be empty"
        if (Strings.notEmpty(organisationUiPb.name.firstName)):
            self.m_nameUpdator.update(pb=organisationPb.name, uipb=organisationUiPb.name)
        if (organisationUiPb.time.milliseconds > 0):
            self.m_timeUpdator.update(pb=organisationPb.time, uipb=organisationUiPb.time)
        else:
            self.m_timeUpdator.update(pb=organisationPb.time,
                                      uipb=self.m_timeUtility.getTimeUiPb(timeUiPb=organisationUiPb.time,
                                                                          timeZone=organisationUiPb.dbInfo.locale.defaultTimeZone))
        if (Strings.isEmpty(organisationUiPb.orgCode)):
            organisationPb.orgCode = self.m_organisationHelper.getOrgCode(id=organisationUiPb.dbInfo.id,
                                                                            timeuipb=organisationUiPb.time)
        else:
            organisationPb.orgCode = organisationUiPb.orgCode
        return organisationPb
