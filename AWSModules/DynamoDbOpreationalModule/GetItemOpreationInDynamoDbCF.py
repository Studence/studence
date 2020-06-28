from enum import Enum

from switchlang import switch

from AWSModules.DynamoDbOpreationalModule.DynamoDbOpreationHelper import DynamoDbOpreationHelper
from AWSModules.DynamoDbOpreationalModule.GetKeyMapper import GetKeyMapper
from AWSModules.DynanoDbDatabaseModule.GetItemInDynamodb import GetItemInDynamodb
from CommonCode.convertJSONTOPb import ConvertJSONToPb
from CommonCode.strings import Strings
from CryptoModule.EncryptorAndDecryptor import EncryptorAndDecryptor


class State(Enum):
    CHECK_TABLE_IS_EMPTY = 0
    ID_IS_EMPTY = 1
    GET_ATTRIBUTES = 2
    DECODE_DATA = 3
    GENREATE_PB = 4
    DONE = 5


class GetItemOpreationInDynamoDbCF:
    m_table_name = None;
    m_id = None
    m_decodedData = None
    m_response = None
    m_pbInstance = None

    m_getAttribute = GetItemInDynamodb()
    m_dynamoDbOpreationHelper = DynamoDbOpreationHelper()
    m_decoder = EncryptorAndDecryptor()
    m_convertorPb = ConvertJSONToPb()
    m_keyMapper = GetKeyMapper()

    def __init__(self, table, pb):
        self.m_table_name = table
        self.m_pbInstance = pb

    def start(self, id):
        self.m_id = id
        self.controlFlow(currentState=State.CHECK_TABLE_IS_EMPTY)

    def done(self):
        return self.m_response

    def checkDominNameIsEmpty(self):
        if (Strings.isEmpty(self.m_table_name)):
            raise Exception("table name is Empty")
        else:
            self.controlFlow(currentState=State.ID_IS_EMPTY)

    def idIsEmpty(self):
        if (Strings.isEmpty(self.m_id)):
            raise Exception("Entity id is Empty")
        else:
            self.controlFlow(currentState=State.GET_ATTRIBUTES)

    def getAttribute(self):
        resp = self.m_getAttribute.get_item(tableName=self.m_table_name.tableName(),
                                            key=self.m_keyMapper.getKey(id=self.m_id,
                                                                        keyType=self.m_table_name.tableKeySchemaType()))
        if (resp == None):
            self.controlFlow(currentState=State.DONE)
        else:
            self.m_response = self.m_dynamoDbOpreationHelper.getRawData(resp)
            self.controlFlow(currentState=State.DECODE_DATA)

    def decodeData(self):
        self.m_decodedData = self.m_decoder.decode(chiperText=self.m_response)
        self.controlFlow(currentState=State.GENREATE_PB)

    def genreatePb(self):
        self.m_response = self.m_convertorPb.converjsontoPB(response=self.m_decodedData,
                                                            instanceType=self.m_pbInstance)
        self.controlFlow(currentState=State.DONE)

    def controlFlow(self, currentState):
        with switch(currentState) as s:
            s.case(State.CHECK_TABLE_IS_EMPTY, self.checkDominNameIsEmpty)
            s.case(State.ID_IS_EMPTY, self.idIsEmpty)
            s.case(State.GET_ATTRIBUTES, self.getAttribute)
            s.case(State.DECODE_DATA, self.decodeData)
            s.case(State.GENREATE_PB, self.genreatePb)
            s.case(State.DONE, self.done)
            s.default(self.done)
