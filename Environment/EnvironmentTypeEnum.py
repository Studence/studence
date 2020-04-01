from enum import Enum


class EnvironmentTypeEnum(Enum):
    UNKNOWN_ENV = 0
    DEVEL = 1,
    PROD = 5,

    @staticmethod
    def getEnum(name):
       return EnvironmentTypeEnum.__getattr__(name=name)
