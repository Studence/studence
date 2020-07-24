from enum import Enum


class StudentConfig(Enum):
    MILLISECONDS = 'Milliseconds'
    STUDENT_CODE = 'StudentCode'
    CLASS_ID = 'ClassId'
    SCHOOL_ID = 'SchoolId'
    ORGANISATION_ID ='OrganisationId'

    @staticmethod
    def list():
        return list(map(lambda c: c.value, StudentConfig))
