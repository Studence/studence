from Comparetor.EnityPbComparetor import EntityPbComparetor
from Comparetor.NamePbComparetor import NamePbComapretor
from Comparetor.TimePbComparetor import TimePbComparetor


class OrganisationComparetor:
    m_entityComparetor = EntityPbComparetor()
    m_nameComparetor = NamePbComapretor()
    m_timeComparetor = TimePbComparetor()

    def compare(self, newPb, oldPb):
        self.m_entityComparetor.compare(newPb=newPb.dbInfo, oldPb=oldPb.dbInfo)
        self.m_nameComparetor.comapre(newpb=newPb.name, oldPb=oldPb.name)
        self.m_timeComparetor.comapre(newPb=newPb.time, oldPb=oldPb.time)
        return True
