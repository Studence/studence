from enum import Enum


class EnvironmentTypeEnum(Enum):
    DEVEL = 0,
    PROD = 1,

    @staticmethod
    def getEnum(name):
       return EnvironmentTypeEnum.__getattr__(name=name)
