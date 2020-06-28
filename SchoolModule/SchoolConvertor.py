from CommonCode.strings import Strings
from Convertor.AccountDetailsPbConvertor import AccountDetailsPbConvertor
from Convertor.AddressPbConvertor import AddressPbConvertor
from Convertor.EntityPbConvertor import EntityPbConvertor
from Convertor.GenericRefPbConvertor import GenericRefPbConvertor
from Convertor.ListPbConvertor import ListPbConvertor
from Convertor.MobilePbConvertor import MobilePbConvertor
from Convertor.NamePbConvertor import NamePbConvertor
from Convertor.TimePbConvertor import TimePbConvertor
from Protobuff.accountDetailsUiPb_pb2 import UNKNOWN_ACCOUNT_TYPE
from Protobuff.schoolUiPb_pb2 import SchoolUiPb


class SchoolConvertor:
    m_entityConvertor = EntityPbConvertor()
    m_nameConvertor = NamePbConvertor()
    m_timeConvertor = TimePbConvertor()
    m_addressConvertor = AddressPbConvertor()
    m_mobileConvetor = MobilePbConvertor()
    m_genericRefConvertor = GenericRefPbConvertor()
    m_accountDetailsConvertor = AccountDetailsPbConvertor()
    m_listConvertor = ListPbConvertor(MobilePbConvertor())

    def convert(self, schoolPb):
        schoolUiPb = SchoolUiPb()
        if (Strings.notEmpty(schoolPb.dbInfo.id)):
            self.m_entityConvertor.convert(pb=schoolPb.dbInfo, uipb=schoolUiPb.dbInfo)
        if (Strings.notEmpty(schoolPb.name.firstName)):
            self.m_nameConvertor.convert(pb=schoolPb.name, uipb=schoolUiPb.name)
        if (Strings.notEmpty(schoolPb.address.street)):
            self.m_addressConvertor.convert(uipb=schoolUiPb.address, pb=schoolPb.address)
        if (len(schoolPb.mobile) > 0):
            # schoolUiPb.mobile.extend(self.m_mobileConvetor.getMobileListtUiPb(pb=schoolPb.mobile))
            self.m_listConvertor.listConvertor(uipbList=schoolUiPb.mobile, pbList=schoolPb.mobile)
        if (schoolPb.createdTime.milliseconds > 0):
            self.m_timeConvertor.convert(pb=schoolPb.createdTime, uipb=schoolUiPb.createdTime)
        if (Strings.notEmpty(schoolPb.organisation.id)):
            self.m_genericRefConvertor.convert(uipb=schoolUiPb.organisation, pb=schoolPb.organisation)
        if (Strings.notEmpty(schoolPb.schoolCode)):
            schoolUiPb.schoolCode = schoolPb.schoolCode
        if (schoolPb.accountUseType != UNKNOWN_ACCOUNT_TYPE):
            schoolUiPb.accountUseType = schoolPb.accountUseType
        if (Strings.notEmpty(schoolPb.accountDetails.accountNo)):
            self.m_accountDetailsConvertor.convert(pb=schoolPb.accountDetails, uipb=schoolUiPb.accountDetails)
        schoolUiPb.accountSection = schoolPb.accountSection
        return schoolUiPb
