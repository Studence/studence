from CommonCode.strings import Strings
from Protobuff.accountDetailsUiPb_pb2 import UNKNOWN_ACCOUNT_TYPE
from Protobuff.classTypeUiPb_pb2 import UNKNOWN_CLASS
from Protobuff.schoolPb_pb2 import SchoolPb
from Protobuff.sectionUiPb_pb2 import UNKNOWN_SECTION
from SchoolModule.SchoolHelper import SchoolHelper
from Updators.AccountDetailsUiPbUpdator import AccountDetailsUiPbUpdator
from Updators.AddressUiPbUpdator import AddressUiPbUpdator
from Updators.EntityUiPbUpdator import EntityUiPbUpdator
from Updators.GenericRefUiPbUpdator import GenericRefUiPbUpdator
from Updators.ListUipbUpdator import ListUiPbUpdator
from Updators.MobileUiPbUpdator import MobileUiPbUpdator
from Updators.NameUiPbUpdator import NameUipbUpdator
from Updators.TimeUiPbUpdator import TimeUiPbUpdator
from Utitlty.TimeUtility import TimeUtility


class SchoolUpdator:
    m_entityUpdator = EntityUiPbUpdator()
    m_nameUpdator = NameUipbUpdator()
    m_mobileUpdator = MobileUiPbUpdator()
    m_addressUpdater = AddressUiPbUpdator()
    m_timeUpdator = TimeUiPbUpdator()
    m_timeUtility = TimeUtility()
    m_genericUpdator = GenericRefUiPbUpdator()
    m_schoolHelper = SchoolHelper()
    m_accountDetailsUpdator = AccountDetailsUiPbUpdator()
    m_listUipbUpdator = ListUiPbUpdator(MobileUiPbUpdator())

    def update(self, schoolUiPb):
        schoolPb = SchoolPb()
        if (Strings.notEmpty(schoolUiPb.dbInfo.id)):
            self.m_entityUpdator.update(pb=schoolPb.dbInfo, uipb=schoolUiPb.dbInfo)
        else:
            assert True, "DbInfo id  Cannot be empty"
        if (Strings.notEmpty(schoolUiPb.name.firstName)):
            self.m_nameUpdator.update(pb=schoolPb.name, uipb=schoolUiPb.name)

        if (Strings.notEmpty(schoolUiPb.address.street)):
            self.m_addressUpdater.update(uipb=schoolUiPb.address, pb=schoolPb.address)

        if (len(schoolUiPb.mobile) > 0):
            # schoolPb.mobile.append(self.m_mobileUpdator.getMobileListtPb(uipb=schoolUiPb.mobile))
            self.m_listUipbUpdator.listUpdator(schoolPb.mobile, schoolUiPb.mobile)

        if (schoolUiPb.createdTime.milliseconds > 0):
            self.m_timeUpdator.update(pb=schoolPb.createdTime, uipb=schoolUiPb.createdTime)
        else:
            self.m_timeUpdator.update(pb=schoolPb.createdTime,
                                      uipb=self.m_timeUtility.getTimeUiPb(timeUiPb=schoolUiPb.createdTime,
                                                                          timeZone=schoolUiPb.dbInfo.locale.defaultTimeZone))
        if (Strings.notEmpty(schoolUiPb.organisation.id)):
            self.m_genericUpdator.update(pb=schoolPb.organisation, uipb=schoolUiPb.organisation)
        else:
            raise Exception('School must have his organisation' + schoolUiPb)

        if (Strings.isEmpty(schoolUiPb.schoolCode)):
            schoolPb.schoolCode = self.m_schoolHelper.getSchoolCode(orgid=schoolUiPb.organisation.id,
                                                                    schid=schoolUiPb.dbInfo.id,
                                                                    timeUipb=schoolUiPb.createdTime)
        else:
            schoolPb.schoolCode = schoolUiPb.schoolCode

        if (schoolUiPb.accountUseType != UNKNOWN_ACCOUNT_TYPE):
            schoolPb.accountUseType = schoolUiPb.accountUseType
        else:
            raise Exception('School doesnot have accountUseType  UNKNOWN_ACCOUNT_TYPE')

        if (Strings.notEmpty(schoolUiPb.accountDetails.accountNo)):
            self.m_accountDetailsUpdator.update(uipb=schoolUiPb.accountDetails, pb=schoolPb.accountDetails)

        if (len(schoolUiPb.classType) > 0):
            for classType in schoolUiPb.classType:
                if (classType != UNKNOWN_CLASS):
                    schoolPb.classType.append(classType)
        else:
            raise Exception('School at least at least have one classes')

        if (len(schoolUiPb.sectionType) > 0):
            for sectionType in schoolUiPb.sectionType:
                if (sectionType != UNKNOWN_SECTION):
                    schoolPb.sectionType.append(sectionType)
        else:
            raise Exception('School at least at least have one section')

        schoolPb.accountSection = schoolUiPb.accountSection

        return schoolPb
