from CacheModule.CacheLoader import CacheLoader
from OrganisationModule.OrganisationService import OrganisationService


class OrganisationCache(CacheLoader):

    def __init__(self):
        super(OrganisationCache, self).__init__(service=OrganisationService())
