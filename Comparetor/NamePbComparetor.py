from google.protobuf.json_format import MessageToJson

from CommonCode.strings import Strings


class NamePbComapretor:

    def comapre(self,newpb,oldPb):
        if(Strings.notEmpty(oldPb.firstName)):
            if(Strings.notEmpty(newpb.firstName)):
                pass
            else:
                raise Exception('First Name Is Empty' + MessageToJson(newpb))

        if(len(newpb.middleName)>0):
            if(len(oldPb.middleName)>0):
                pass
            else:
                raise Exception('MiddleName Is Empty' + MessageToJson(newpb))

        if(Strings.notEmpty(oldPb.lastName)):
            if(Strings.notEmpty(oldPb.lastName)):
                pass
            else:
                raise Exception('lastName Is Empty' + MessageToJson(newpb))

        if(Strings.notEmpty(newpb.canonicalName)):
            if(Strings.notEmpty(oldPb.canonicalName)):
                pass
            else:
                raise Exception('canonicalName Is Empty' + MessageToJson(newpb))
