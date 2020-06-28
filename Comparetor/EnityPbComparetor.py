from google.protobuf.json_format import MessageToJson

from CommonCode.strings import Strings
from Protobuff.entityUiPb_pb2 import UNKNOWN_STATUS
from Protobuff.timeUiPb_pb2 import UNKNOWN_TIME_ZONE


class EntityPbComparetor:

    def compare(self, newPb, oldPb):
        if (Strings.notEmpty(oldPb.id)):
            if (Strings.notEmpty(newPb.id)):
                if (Strings.areEquals(str1=oldPb.id, str2=newPb.id)):
                    oldPb.id = newPb.id
                else:
                    raise Exception('DbInfo id deffers in pbs' + MessageToJson(newPb) + " " + MessageToJson(oldPb))
            else:
                assert True, "id Cannot be Empty"
        else:
            assert True, "id Cannot be Empty"

        if (oldPb.version > 0):
            if (newPb.version > 0):
                if (oldPb.version < newPb.version):
                    oldPb.version = newPb.version
                else:
                    raise Exception(
                        'Version of new pb is should be greator then old' + MessageToJson(newPb) + " " + MessageToJson(
                            oldPb))
            else:
                assert True, "version cant be zero"
        else:
            assert True, "version cant be zero"

        if (oldPb.lifeTime != UNKNOWN_STATUS):
            if (newPb.lifeTime != UNKNOWN_STATUS):
                oldPb.lifeTime = newPb.lifeTime
            else:
                raise Exception('Status Cannot be UNKOWN_STATUS' + MessageToJson(newPb))
        else:
            raise Exception('Status Cannot be UNKOWN_STATUS' + MessageToJson(newPb))

        if (oldPb.locale.defaultTimeZone != UNKNOWN_TIME_ZONE):
            if (newPb.locale.defaultTimeZone != UNKNOWN_TIME_ZONE):
                oldPb.locale.defaultTimeZone = newPb.locale.defaultTimeZone
            else:
                raise Exception('TimeZone Cannot be UNKOWN_TIME_ZONE' + MessageToJson(newPb))
        else:
            raise Exception('TimeZone Cannot be UNKOWN_TIME_ZONE' + MessageToJson(newPb))
