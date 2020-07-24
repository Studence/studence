from CommonCode.CommonHelper import CommonHelper
from CommonCode.strings import Strings
from Protobuff.loginPb_pb2 import LoginPb
from Protobuff.userTypeUiPb_pb2 import UserTypeEnum
from Updators.EntityUiPbUpdator import EntityUiPbUpdator
from Updators.NameUiPbUpdator import NameUipbUpdator
from Updators.TimeUiPbUpdator import TimeUiPbUpdator
from Utitlty.TimeUtility import TimeUtility


class LoginUpdator:
    m_entityUpdator = EntityUiPbUpdator()
    m_nameUpdator = NameUipbUpdator()
    m_timeUpdator = TimeUiPbUpdator()
    m_timeUtility = TimeUtility()
    m_commonHelper = CommonHelper()

    def update(self, loginUiPb):
        loginPb = LoginPb();
        if (Strings.notEmpty(loginUiPb.dbInfo.id)):
            if ("@" in loginUiPb.dbInfo.id):
                self.m_entityUpdator.update(pb=loginPb.dbInfo, uipb=loginUiPb.dbInfo)
            else:
                loginPb.dbInfo.id = self.m_commonHelper.getdbInfoId(loginUiPb.dbInfo.id,
                                                                      UserTypeEnum.Name(loginUiPb.userType))
                self.m_entityUpdator.update(pb=loginPb.dbInfo, uipb=loginUiPb.dbInfo)
        else:
            assert True, "DbInfo id cannot be empty"
        if(Strings.notEmpty())
