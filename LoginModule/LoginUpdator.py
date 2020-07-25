from CommonCode.CommonHelper import CommonHelper
from CommonCode.passwordHashOrDehashHelper import PasswordHasherOrDeHasher
from CommonCode.strings import Strings
from Protobuff.loginPb_pb2 import LoginPb
from Protobuff.userTypeUiPb_pb2 import UserTypeEnum
from Updators.EmailUiPbUpdater import EmailUiPbUpdator
from Updators.EntityUiPbUpdator import EntityUiPbUpdator
from Updators.GenericRefUiPbUpdator import GenericRefUiPbUpdator
from Updators.NameUiPbUpdator import NameUipbUpdator
from Updators.TimeUiPbUpdator import TimeUiPbUpdator
from Utitlty.TimeUtility import TimeUtility


class LoginUpdator:
    m_entityUpdator = EntityUiPbUpdator()
    m_nameUpdator = NameUipbUpdator()
    m_timeUpdator = TimeUiPbUpdator()
    m_emailUpdator = EmailUiPbUpdator()
    m_timeUtility = TimeUtility()
    m_genericRefUpdator = GenericRefUiPbUpdator()
    m_passwordHasherOrdeHasher = PasswordHasherOrDeHasher()
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

        if (Strings.notEmpty(loginUiPb.email.localPart) and Strings.notEmpty(loginUiPb.email.domain)):
            self.m_emailUpdator.update(loginUiPb.email, loginUiPb.email)
        else:
            assert True, "email cannot be empty"

        if (Strings.notEmpty(loginUiPb.password)):
            if (self.m_passwordHasherOrdeHasher.getIsValidMd5(data=loginUiPb.password)):
                loginPb.password = loginUiPb.password
            else:
                loginPb.password = self.m_passwordHasherOrdeHasher.getMd5hashFromPassWord(loginUiPb.password)
        else:
            assert True, "Password cannot be empty"

        if (Strings.notEmpty(loginUiPb.userRef.id)):
            self.m_genericRefUpdator.update(loginPb.userRef, loginUiPb.userRef)
        else:
            assert True, "login must have user"

        if (loginUiPb.userType != UserTypeEnum.UNKNOWN_USER):
            loginPb.userType = loginUiPb.userType
        else:
            assert True, "user type cannot be UNKNOWN_USER"

        if (loginUiPb.time.milliseconds > 0):
            self.m_timeUpdator.update(pb=loginPb.time, uipb=loginUiPb.time)
        else:
            self.m_timeUpdator.update(pb=loginPb.time,
                                      uipb=self.m_timeUtility.getTimeUiPb(timeUiPb=loginUiPb.time,
                                                                          timeZone=loginUiPb.dbInfo.locale.defaultTimeZone))
