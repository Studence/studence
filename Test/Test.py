from OrganisationModule.OrganisationService import OrganisationService
from Protobuff.organisationUiPb_pb2 import OrganisationUiPb
from Protobuff.timeUiPb_pb2 import TimeZoneEnum

serivce = OrganisationService()
org = OrganisationUiPb()
org.name.firstName = 'SchoolDemo'
org.dbInfo.locale.defaultTimeZone = TimeZoneEnum.IST
orga = serivce.create(organisationUiPb=org)
print(orga)
