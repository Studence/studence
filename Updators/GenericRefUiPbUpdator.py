from CommonCode.strings import Strings
from Updators.EntityUiPbUpdator import EntityUiPbUpdator
from Updators.NameUiPbUpdator import NameUipbUpdator


class GenericRefUiPbUpdator:
    m_entityUiPbUpdator = EntityUiPbUpdator()
    m_nameUipbUpdator = NameUipbUpdator()

    def update(self, pb, uipb):
        if (Strings.notEmpty(uipb.id)):
            pb.id = uipb.id
        self.m_nameUipbUpdator.update(uipb=uipb.name, pb=pb.name)
        pb.code = uipb.code
