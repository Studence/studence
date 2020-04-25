from enum import Enum

from CommonCode.HashMap.HashMap import HashMap
from CommonCode.JsonFormatter import JsonFormatter
from CryptoModule.EncryptorAndDecryptor import EncryptorAndDecryptor
from Protobuff.entityUiPb_pb2 import StatusEnum


class BasicEntityIndex(Enum):
    RAW_DATA = 'RAW_DATA'
    LIFETIME = 'LIFETIME'

    @staticmethod
    def list():
        return list(map(lambda c: c.value, BasicEntityIndex))


class BasicPbIndexGenreator:
    m_encoder = EncryptorAndDecryptor()

    def genereate(self, pb):
        hashMap = HashMap()
        hashMap.clear()
        try:
            hashMap.put(BasicEntityIndex.RAW_DATA.value,
                        self.m_encoder.encode(plainText=JsonFormatter.printToString(pb)))
            hashMap.put(BasicEntityIndex.LIFETIME.value, StatusEnum.Name(pb.dbInfo.lifeTime))
            return hashMap
        except:
            pass
            return None
