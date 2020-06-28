from enum import Enum


class OrganisationConfig(Enum):
    MILLISECONDS = 'Milliseconds'
    ORGANISATION_CODE = 'OrganisationCode'

    @staticmethod
    def list():
        return list(map(lambda c: c.value, OrganisationConfig))
