from AWSModules.DynamoDbOpreationalModule.DynamoDbChangeHandler import DynamoDbChangeHandler
from AWSModules.SimpleDbOrpreationModule.SimpleDBChangeHandler import SimpleDbChangeHandler
from BaseCodeModule.UpdateListner import UpdateListner
from OrganisationModule.OrganisationPbIndexGenerator import OrganisationPbGenreator
from OrganisationModule.OrganisationTableName import OrganisationTableName
from Protobuff.organisationPb_pb2 import OrganisationPb


class OrganisationUpdateListner(UpdateListner):

    def __init__(self):
        super(OrganisationUpdateListner, self).__init__(
            SimpleDbChangeHandler(OrganisationTableName(), OrganisationPb(), OrganisationPbGenreator()),
            DynamoDbChangeHandler(OrganisationTableName(), OrganisationPb(), OrganisationPbGenreator()))

        def updateListen(self, pb):
            self.listenUpdate(pb=pb)
