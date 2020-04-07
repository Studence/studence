from google.protobuf.json_format import MessageToJson

from CommonCode.strings import Strings
from Protobuff.entityUiPb_pb2 import UNKNOWN_STATUS
from Protobuff.timeUiPb_pb2 import UNKNOWN_TIME_ZONE


class EntityPbComparetor:

    def compare(self, newPb, oldPb):
        if (Strings.notEmpty(oldPb.id)):
            if (Strings.notEmpty(newPb.id)):
                if (Strings.areEquals(str1=oldPb.id, str2=newPb.id)):
                    pass
                else:
                    raise Exception('DbInfo id deffers in pbs' + MessageToJson(newPb) + " " + MessageToJson(oldPb))
            else:
                assert True, "id Cannot be Empty"
        else:
            assert True, "id Cannot be Empty"

        if (oldPb.lifeTime != UNKNOWN_STATUS):
            if (newPb.lifeTime != UNKNOWN_STATUS):
                pass
            else:
                raise Exception('Status Cannot be UNKOWN_STATUS' + MessageToJson(newPb))
        else:
            raise Exception('Status Cannot be UNKOWN_STATUS' + MessageToJson(newPb))

        if (oldPb.locale.defaultTimeZone != UNKNOWN_TIME_ZONE):
            if (newPb.locale.defaultTimeZone != UNKNOWN_TIME_ZONE):
                return True
            else:
                raise Exception('TimeZone Cannot be UNKOWN_TIME_ZONE' + MessageToJson(newPb))
        else:
            raise Exception('TimeZone Cannot be UNKOWN_TIME_ZONE' + MessageToJson(newPb))
