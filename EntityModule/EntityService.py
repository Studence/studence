from EntityModule.EnityChangeHandler import EntityChangeHandler
from EntityModule.EntityTableName import EntityTableName
from EntityModule.EntityUpdateListner import EntityTableUpdateListner


class EntityService:
    m_entityService = EntityTableUpdateListner(EntityChangeHandler(EntityTableName()))

    def getEntityId(self):
        return self.m_entityService.listenUpdate()
