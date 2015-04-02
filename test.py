from pysimplesoap.client import SoapClient
client = SoapClient(wsdl="http://41.208.68.195:4321/LcraHnecIntegrationService.svc?wsdl",trace=False)
# response = client.AddIntegers(a=1,b=2)
# result = response['AddResult']
subscriberId = ""
securityToken =[]

guid = client.OpenSession(subscriberId,securityToken)


gnonls



if (client):
	print True