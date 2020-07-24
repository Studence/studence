from AWSModules.DynamoDbOpreationalModule.DynamoDbChangeHandler import DynamoDbChangeHandler
from AWSModules.SimpleDbOrpreationModule.SimpleDBChangeHandler import SimpleDbChangeHandler
from BaseCodeModule.UpdateListner import UpdateListner
from LoginModule.LoginPbIndexGenerator import LoginPbIndexGenreator
from LoginModule.LoginTableName import LoginTableName
from Protobuff.loginPb_pb2 import LoginPb


class LoginUpdateListner(UpdateListner):

    def __init__(self):
        super(LoginUpdateListner, self).__init__(
            SimpleDbChangeHandler(LoginTableName(), LoginPb(), LoginPbIndexGenreator()),
            DynamoDbChangeHandler(LoginTableName(), LoginPb(), LoginPbIndexGenreator()))

        def updateListen(self, pb):
            self.listenUpdate(pb=pb)
