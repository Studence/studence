from enum import Enum


class ClassConfig(Enum):
    MILLISECONDS = 'Milliseconds'
    CLASS_TYPE = 'ClassType'
    SECTION_TYPE = 'SectionType'
    SCHOOL_ID = 'SchoolId'
    ORGANISATION_ID = 'OrganisationId'
    CLASS_CODE = 'ClassCode'


    @staticmethod
    def list():
        return list(map(lambda c: c.value, ClassConfig))
