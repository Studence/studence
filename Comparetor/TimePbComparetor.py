from google.protobuf.json_format import MessageToJson

from CommonCode.strings import Strings
from Protobuff.timeUiPb_pb2 import UNKNOWN_TIME_ZONE


class TimePbComparetor:

    def comapre(self,newPb,oldPb):
        if(Strings.notEmpty(oldPb.date)):
            if(Strings.notEmpty(newPb.date)):
               oldPb.date = newPb.date
            else:
                raise Exception('Date Is Empty' + MessageToJson(newPb))

        if(Strings.notEmpty(oldPb.month)):
            if(Strings.notEmpty(newPb.month)):
                oldPb.month = newPb.month
            else:
                raise Exception('Month Is Empty' + MessageToJson(newPb))

        if(Strings.notEmpty(oldPb.year)):
            if(Strings.notEmpty(newPb.year)):
                oldPb.year = newPb.year
            else:
                raise Exception('Year Is Empty' + MessageToJson(newPb))

        if(newPb.milliseconds>0):
            if(oldPb.milliseconds>0):
                newPb.milliseconds = oldPb.milliseconds
            else:
                raise Exception('milliseconds cant be Zero' + MessageToJson(newPb))

        if(Strings.notEmpty(oldPb.formattedDate)):
            if(Strings.notEmpty(newPb.formattedDate)):
                oldPb.formattedDate = newPb.formattedDate
            else:
                raise Exception('Formatted date cant be Empty' + MessageToJson(newPb))

        if(oldPb.timezone!=UNKNOWN_TIME_ZONE):
            if(newPb.timezone!=UNKNOWN_TIME_ZONE):
                oldPb.timezone = newPb.timezone
            else:
                raise Exception('Time zone cannot be Unknown' + MessageToJson(newPb))
