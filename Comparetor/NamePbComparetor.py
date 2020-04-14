from google.protobuf.json_format import MessageToJson

from CommonCode.strings import Strings


class NamePbComapretor:

    def comapre(self, newpb, oldPb):
        if (Strings.notEmpty(oldPb.firstName)):
            if (Strings.notEmpty(newpb.firstName)):
                oldPb.firstName = newpb.firstName
            else:
                raise Exception('First Name Is Empty' + MessageToJson(newpb))

        if (len(oldPb.middleName) > 0):
            if (len(newpb.middleName) > 0):
                del oldPb.middleName[:]
                oldPb.middleName.extend(newpb.middleName)
            else:
                raise Exception('MiddleName Is Empty' + MessageToJson(newpb))

        if (Strings.notEmpty(oldPb.lastName)):
            if (Strings.notEmpty(newpb.lastName)):
                oldPb.lastName = newpb.lastName
            else:
                raise Exception('lastName Is Empty' + MessageToJson(newpb))

        if (Strings.notEmpty(oldPb.canonicalName)):
            if (Strings.notEmpty(newpb.canonicalName)):
                oldPb.canonicalName = newpb.canonicalName
            else:
                raise Exception('canonicalName Is Empty' + MessageToJson(newpb))
