class EntityQuery:
    BASE_QUERY = "SELECT * FROM"
    BASE_UPDATE_QUERY = "UPDATE"

    def getEntityQuery(self, data):
        return self.BASE_QUERY + ' "' + data + '"'

    def updateEntityQuery(self, data, value):
        return self.BASE_UPDATE_QUERY + ' "' + data + '"' + " SET dbid = " + value + " WHERE id = 1"
