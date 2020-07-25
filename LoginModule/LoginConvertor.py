from CommonCode.strings import Strings
from Convertor.EmailPbConverter import EmailPbConvertor
from Convertor.EntityPbConvertor import EntityPbConvertor
from Convertor.GenericRefPbConvertor import GenericRefPbConvertor
from Convertor.NamePbConvertor import NamePbConvertor
from Convertor.TimePbConvertor import TimePbConvertor
from Protobuff.loginUiPb_pb2 import LoginUiPb


class LoginConvertor:
    m_entityPbConvertor = EntityPbConvertor()
    m_namePbConvertor = NamePbConvertor()
    m_timePbConvertor = TimePbConvertor()
    m_emailPbConverter = EmailPbConvertor()
    m_genericRefConvertor = GenericRefPbConvertor()

    def convert(self, loginPb):
        loginUiPb = LoginUiPb()
        if (Strings.notEmpty(loginPb.dbInfo.id)):
            self.m_entityPbConvertor.convert(pb=loginPb.dbInfo, uipb=loginUiPb.dbInfo)
        if (Strings.notEmpty(loginPb.email.localPart) and Strings.notEmpty(loginPb.email.domain)):
            self.m_emailPbConverter.convert(uipb=loginUiPb.email, pb=loginPb.email)
        if (Strings.notEmpty(loginPb.password)):
            loginUiPb.password = loginPb.password
        if (Strings.notEmpty(loginPb.userRef.id)):
            self.m_genericRefConvertor.convert(uipb=loginUiPb.userRef, pb=loginPb.userRef)
        loginUiPb.userType = loginPb.userType
        if (loginPb.time.milliseconds > 0):
            self.m_timePbConvertor.convert(pb=loginPb.time, uipb=loginUiPb.time)
        return loginUiPb
