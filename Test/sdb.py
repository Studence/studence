from AWSModules.SimpleDbModule.SimpleDbConnection import SimpleDbConnection

sdb = SimpleDbConnection()
resp = sdb.getConnection().get_attributes(
    DomainName='ENTITY_DEVEL',
ItemName = 'ID'
)
print(resp)
