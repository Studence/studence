from CommonCode.strings import Strings
from Convertor import EmailPbConverter
from Convertor.AddressPbConvertor import AddressPbConvertor
from Convertor.EmailPbConverter import EmailPbConvertor
from Convertor.EntityPbConvertor import EntityPbConvertor
from Convertor.NamePbConvertor import NamePbConvertor
from Convertor.TimePbConvertor import TimePbConvertor
from Protobuff.studentUiPb_pb2 import StudentUiPb


class StudentConvertor:
    m_entityPbConvertor = EntityPbConvertor()
    m_namePbConvertor = NamePbConvertor()
    m_timePbConvertor = TimePbConvertor()
    m_emailPbConverter = EmailPbConvertor()
    m_addressConvertor = AddressPbConvertor()

    def convert(self, studentPb):
        studentUiPb = StudentUiPb()
        if (Strings.notEmpty(studentPb.dbInfo.id)):
            self.m_entityPbConvertor.convert(pb=studentPb.dbInfo, uipb=studentUiPb.dbInfo)
        if (Strings.notEmpty(studentPb.name.firstName)):
            self.m_namePbConvertor.convert(pb=studentPb.name, uipb=studentUiPb.name)
        if (studentPb.time.milliseconds > 0):
            self.m_timePbConvertor.convert(pb=studentPb.time, uipb=studentUiPb.time)
        if (Strings.notEmpty(studentPb.orgCode)):
            studentUiPb.orgCode = studentPb.orgCode
        if(Strings.notEmpty(studentPb.email.localPart) and Strings.notEmpty(studentPb.email.domain)):
            self.m_emailPbConverter.convert(uipb=studentUiPb.email,pb=studentPb.email)
        if(Strings.notEmpty(studentUiPb.address.street) and Strings.notEmpty(studentUiPb.address.landmark)):
            self.m_addressConvertor.convert(uipb=studentUiPb.address,pb=studentPb.address)
        if
        return studentUiPb
