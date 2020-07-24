from AWSModules.DynamoDbOpreationalModule.DynamoDbChangeHandler import DynamoDbChangeHandler
from AWSModules.SimpleDbOrpreationModule.SimpleDBChangeHandler import SimpleDbChangeHandler
from BaseCodeModule.UpdateListner import UpdateListner
from Protobuff.studentPb_pb2 import StudentPb
from StudentModule.StudentPbIndexGenerator import StudentPbIndexGenreator
from StudentModule.StudentTableName import StudentTableName


class StudentUpdateListner(UpdateListner):

    def __init__(self):
        super(StudentUpdateListner, self).__init__(
            SimpleDbChangeHandler(StudentTableName(), StudentPb(), StudentPbIndexGenreator()),
            DynamoDbChangeHandler(StudentTableName(), StudentPb(), StudentPbIndexGenreator()))

        def updateListen(self, pb):
            self.listenUpdate(pb=pb)
