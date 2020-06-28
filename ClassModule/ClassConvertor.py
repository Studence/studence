from CommonCode.strings import Strings
from Convertor.EntityPbConvertor import EntityPbConvertor
from Convertor.NamePbConvertor import NamePbConvertor
from Convertor.TimePbConvertor import TimePbConvertor
from Protobuff.classTypeUiPb_pb2 import UNKNOWN_CLASS
from Protobuff.classUiPb_pb2 import ClassUiPb
from Protobuff.sectionUiPb_pb2 import UNKNOWN_SECTION
from RefComvertor.SchoolRefUiPbConvertor import SchoolRefUiPbConvertor


class ClassConvertor:
    m_entityPbConvertor = EntityPbConvertor()
    m_namePbConvertor = NamePbConvertor()
    m_timePbConvertor = TimePbConvertor()
    m_schoolRefConverotor = SchoolRefUiPbConvertor()

    def convert(self, classPb):
        classUiPb = ClassUiPb()
        if (Strings.notEmpty(classPb.dbInfo.id)):
            self.m_entityPbConvertor.convert(pb=classPb.dbInfo, uipb=classUiPb.dbInfo)
        if (Strings.notEmpty(classPb.name.firstName)):
            self.m_namePbConvertor.convert(pb=classPb.name, uipb=classUiPb.name)
        if (classPb.crteatedTime.milliseconds > 0):
            self.m_timePbConvertor.convert(pb=classPb.createdTime, uipb=classUiPb.createdTime)
        if (Strings.notEmpty(classPb.schoolCode)):
            classUiPb.schoolCode = classPb.schoolCode
        if (classPb.classType != UNKNOWN_CLASS):
            classUiPb.classType = classPb.classType
        if (classPb.sectionType != UNKNOWN_SECTION):
            classUiPb.sectionType = classPb.sectionType
        if (Strings.notEmpty(classPb.schoolRef.id)):
            self.m_schoolRefConverotor.refConvertor(schoolPbRef=classPb.schoolRef, schoolUiPbRef=classUiPb.schoolRef)
        return classUiPb
