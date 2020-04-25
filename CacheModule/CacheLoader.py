from cacheout import Cache


class CacheLoader(Cache):
    m_service = None

    def __init__(self, service):
        super(CacheLoader, self).__init__(ttl=1000)
        self.m_service = service

    def checked(self, id):
        try:
            data = self.get(key=id)
            if (data == None):
                raise Exception()
            return data
        except:
            self.set(key=id, value=self.m_service.get(id))
            return self.get(key=id)
