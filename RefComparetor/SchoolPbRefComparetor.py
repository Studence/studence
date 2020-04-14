from google.protobuf.json_format import MessageToJson

from CommonCode.strings import Strings
from Comparetor.GenericRefPbComparetor import GenericRefPbComparetor
from Protobuff.classTypeUiPb_pb2 import UNKNOWN_CLASS
from Protobuff.sectionUiPb_pb2 import UNKNOWN_SECTION


class SchoolPbRefComparetor:
    m_genericRefComparetor = GenericRefPbComparetor()

    def refComparetor(self, newRefPb, oldRefPb):
        if (Strings.notEmpty(oldRefPb.id)):
            if (Strings.notEmpty(newRefPb.id)):
                oldRefPb.id = newRefPb.id
            else:
                raise Exception('Id cannot be empty' + MessageToJson(newRefPb))

        if (Strings.notEmpty(oldRefPb.organisation.id)):
            if (Strings.notEmpty(newRefPb.organisation.id)):
                self.m_genericRefComparetor.compare(newPb=newRefPb.organisation, oldPb=oldRefPb.organisation)
            else:
                raise Exception('organisation cannot be empty' + MessageToJson(newRefPb))

        if (Strings.notEmpty(oldRefPb.schoolCode)):
            if (Strings.notEmpty(newRefPb.schoolCode)):
                oldRefPb.schoolCode = newRefPb.schoolCode
            else:
                raise Exception('schoolCode cannot be empty' + MessageToJson(newRefPb))

        if (len(oldRefPb.classType) > 0):
            if (len(newRefPb.classType) > 0):
                del oldRefPb.classType[:]
                for classType in newRefPb.classType:
                    if (classType != UNKNOWN_CLASS):
                        oldRefPb.classType.append(classType)
                    else:
                        raise Exception('classType cannot be UNKNOWN_CLASS' + MessageToJson(newRefPb))
            else:
                raise Exception('classType list cannot be Empty' + MessageToJson(newRefPb))

        if (len(oldRefPb.sectionType) > 0):
            if (len(newRefPb.sectionType) > 0):
                del oldRefPb.sectionType[:]
                for sectionType in newRefPb.sectionType:
                    if (sectionType != UNKNOWN_SECTION):
                        oldRefPb.classType.append(sectionType)
                    else:
                        raise Exception('sectionType cannot be UNKNOWN_SECTION' + MessageToJson(newRefPb))
            else:
                raise Exception('sectionType list cannot be Empty' + MessageToJson(newRefPb))
