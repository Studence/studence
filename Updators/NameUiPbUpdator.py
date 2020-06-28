from CommonCode.List.List import List
from CommonCode.strings import Strings


class NameUipbUpdator:

    def update(self, pb, uipb):
        pb.firstName = Strings.toLower(uipb.firstName)
        pb.middleName.extend(self.getMiddleNames(uipb.middleName))
        pb.lastName = Strings.toLower(uipb.lastName)
        pb.canonicalName = Strings.toLower(uipb.canonicalName)
        return

    def getMiddleNames(self, list):
        middleNammesList = List()
        middleNammesList.clear()
        for names in list:
            middleNammesList.__append__(names.lower())
        return middleNammesList
