from pysimplesoap.client import SoapClient
client = SoapClient(wsdl="http://41.208.68.195:4321/LcraHnecIntegrationService.svc?wsdl",trace=False)
# response = client.AddIntegers(a=1,b=2)
# result = response['AddResult']
subscriberId = ""
securityToken =[]
import MySQLdb
def connect():
  db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                      passwd="102030", # your password
                      db="py") # name of the data base
  return db.cursor() 




cur = connect()
# Use all the SQL you like
cur.execute("SELECT * FROM LibyanCitizens")

# print all the first cell of all the rows
for row in cur.fetchall() :
    print row[0]

# guid = client.OpenSession(subscriberId,securityToken)


if (client):
  print True
def insert(guid):
  no_libyan= GetNoOfNewLibyanCitizens(guid)
  list_libyan=GetNewLibyanCitizensNextBatch(guid)
  cur = connect()
  cur.execute("INSERT INTO `batchId`(`id_batch`, `id_session`) VALUES (%s,%s)",(list_libyan.ID,guid))
  cur.execute("INSERT INTO `LibyanCitizens` SET %s ",(list_libyan.List))
  AcknowledgeNewLibyanCitizensBatchReceived(guid, list_libyan.ID)
  cur.execute("UPDATE `batchId` SET `Acknowledge`=1 WHERE `id_batch`= %s AND `id_session`= %s",(list_libyan.ID,guid))



