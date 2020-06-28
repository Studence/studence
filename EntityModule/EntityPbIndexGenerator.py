from enum import Enum

from CommonCode.HashMap.HashMap import HashMap


class EntityIndexPbEnum(Enum):
    ID = 'ID'


class EntityPbIndexGenerator:

    def genreateToPb(self, id):
        map = HashMap()
        map.clear()
        map.put(EntityIndexPbEnum.ID.value, id)
        return map
