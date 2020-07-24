from BaseCodeModule.BasePbIndexGenreator import BasePbIndexGenreator
from CommonCode.strings import Strings
from LoginModule.LoginConfig import LoginConfig
from Protobuff.userTypeUiPb_pb2 import UserTypeEnum


class LoginPbIndexGenreator(BasePbIndexGenreator):

    def genreateToPb(self, pb):
        map = self.genereate(pb=pb)
        map.put(LoginConfig.MILLISECONDS.value, pb.time.milliseconds)
        map.put(LoginConfig.USER_EMAIL.value, Strings.getFormattedEmail(pb.email))
        map.put(LoginConfig.USER_ID.value, pb.userRef.id)
        map.put(LoginConfig.USER_TYPE.value, UserTypeEnum.Name(pb.userType.value))
        map.put(LoginConfig.USER_PASSWORD.value, pb.password)
        return map
