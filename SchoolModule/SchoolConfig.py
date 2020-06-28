from enum import Enum


class SchoolConfig(Enum):
    MILLISECONDS = 'Milliseconds'
    SCHOOL_CODE = 'SchoolCode'
    ORGANISATION_ID = 'OrganisationId'
    ACCOUNT_TYPE = 'AccountType'

    @staticmethod
    def list():
        return list(map(lambda c: c.value, SchoolConfig))
