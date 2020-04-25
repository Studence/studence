from CommonCode.strings import Strings
from RefUpdator.SchoolUiPbRefUpdatpr import SchoolRefUiPbUpdator


class ClassUiPbRefUpdator:

    m_schoolRefUpdator = SchoolRefUiPbUpdator()
    

    def refUpdator(self, classPbRef, classUiPbRef):
        if (Strings.notEmpty(classUiPbRef.id)):
            classPbRef.id = classUiPbRef.id
        else:
            return


