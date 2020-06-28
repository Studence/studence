from Convertor.EntityPbConvertor import EntityPbConvertor
from Convertor.NamePbConvertor import NamePbConvertor


class GenericRefPbConvertor:
    m_entityPbConvertor = EntityPbConvertor()
    m_namePbConvertor = NamePbConvertor()

    def convert(self, uipb, pb):
        uipb.id = pb.id
        self.m_namePbConvertor.convert(uipb=uipb.name, pb=pb.name)
        uipb.code = pb.code
