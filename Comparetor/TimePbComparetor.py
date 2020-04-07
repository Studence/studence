from google.protobuf.json_format import MessageToJson

from CommonCode.strings import Strings
from Protobuff.timeUiPb_pb2 import UNKNOWN_TIME_ZONE


class TimePbComparetor:

    def comapre(self,newPb,oldPb):
        if(Strings.notEmpty(oldPb.date)):
            if(Strings.notEmpty(newPb.date)):
                pass
            else:
                raise Exception('Date Is Empty' + MessageToJson(newPb))

        if(Strings.notEmpty(oldPb.month)):
            if(Strings.notEmpty(newPb.month)):
                pass
            else:
                raise Exception('Month Is Empty' + MessageToJson(newPb))

        if(Strings.notEmpty(oldPb.year)):
            if(Strings.notEmpty(newPb.year)):
                pass
            else:
                raise Exception('Year Is Empty' + MessageToJson(newPb))

        if(newPb.milliseconds>0):
            if(oldPb.milliseconds>0):
                pass
            else:
                raise Exception('milliseconds cant be Zero' + MessageToJson(newPb))

        if(Strings.notEmpty(oldPb.formattedDate)):
            if(Strings.notEmpty(newPb.formattedDate)):
                pass
            else:
                raise Exception('Formatted date cant be Empty' + MessageToJson(newPb))

        if(oldPb.timezone!=UNKNOWN_TIME_ZONE):
            if(newPb.timezone!=UNKNOWN_TIME_ZONE):
                pass
            else:
                raise Exception('Time zone cannot be Unknown' + MessageToJson(newPb))
