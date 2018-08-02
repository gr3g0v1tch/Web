#################################################################
#Objective: 
# Check robots.txt
#Description: 
# Test each entries in robots.txt
#Date:
# 02/08/2018
#################################################################

import requests

#clean the robots.txt file
#delete Allow and Disallow directive
infile = "robots.txt"
outfile = "cleaned_file.txt"

delete_list = ["Disallow: /", "Allow: /"]
fin = open(infile)
fout = open(outfile, "w+")

print("cleaning file...")
for line in fin:
    for word in delete_list:
        line = line.replace(word, "")
    fout.write(line)
fin.close()
fout.close()

cleanfile = "cleaned_file.txt"
fclean = open(cleanfile)

match='404 Not Found'

for entries in fclean:
        entries = entries.rstrip("\n")
        url = "http://192.168.0.7/%s" % entries
        request = requests.get(url).text
        if match not in request:
                print("UP: "+url)
