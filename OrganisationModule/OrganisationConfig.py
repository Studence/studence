from enum import Enum


class OrganisationConfig(Enum):
    MILLISECONDS = 'Milliseconds'

    @staticmethod
    def list():
        return list(map(lambda c: c.value, OrganisationConfig))
