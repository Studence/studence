from CommonCode.strings import Strings
from Updators.GenericRefUiPbUpdator import GenericRefUiPbUpdator


class SchoolRefUiPbUpdator:
    m_genericUpdator = GenericRefUiPbUpdator()

    def refUpdator(self, schoolPbRef, schoolUiPbRef):
        if (Strings.notEmpty(schoolUiPbRef.id)):
            schoolPbRef.id = schoolUiPbRef.id
        else:
            return

        if (Strings.notEmpty(schoolUiPbRef.organisation.id)):
            self.m_genericUpdator.update(pb=schoolPbRef.organisation, uipb=schoolUiPbRef.organisation)
        else:
            raise Exception('School must have his organisation' + schoolUiPbRef)

        if (Strings.notEmpty(schoolUiPbRef.schoolCode)):
            schoolPbRef.schoolCode = schoolUiPbRef.schoolCode

        if (len(schoolUiPbRef.classType) > 0):
            for classType in schoolUiPbRef.classType:
                schoolPbRef.classType.append(classType)
        else:
            raise Exception('School at least at least have one classes')

        if (len(schoolUiPbRef.sectionType) > 0):
            for sectionType in schoolUiPbRef.sectionType:
                schoolPbRef.sectionType.append(sectionType)
        else:
            raise Exception('School at least at least have one section')
