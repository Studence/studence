from google.protobuf.json_format import MessageToJson

from ClassModule.ClassHelper import ClassHelper
from CommonCode.strings import Strings
from Protobuff.classPb_pb2 import ClassPb
from Protobuff.classTypeUiPb_pb2 import UNKNOWN_CLASS
from Protobuff.sectionUiPb_pb2 import UNKNOWN_SECTION
from RefUpdator.SchoolUiPbRefUpdatpr import SchoolRefUiPbUpdator
from Updators.EntityUiPbUpdator import EntityUiPbUpdator
from Updators.NameUiPbUpdator import NameUipbUpdator
from Updators.TimeUiPbUpdator import TimeUiPbUpdator
from Utitlty.TimeUtility import TimeUtility


class ClassUpdator:
    m_entityUipbUpdator = EntityUiPbUpdator()
    m_nameUiPbUpdator = NameUipbUpdator()
    m_schooRefUpdator = SchoolRefUiPbUpdator()
    m_timeUpdator = TimeUiPbUpdator()
    m_timeUtility = TimeUtility()
    m_classHelper = ClassHelper()

    def updator(self, classUiPb):
        classPb = ClassPb()
        if (Strings.notEmpty(classUiPb.dbInfo.id)):
            self.m_entityUipbUpdator.update(pb=classPb.dbInfo, uipb=classUiPb.dbInfo)
        else:
            assert True, "DbInfo id  Cannot be empty"
        if (Strings.notEmpty(classUiPb.name.firstName)):
            self.m_nameUiPbUpdator.update(pb=classUiPb.name, uipb=classUiPb.name)

        if (classUiPb.classType != UNKNOWN_CLASS):
            classPb.classType = classUiPb.classType
        else:
            assert True, "Class type  Cannot be UNKNOWN_CLASS"

        if (classUiPb.sectionType != UNKNOWN_SECTION):
            classPb.sectionType = classUiPb.sectionType
        else:
            assert True, "Section type  Cannot be UNKNOWN_SECTION"

        if (Strings.notEmpty(classUiPb.schoolRef.id)):
            self.m_schooRefUpdator.refUpdator(schoolPbRef=classPb.schoolRef, schoolUiPbRef=classUiPb.schoolRef)
        else:
            raise Exception('Class Must have School Ref' + MessageToJson(classUiPb))

        if (Strings.notEmpty(classUiPb.classCode)):
            classPb.classCode = classUiPb.classCode
        else:
            classPb.classCode = self.m_classHelper.getClassCode(schoolCode=classUiPb.schoolRef.schoolCode,
                                                                id=classUiPb.dbInfo.id)
        if (classUiPb.createdtime.milliseconds > 0):
            self.m_timeUpdator.update(pb=classPb.createdTime, uipb=classUiPb.createdtime)
        else:
            self.m_timeUpdator.update(pb=classPb.time,
                                      uipb=self.m_timeUtility.getTimeUiPb(timeUiPb=classUiPb.time,
                                                                          timeZone=classUiPb.dbInfo.locale.default))
