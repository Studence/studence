from google.protobuf.json_format import MessageToJson

from CommonCode.strings import Strings
from Comparetor.AccountDetailsPbComparetor import AccountDetailsPbComparetor
from Comparetor.AddressPbComparetor import AddressPbComparetor
from Comparetor.EnityPbComparetor import EntityPbComparetor
from Comparetor.GenericRefPbComparetor import GenericRefPbComparetor
from Comparetor.ListPbComparetor import ListPbComapretor
from Comparetor.MobileComparetor import MobileComparetor
from Comparetor.NamePbComparetor import NamePbComapretor
from Comparetor.TimePbComparetor import TimePbComparetor
from Protobuff.accountDetailsUiPb_pb2 import UNKNOWN_ACCOUNT_TYPE


class SchoolComparetor:
    m_entityComparetor = EntityPbComparetor()
    m_nameComparetor = NamePbComapretor()
    m_timeComparetor = TimePbComparetor()
    m_accountDetailsComparetor = AccountDetailsPbComparetor()
    m_addressComparetor = AddressPbComparetor()
    m_ListPbComparetor = ListPbComapretor(MobileComparetor())
    m_genericRefComparetor = GenericRefPbComparetor()

    def compare(self, newPb, oldPb):
        self.m_entityComparetor.compare(newPb=newPb.dbInfo, oldPb=oldPb.dbInfo)
        self.m_nameComparetor.comapre(newpb=newPb.name, oldPb=oldPb.name)
        self.m_timeComparetor.comapre(newPb=newPb.createdTime, oldPb=oldPb.createdTime)
        self.m_addressComparetor.compare(newPb=newPb.address, oldPb=oldPb.address)
        self.m_ListPbComparetor.compareList(newPbList=newPb.mobile, oldPbList=oldPb.mobile)
        self.m_genericRefComparetor.compare(newPb=newPb.organisation, oldPb=oldPb.organisation)
        if (Strings.notEmpty(oldPb.schoolCode)):
            if (Strings.notEmpty(newPb.schoolCode)):
                oldPb.schoolCode = newPb.schoolCode
            else:
                raise Exception('Code  Is Empty' + MessageToJson(newPb))
        if (oldPb.accountUseType != UNKNOWN_ACCOUNT_TYPE):
            if (newPb.accountUseType != UNKNOWN_ACCOUNT_TYPE):
                oldPb.accountUseType = newPb.accountUseType
            else:
                raise Exception('accountUseType cannot be UNKNOWN_ACCOUNT_TYPE' + MessageToJson(newPb))

        self.m_accountDetailsComparetor.compare(newPb=newPb.accountDetails, oldPb=oldPb.accountDetails)
        oldPb.accountSection = newPb.accountSection

        return oldPb
