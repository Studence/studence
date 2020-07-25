from BaseCodeModule.BaseService import BaseService
from LoginModule.LoginComparetor import LoginComparetor
from LoginModule.LoginConvertor import LoginConvertor
from LoginModule.LoginTableName import LoginTableName
from LoginModule.LoginUpdateListner import LoginUpdateListner
from LoginModule.LoginUpdator import LoginUpdator
from Protobuff.loginPb_pb2 import LoginPb


class LoginService(BaseService):

    def __init__(self):
        super(LoginService, self).__init__(LoginPb(), LoginUpdator(), LoginConvertor(),
                                                  LoginComparetor(), LoginUpdateListner(),
                                                  LoginTableName())

    def create(self, LoginUiPb):
        return self.createEntity(uipb=LoginUiPb)

    def get(self, id):
        return self.getEntity(id=id)

    def update(self, id, LoginUipb):
        return self.updateEntity(id=id, uipb=LoginUipb)

    #def search(self, LoginSearchRequestUipb):
        #return self.m_aSearchEntity.search(reqUipb=LoginSearchRequestUipb)
