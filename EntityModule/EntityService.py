from EntityModule.EntityServiceCF import EntityServiceCF


class EntityService:
    m_entityServiceCf = EntityServiceCF()

    def getEntityId(self):
        self.m_entityServiceCf.start()
        return self.m_entityServiceCf.done()
