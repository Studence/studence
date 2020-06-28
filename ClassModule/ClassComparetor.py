from google.protobuf.json_format import MessageToJson

from CommonCode.strings import Strings
from Comparetor.EnityPbComparetor import EntityPbComparetor
from Comparetor.NamePbComparetor import NamePbComapretor
from Comparetor.TimePbComparetor import TimePbComparetor
from Protobuff.classTypeUiPb_pb2 import UNKNOWN_CLASS
from Protobuff.sectionUiPb_pb2 import UNKNOWN_SECTION
from RefComvertor.SchoolRefUiPbConvertor import SchoolRefUiPbConvertor


class ClassComparetor:
    m_entityComparetor = EntityPbComparetor()
    m_nameComparetor = NamePbComapretor()
    m_timeComparetor = TimePbComparetor()
    m_schoolRefComparetor = SchoolRefUiPbConvertor()


def compare(self, newPb, oldPb):
    self.m_entityComparetor.compare(newPb=newPb.dbInfo, oldPb=oldPb.dbInfo)
    self.m_nameComparetor.comapre(newpb=newPb.name, oldPb=oldPb.name)
    self.m_timeComparetor.comapre(newPb=newPb.createdTime, oldPb=oldPb.createdTime)
    if (oldPb.classType != UNKNOWN_CLASS):
        if (newPb.classType != UNKNOWN_CLASS):
            oldPb.classType = newPb.classType
        else:
            raise Exception('classType is missing' + MessageToJson(newPb))
    if (oldPb.sectionType != UNKNOWN_SECTION):
        if (newPb.sectionType != UNKNOWN_SECTION):
            oldPb.sectionType = newPb.sectionType
        else:
            raise Exception('sectionType is missing' + MessageToJson(newPb))
    if (Strings.notEmpty(oldPb.schoolRef.id)):
        if (Strings.notEmpty(newPb.schoolRef.id)):
            self.m_schoolRefComparetor.refConvertor(schoolPbRef=oldPb.schoolRef, schoolUiPbRef=newPb.schoolRef)
        else:
            raise Exception('schoolRef is missing' + MessageToJson(newPb))
    if (Strings.notEmpty(oldPb.classCode)):
        if (Strings.notEmpty(newPb.classCode)):
            oldPb.classCode = newPb.classCode
        else:
            raise Exception('classCode is missing' + MessageToJson(newPb))
    return oldPb
