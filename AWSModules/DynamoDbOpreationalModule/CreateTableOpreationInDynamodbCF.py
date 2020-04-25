import copy
from enum import Enum

from switchlang import switch

from AWSModules.DynamoDbOpreationalModule.DynamoDbOpreationHelper import DynamoDbOpreationHelper
from AWSModules.DynanoDbDatabaseModule.AttributeDefinationsMapper import AttributeDefinationsMapper
from AWSModules.DynanoDbDatabaseModule.CreateTableInDynamodb import CreateTableInDynamoDb
from AWSModules.DynanoDbDatabaseModule.KeySchemaMapper import KeySchemaMapper
from CommonCode.List.List import List
from CommonCode.strings import Strings
from Environment.EnvironmentTypeEnum import EnvironmentTypeEnum


class State(Enum):
    CHECK_TABLE_NAME = 0;
    GET_KEY_SCHEMA = 1
    GET_ATTRIBUTE_TYPE = 2
    CREATE_TABLE = 3
    DONE = 4;


class CreateTableOpreationInDynamodbCF:
    m_TableName = None;
    m_keyType = None
    m_keySchema = None
    m_attributeType = None
    m_createTable = CreateTableInDynamoDb()
    m_dynamoDbOpreationHeper = DynamoDbOpreationHelper()
    m_keySchemaMapper = KeySchemaMapper()
    m_attributeMapper = None

    def __init__(self, keyType, config):
        self.m_keyType = keyType
        self.m_attributeMapper = AttributeDefinationsMapper(config)

    def start(self, tableName):
        self.m_TableName = tableName
        self.controlFlow(currentState=State.CHECK_TABLE_NAME)

    def done(self):
        return

    def checkTableNameIsEmpty(self):
        if (Strings.isEmpty(self.m_TableName)):
            raise Exception("table name is Empty")
        else:
            self.controlFlow(currentState=State.GET_KEY_SCHEMA)

    def keySchema(self):
        self.m_keySchema = copy.copy(self.m_keySchemaMapper.keyMapper(keyType=self.m_keyType))
        if (self.m_keySchema == None):
            raise Exception("Error while Building key Schema")
        else:
            self.controlFlow(currentState=State.GET_ATTRIBUTE_TYPE)

    def attributeType(self):
        self.m_attributeType = self.m_dynamoDbOpreationHeper.getAttributeList(self.m_keySchema,self.m_attributeMapper.attributeMapper(),self.m_keyType)
        if (self.m_attributeType == None):
            raise Exception("Error while Building Attribute")
        else:
            self.controlFlow(currentState=State.CREATE_TABLE)

    def createTable(self):
        for env in EnvironmentTypeEnum:
            self.m_createTable.createTable(
                self.m_dynamoDbOpreationHeper.getTableName(tableName=self.m_TableName, eviornment=env),
                keySchemaList=self.m_keySchema, AttributeDefinitionList=self.m_attributeType)

    def controlFlow(self, currentState):
        with switch(currentState) as s:
            s.case(State.CHECK_TABLE_NAME, self.checkTableNameIsEmpty)
            s.case(State.GET_KEY_SCHEMA, self.keySchema)
            s.case(State.GET_ATTRIBUTE_TYPE, self.attributeType)
            s.case(State.CREATE_TABLE, self.createTable)
            s.case(State.DONE, self.done)
            s.default(self.done)
