from CacheModule.CacheLoader import CacheLoader


class LoginCache(CacheLoader):

    def __init__(self):
        super(LoginCache, self).__init__(service=LoginService())
