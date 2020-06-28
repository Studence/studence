from AWSModules.DynamoDbOpreationalModule.DynamoDbChangeHandler import DynamoDbChangeHandler
from AWSModules.SimpleDbOrpreationModule.SimpleDBChangeHandler import SimpleDbChangeHandler
from BaseCodeModule.UpdateListner import UpdateListner
from Protobuff.schoolPb_pb2 import SchoolPb
from SchoolModule.SchoolPbIndexGenreator import SchoolPbIndexGenreator
from SchoolModule.SchoolTableName import SchoolTableName


class SchoolUpdateListner(UpdateListner):
    
    def __init__(self):
        super(SchoolUpdateListner, self).__init__(SimpleDbChangeHandler(SchoolTableName(), SchoolPb(), SchoolPbIndexGenreator()),
            DynamoDbChangeHandler(SchoolTableName(), SchoolPb(), SchoolPbIndexGenreator()))

    def updateListen(self, pb):
        self.listenUpdate(pb=pb)
