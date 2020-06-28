from BaseCodeModule.BasePbIndexGenreator import BasePbIndexGenreator
from OrganisationModule.OrganisationConfig import OrganisationConfig


class OrganisationPbIndexGenreator(BasePbIndexGenreator):

    def genreateToPb(self, pb):
        map = self.genereate(pb=pb)
        map.put(OrganisationConfig.MILLISECONDS.value, pb.time.milliseconds)
        map.put(OrganisationConfig.ORGANISATION_CODE.value, pb.orgCode)
        return map
