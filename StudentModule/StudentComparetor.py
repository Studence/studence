from google.protobuf.json_format import MessageToJson

from CommonCode.strings import Strings
from Comparetor.EnityPbComparetor import EntityPbComparetor
from Comparetor.NamePbComparetor import NamePbComapretor
from Comparetor.TimePbComparetor import TimePbComparetor


class StudentComparetor:
    m_entityComparetor = EntityPbComparetor()
    m_nameComparetor = NamePbComapretor()
    m_timeComparetor = TimePbComparetor()

    def compare(self, newPb, oldPb):
        self.m_entityComparetor.compare(newPb=newPb.dbInfo, oldPb=oldPb.dbInfo)
        self.m_nameComparetor.comapre(newpb=newPb.name, oldPb=oldPb.name)
        self.m_timeComparetor.comapre(newPb=newPb.time, oldPb=oldPb.time)
        if (Strings.notEmpty(oldPb.orgCode)):
            if (Strings.notEmpty(newPb.orgCode)):
                oldPb.orgCode = newPb.orgCode
            else:
                raise Exception('OrgCode is missing' + MessageToJson(newPb))
        return oldPb
