from enum import Enum


class AttendanceConfig(Enum):
    MILLISECONDS = 'Milliseconds'


    @staticmethod
    def list():
        return list(map(lambda c: c.value, AttendanceConfig))
