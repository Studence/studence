from google.protobuf.json_format import MessageToJson

from CommonCode.List.List import List
from CommonCode.strings import Strings
from Protobuff.mobileUiPb_pb2 import UNKNOWN_CODE


class MobileComparetor:

    def compare(self, newpb, oldPb):
        if (oldPb.code != UNKNOWN_CODE):
            if (newpb.code != UNKNOWN_CODE):
                oldPb.code = newpb.code
            else:
                raise Exception('Code Cannot be UNKNOWN_CODE' + MessageToJson(newpb))
        if (Strings.notEmpty(oldPb.number)):
            if (Strings.notEmpty(newpb.number)):
                oldPb.number = newpb.number
            else:
                raise Exception('Number Cannot be Empty' + MessageToJson(newpb))




