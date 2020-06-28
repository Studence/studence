from OrganisationModule.OrganisationService import OrganisationService
from Protobuff.organisationUiPb_pb2 import OrganisationUiPb
from Protobuff.timeUiPb_pb2 import TimeZoneEnum

serivce = OrganisationService()
org = serivce.get(id="kb")
org.name.firstName = 'Demo'
org.name.lastName = 'School Devel'
org.dbInfo.locale.defaultTimeZone = TimeZoneEnum.IST
orga = serivce.update(id="kb",organisationUipb=org)
print(orga)
