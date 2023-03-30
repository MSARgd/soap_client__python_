from suds.client import Client
if __name__ == '__main__':
    url_wsdl = "http://localhost:8089/BanqueWS?wsdl"
    client = Client(url_wsdl)
    result = client.service.ConversationEuroToDh(100)
    print(result)
    compte = client.service.getCompte(1)
    comptes = client.service.getAllComptes()
    for i in range(0,len(comptes)) :
        print("code : "+str(comptes[i].code)+"  solde : "+str(comptes[i].solde))


