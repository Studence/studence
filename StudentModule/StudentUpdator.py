from CommonCode.strings import Strings
from Convertor.EmailPbConverter import EmailPbConvertor
from Protobuff.studentPb_pb2 import StudentPb
from RefUpdator.ClassUiPbRefUpdator import ClassUiPbRefUpdator
from StudentModule.StudentHelper import StudentHelper
from Updators.AddressUiPbUpdator import AddressUiPbUpdator
from Updators.EmailUiPbUpdater import EmailUiPbUpdator
from Updators.EntityUiPbUpdator import EntityUiPbUpdator
from Updators.ListUipbUpdator import ListUiPbUpdator
from Updators.MobileUiPbUpdator import MobileUiPbUpdator
from Updators.NameUiPbUpdator import NameUipbUpdator
from Updators.TimeUiPbUpdator import TimeUiPbUpdator
from Utitlty.TimeUtility import TimeUtility


class StudentUpdator:
    m_entityUpdator = EntityUiPbUpdator()
    m_nameUpdator = NameUipbUpdator()
    m_timeUpdator = TimeUiPbUpdator()
    m_timeUtility = TimeUtility()
    m_studentHelper = StudentHelper()
    m_emailUpdater = EmailUiPbUpdator()
    m_addressUpdater = AddressUiPbUpdator()
    m_listUipbUpdator = ListUiPbUpdator(MobileUiPbUpdator())
    m_classRefUpdator = ClassUiPbRefUpdator()

    def update(self, studentUiPb):
        studentPb = StudentPb()
        if (Strings.notEmpty(studentUiPb.dbInfo.id)):
            self.m_entityUpdator.update(pb=studentPb.dbInfo, uipb=studentUiPb.dbInfo)
        else:
            assert True, "DbInfo id  Cannot be empty"
        if (Strings.notEmpty(studentUiPb.name.firstName)):
            self.m_nameUpdator.update(pb=studentPb.name, uipb=studentUiPb.name)
        if (studentUiPb.time.milliseconds > 0):
            self.m_timeUpdator.update(pb=studentPb.time, uipb=studentUiPb.time)
        else:
            self.m_timeUpdator.update(pb=studentPb.time,
                                      uipb=self.m_timeUtility.getTimeUiPb(timeUiPb=studentUiPb.time,
                                                                          timeZone=studentUiPb.dbInfo.locale.defaultTimeZone))

        if(Strings.notEmpty(studentUiPb.email.localPart) and Strings.notEmpty(studentUiPb.email.domain)):
            self.m_emailUpdater.update(studentPb.email,studentUiPb.email)

        if(Strings.notEmpty(studentUiPb.address.street) and Strings.notEmpty(studentUiPb.address.landmark)):
            self.m_addressUpdater.update(studentPb.address,studentUiPb.address)


        if(len(studentUiPb.mobile) > 0):
            # studentPb.mobile.append(self.m_mobileUpdator.getMobileListtPb(uipb=studentUiPb.mobile))
            self.m_listUipbUpdator.listUpdator(studentPb.mobile, studentUiPb.mobile)

        if(Strings.notEmpty(studentUiPb.classRef.id)):
            self.m_classRefUpdator.refUpdator(studentPb.classRef,studentUiPb.classRef)
        if (Strings.isEmpty(studentUiPb.studentcode)):
            studentPb.schoolCode = self.m_studentHelper.getStudentCode(orgid=studentUiPb.classRef.schoolRef.id,
                                                                    schid=studentUiPb.classRef.schoolRef.id,
                                                                    clshid=studentUiPb.classRef.id,
                                                                    timeUipb=studentUiPb.createdTime)
        else:
            studentPb.schoolCode = studentUiPb.schoolCode


        return studentPb
