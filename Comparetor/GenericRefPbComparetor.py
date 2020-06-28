from google.protobuf.json_format import MessageToJson

from CommonCode.strings import Strings
from Comparetor.EnityPbComparetor import EntityPbComparetor
from Comparetor.NamePbComparetor import NamePbComapretor


class GenericRefPbComparetor:
    m_entityPbComparetor = EntityPbComparetor()
    m_namePbComparetor = NamePbComapretor()

    def compare(self, newPb,oldPb):
        if(Strings.notEmpty(oldPb.id)):
            if(Strings.notEmpty(newPb.id)):
                oldPb.id=newPb.id
            else:
                raise Exception('Id  Is Empty' + MessageToJson(newPb))
        self.m_namePbComparetor.comapre(newpb=newPb.name, oldPb=oldPb.name)
        if (Strings.notEmpty(oldPb.code)):
            if (Strings.notEmpty(newPb.code)):
                oldPb.code = newPb.code
            else:
                raise Exception('Code  Is Empty' + MessageToJson(newPb))

