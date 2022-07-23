""" This is for get a sha265 hash of a file """

from functools import cache
import json

import requests

url = "https://www.virustotal.com/api/v3/files/"

headers = {
    "Accept": "application/json",
    "x-apikey": "64857d0f2d98c1be3d940966278b4577ffc957cc579ab62a6d919babb79cd987"
}

  
  
file1 = open('md5.txt', 'r')
Lines = file1.readlines()
  
writenTxt =""

f=open('sha256.txt', 'w')
s=open('cannnotFind.txt', 'w')
# Strips the newline character
for line in Lines:
    subUrl=line.strip()
    urlToSend=url + subUrl
    print(urlToSend)
    response = requests.get(urlToSend, headers=headers)
    json_response= json.loads(response.text)
    try:
        shaValue=json_response['data']['attributes']['sha256']
        print(shaValue)
        f.write(shaValue + "\n")
    except:
        s.write(subUrl + "\n")  

