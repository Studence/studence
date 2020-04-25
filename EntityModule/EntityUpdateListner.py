from EntityModule.EntityTableName import EntityTableName
from EntityModule.EntityUpdateListnerCF import EnityUpdateListnerCF


class EntityTableUpdateListner():
    m_argsList = None

    def __init__(self, *args):
        self.m_argsList = args

    def listenUpdate(self):
        enityUpdateListnerCF = EnityUpdateListnerCF(self.m_argsList, EntityTableName())
        enityUpdateListnerCF.start()
        return enityUpdateListnerCF.done()
