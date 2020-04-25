from BaseCodeModule.BasicPbIndexGenreator import BasicPbIndexGenreator
from OrganisationModule.OrganisationConfig import OrganisationConfig


class OrganisationPbGenreator(BasicPbIndexGenreator):

    def genreateToPb(self, pb):
        map = self.genereate(pb=pb)
        map.put(OrganisationConfig.MILLISECONDS.value, pb.time.milliseconds)
        return map
