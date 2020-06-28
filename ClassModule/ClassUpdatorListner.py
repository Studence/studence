from AWSModules.DynamoDbOpreationalModule.DynamoDbChangeHandler import DynamoDbChangeHandler
from AWSModules.SimpleDbOrpreationModule.SimpleDBChangeHandler import SimpleDbChangeHandler
from BaseCodeModule.UpdateListner import UpdateListner
from ClassModule.ClassPbIndexGenerator import ClassPbIndexGenerator
from ClassModule.ClassTableName import ClassTableName
from Protobuff.classPb_pb2 import ClassPb


class ClassUpdateListner(UpdateListner):

    def __init__(self):
        super(ClassUpdateListner, self).__init__(
            SimpleDbChangeHandler(ClassTableName(), ClassPb(), ClassPbIndexGenerator()),
            DynamoDbChangeHandler(ClassTableName(), ClassPb(), ClassPbIndexGenerator()))

        def updateListen(self, pb):
            self.listenUpdate(pb=pb)
