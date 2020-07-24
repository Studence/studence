from CommonCode.strings import Strings
from Protobuff.classTypeUiPb_pb2 import UNKNOWN_CLASS
from Protobuff.sectionUiPb_pb2 import UNKNOWN_SECTION
from RefUpdator.SchoolUiPbRefUpdatpr import SchoolRefUiPbUpdator


class ClassUiPbRefUpdator:

    m_schoolRefUpdator = SchoolRefUiPbUpdator()
    

    def refUpdator(self, classPbRef, classUiPbRef):
        if (Strings.notEmpty(classUiPbRef.id)):
            classPbRef.id = classUiPbRef.id
        else:
            return
        if(Strings.notEmpty(classUiPbRef.schoolRef.id)):
           self.m_schoolRefUpdator.refUpdator(classPbRef.schoolRef,classUiPbRef.schoolRef)
        else:
            raise Exception('class must have his school' + classUiPbRef)
        if(Strings.notEmpty(classUiPbRef.classCode)):
            classPbRef.classCode =classUiPbRef.classCode;
        else:
            raise Exception('class must have his Class Code' + classUiPbRef)
        if(classUiPbRef.classType != UNKNOWN_CLASS):
            classPbRef.classType =classUiPbRef.classType
        else:
            raise Exception('class must have his Class Type' + classUiPbRef)
        if(classUiPbRef.sectionType!=UNKNOWN_SECTION):
            classPbRef.sectionType = classUiPbRef.sectionType
        else:
           raise Exception('class must have his Section Type' + classUiPbRef)


