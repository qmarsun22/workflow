from urllib.request import DataHandler
import requests
import json
import os
import sys
import glob
#def test():
#https://www.zoho.com/crm/developer/docs/api/v2/auth-request.html

def cleanup():
    # cleanup files if its more than 10 minutes
    dir=r"C:\Users\KumarSundaram\Downloads\self_client*.json"
    print(dir)
    for file in glob.glob(dir):
        print(f"removing the file {file}")
        os.remove(file)

def get_token():
    filepath=r"C:\Users\KumarSundaram\Downloads\self_client.json"
    f = open(filepath)
    data=json.load(f)
    f.close()
    return data


def insert_records():
    import requests
    import jsona

    url = 'https://www.zohoapis.com/crm/v2/Leads'

    headers = {
    'Authorization': 'Zoho-oauthtoken 1000.cef7bf1a6a4dc8bfe44447581b30bf07.ff117a6cdac8943595405883365833be',
    }

    #headers =  {"scope":["ZohoInvoice.fullaccess.all"],"expiry_time":1656472923084,"client_id":"1000.J6BMS9G17IDORUIU6L2Q1CEH93J3NX","client_secret":"8727c049c0d3966137e51f9b573d07a5bab79f8c73","code":"1000.cef7bf1a6a4dc8bfe44447581b30bf07.ff117a6cdac8943595405883365833be","grant_type":"authorization_code"}

    
#1000.cef7bf1a6a4dc8bfe44447581b30bf07.ff117a6cdac8943595405883365833be

    request_body = dict()
    record_list = list()

    record_object_1 = {
        'Company': 'Zylker',
        'Email': 'p.daly@zylker.com',
        'Last_Name': 'Daly',
        'First_Name': 'Paul',
        'Lead_Status': 'Contacted',
    }

    record_object_2 = {
        'Last_Name': 'Dolan',
        'First_Name': 'Brian',
        'Email': 'brian@villa.com',
        'Company': 'Villa Margarita'
    }

    record_list.append(record_object_1)

    record_list.append(record_object_2)

    request_body['data'] = record_list

    trigger = [
        'approval',
        'workflow',
        'blueprint'
    ]

    request_body['trigger'] = trigger

    response = requests.post(url=url, headers=headers, data=json.dumps(request_body).encode('utf-8'))
    print('response ',response)
    if response is not None:
        print("HTTP Status Code : " + str(response.status_code))

        print(response.json())

#insert_records()

def write_refresh_access_token(jsonmsg):
    print("test")

def get_refresh_access_token(key):
    print(f"get_refresh_access_token {key}")
    apiUrl = "https://accounts.zoho.com/oauth/v2/token"
    r = requests.post(url=apiUrl, data=key )
    print(r)
    print('gen tocken', r.json())
    response=r.json()
    accesss_token = response["access_token"]
    refresh_token = response["refresh_token"]
    print(f'access tokenn {accesss_token}')
    print(f'refrsh token {refresh_token}')
    return(accesss_token,refresh_token)

def get_invoice(auth_token,client_id):
    print("get invoice")
    print(f"auth tokent {auth_token}")
    auth_token=f"Zoho-oauthtoken {auth_token}"
    invoice_orgid="784564479"
   # auth_token=f"Zoho-oauthtoken {auth_token}"
    auth_token=f"{auth_token}"
    myheader = {"X-com-zoho-invoice-organizationid":invoice_orgid , 
               "Authorization": auth_token}
    print(f"my header {myheader}")
    apiurl=f"https://invoice.zoho.com/api/v3/invoices"
    print(f"get apiurl {apiurl}")
    r = requests.get(apiurl, headers=myheader )
    print(r)
    print('get_invoice', r.json())



def gen_oath_token():
        a=1
#https://accounts.zoho.com/oauth/v2/token?
#/////////////// main

#$ curl https://inventory.zoho.com/api/v1/organizations?authtoken=ba4604e8e433g9c892e360d53463oec5

print(sys.argv[1])
if(sys.argv[1] == "clean"):
    print("ZohoInvoice.fullaccess.all")
    print("https://api-console.zoho.com/")
    cleanup()
    sys.exit()


key=get_token()

#download the api key
#https://api-console.zoho.com/
# 'ZohoInvoice.invoices.READ
print(key)

(access , refresh) = get_refresh_access_token(key)
# if you get once then try to reuse it.
client_id = key["client_id"]
print(f"client id {client_id}")
get_invoice(access,client_id)
#https://www.zoho.com/invoice/api/v3/introduction/


#invoices	To access invoices related APIs
#Availabe types: ZohoInvoice.invoices.Create, 
#ZohoInvoice.invoices.UPDATE, ZohoInvoice.invoices.READ, 
#ZohoInvoice.invoices.DELETE

sys.exit(0)
#///////////////////////////////
#     

#stockname, lastclosedprice, date
#adsf, 23.23 20220622
#bcd, 234.34, 20220622
#...
##...
#...
#===========================
#==>
#endofdayprice =
#[
#    {
#        stickname=
#        lastclosedprice
#        date
#    },
#    {
#    }
#]
#//////////////////
# readfile line by line
# eachline split into variable
# varibale insert to arrayofdict values

#1000.J6BMS9G17IDORUIU6L2Q1CEH93J3NX
#8727c049c0d3966137e51f9b573d07a5bab79f8c73


inputdata={
    "scope": [
        "ZohoInvoice.fullaccess.all"
    ],
    "expiry_time": 1657392537271,
    "client_id": "1000.WID2UB353SXAIEJP81M3J45A99Z7KM",
    "client_secret": "f86f51a04635fd237f210ea9b10cedaa18e7e0262e",
    "code": "1000.a47f34684868e1e6b7f75c5ed18bd10d.69735a355031d7d6ae047b372887bdf8",
    "grant_type": "authorization_code"
}
print(input)
#apiUrl = "https://accounts.zoho.com/oauth/v2/token"
#r = requests.post(url=apiUrl, data=inputdata )
#print(r)
#print('gen tocken', r.json())
#response=r.json()
#print('access tokenn',response["access_token"])
#print('refrsh token',response["refresh_token"])

#access tokenn 1000.65f878fd31be79273be8078622fb86de.56c5d422e77b7243d0a37d27f4673273
#refrsh token 1000.150aecb1ea3b402e998e88614c00a8dc.08ec4987fd12a09bd3c29fe449ef5016
Accounts_URL="https://accounts.zoho.com"
refresh_token="1000.150aecb1ea3b402e998e88614c00a8dc.08ec4987fd12a09bd3c29fe449ef5016"
client_id="1000.150aecb1ea3b402e998e88614c00a8dc.08ec4987fd12a09bd3c29fe449ef5016"
client_secret="f86f51a04635fd237f210ea9b10cedaa18e7e0262e"

apiurl=f"{Accounts_URL}/oauth/v2/token?refresh_token={refresh_token}&client_id={client_id}&client_secret={client_secret}&grant_type=refresh_token"
print(apiurl)


apiurl="https://accounts.zoho.com/oauth/v2/auth?"\
"scope=ZohoInvoice.fullaccess.all"\
"&client_id=1000.0SRSZSY37WMZ69405H3TMYI2239V"\
"&state=testing"\
"&response_type=code&redirect_uri=http://www.zoho.com/invoice&access_type=offline"
#print(apiurl)
#r = requests.post(url=apiurl )
#print(r)
#print(r.json())
#with open('zomooutput.html', 'w') as f:
#    f.write(str(r))

# generate access and refresh tokem
#https://accounts.zoho.com/oauth/v2/token?code=1000.dd7e47321d48b8a7e312e3d6eb1a9bb8.b6c07ac766ec11da98bf6a261e24dca4&client_id=1000.0SRSZSY37WMZ69405H3TMYI2239V&client_secret=fb0196010f2b70df8db2a173ca2cf59388798abf&redirect_uri=http://www.zoho.com/invoice&grant_type=authorization_code

#curl "https://www.zohoapis.com/crm/v2/Leads?converted=true&approved=true"
#-X GET
#-H "Authorization: Zoho-oauthtoken 1000.8cb99dxxxxxxxxxxxxx9be93.9b8xxxxxxxxxxxxxxxf"

#1000.cef7bf1a6a4dc8bfe44447581b30bf07.ff117a6cdac8943595405883365833be
apiurl="https://accounts.zoho.com/oauth/v2/token?"\
"gran_type=authorization_code" \
"&client_id=1000.J6BMS9G17IDORUIU6L2Q1CEH93J3NX"\
"&client_secret=8727c049c0d3966137e51f9b573d07a5bab79f8c73"\
"&redirect_uri=http://www.zoho.com/invoice&access_type=offline"
#print(apiurl)
#r = requests.post(url=apiurl )
#print(r)
#print(r.json())

# crm
# campaigns
# connect 
# work drive 
  # (Grant workflow)

#////////////////////
# Quickbooks==>
#///////////////////
#HTML, CSS,Javascript
#Monday, zoho and Quickbooks , local files
#===================

#https://www.zoho.com/crm/developer/docs/api/v2/
#https://www.zoho.com/crm/developer/docs/api/v2/auth-request.html

#//////////////////'a

#https://api-console.zoho.com/

#input_data={"scope":["ZohoInvoice.fullaccess.all"],"expiry_time":1656589263315,"client_id":"1000.J6BMS9G17IDORUIU6L2Q1CEH93J3NX","client_secret":"8727c049c0d3966137e51f9b573d07a5bab79f8c73","code":"1000.9f9f0ecab56de6bf6a9acf80b5dd9c61.a22ee090cf1ccd6436c5e8ada394f22e","grant_type":"authorization_code"}
input_data={"scope":["ZohoInvoice.fullaccess.all"],"expiry_time":1657277652783,"client_id":"1000.WID2UB353SXAIEJP81M3J45A99Z7KM","client_secret":"f86f51a04635fd237f210ea9b10cedaa18e7e0262e","code":"1000.0a554af1eea06fdf60700169f0a1664f.0f01c49f7f02b6ddd03b4aef60c11919","grant_type":"authorization_code"}
#input_data={"scope":["ZohoInvoice.fullaccess.all"],"expiry_time":1656617619965,"client_id":"1000.J6BMS9G17IDORUIU6L2Q1CEH93J3NX","client_secret":"8727c049c0d3966137e51f9b573d07a5bab79f8c73","code":"1000.0ea6c2f901116fa7eb80e8b8509d16d7.4fc0d967dbe9b89927c161aa1926e63f","grant_type":"authorization_code"}
apiUrl = "https://accounts.zoho.com/oauth/v2/token"
#r = requests.post(url=apiUrl, json=input_data )
#print(r)
#print('get oauth toketn', r.json())

apiurl="https://accounts.zoho.com/oauth/v2/token?"\
"gran_type=authorization_code" \
"&client_id=1004.9LW8H4GWNBNYRNRK5DU1FWAMFVMABY"\
"&client_secret=defe01477e14966693e03f0115874eaaed46b08eae"\
"&redirect_uri=http://www.zoho.com/invoice&access_type=offline"
#r = requests.post(url=apiUrl, json=input_data )
#print(r)
#print('token',r.json())
#1004.IUK6PUCO9RDV9OYCQQ5SWKZF8MNXBA
a
#8655f206e4d44ed68c090a4bcfc05e9a110b6a2075
