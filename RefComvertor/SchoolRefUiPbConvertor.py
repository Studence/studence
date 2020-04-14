from CommonCode.strings import Strings
from Convertor.GenericRefPbConvertor import GenericRefPbConvertor


class SchoolRefUiPbConvertor:
    m_genericRefConvertor = GenericRefPbConvertor()

    def refConvertor(self, schoolUiPbRef, schoolPbRef):
        if (Strings.notEmpty(schoolPbRef.id)):
            schoolUiPbRef.id = schoolPbRef.id
        else:
            return

        self.m_genericRefConvertor.convert(pb=schoolPbRef.organisation, uipb=schoolUiPbRef.organisation)
        schoolUiPbRef.schoolCode = schoolPbRef.schoolCode
        if (len(schoolPbRef.classType) > 0):
            for classType in schoolPbRef.classType:
                schoolUiPbRef.classType.append(classType)
        else:
            raise Exception('School at least at least have one classes')

        if (len(schoolPbRef.sectionType) > 0):
            for sectionType in schoolPbRef.sectionType:
                schoolUiPbRef.sectionType.append(sectionType)
        else:
            raise Exception('School at least at least have one section')
