from CommonCode.List.List import List
from OrganisationModule.OrganisationService import OrganisationService
from Protobuff.accountDetailsUiPb_pb2 import SINGLE_USE
from Protobuff.mobileUiPb_pb2 import MobileUiPb, ISD
from Protobuff.schoolUiPb_pb2 import SchoolUiPb
from Protobuff.timeUiPb_pb2 import IST
from SchoolModule.SchoolService import SchoolService

service = SchoolService()
organisationService = OrganisationService()

org = organisationService.get(id="k")

school = SchoolUiPb()
mymobileList = List()
school.dbInfo.locale.defaultTimeZone = IST
school.name.firstName = "Studence"
school.name.lastName = "school"
school.address.street = "jugal vihar colony"
school.address.landmark = "near water Tank"
school.address.area = "Faizullaganj"
school.address.city = "Lucknow"
school.address.state = "uttar pradesh"
mobile = school.mobile.add()
mobile.code = ISD
mobile.number = "9621019232"
mobile = school.mobile.add()
mobile.code = ISD
mobile.number = "8687598496"
school.organisation.id = org.dbInfo.id
school.organisation.name.CopyFrom(org.name)
school.organisation.code = org.orgCode
school.accountUseType = SINGLE_USE
school.accountDetails.accountNo = "1234546789987456321"
school.accountDetails.ifscCode = "BOI96325"
school.accountDetails.recipientName = "SHUBHAM TIWARI"
school.accountDetails.bankName = "Bank of India"
school.accountDetails.branch = "Handori"
school.accountDetails.googlePay.upiId = "shubham@boibk"
print(service.get(id="0"))
#print(service.update(id="r",schoolUipb=school))
