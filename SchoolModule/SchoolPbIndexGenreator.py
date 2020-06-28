from BaseCodeModule.BasePbIndexGenreator import BasePbIndexGenreator
from Protobuff.accountDetailsUiPb_pb2 import AccountUseTypeEnum
from SchoolModule.SchoolConfig import SchoolConfig


class SchoolPbIndexGenreator(BasePbIndexGenreator):


    def genreateToPb(self, pb):
        map = self.genereate(pb=pb)
        map.put(SchoolConfig.MILLISECONDS.value, pb.createdTime.milliseconds)
        map.put(SchoolConfig.SCHOOL_CODE.value, pb.schoolCode)
        map.put(SchoolConfig.ORGANISATION_ID.value, pb.organisation.id)
        map.put(SchoolConfig.ACCOUNT_TYPE.value, AccountUseTypeEnum.Name(pb.accountUseType))
        return map
