import requests
import json
import csv

""" Written by Ziya DENİZ """
""" The purpose of this code is get recent blacklisted ips from abuseIPdb to add our lookup file. With this we can decrease the number of allerts.
While number of alerts are decreasing if our system has some vulnerabilities we protect it from automated scanner hosts activities. """

# Defining the api-endpoint
url = 'https://api.abuseipdb.com/api/v2/blacklist'


""" With free plan we have only 5 requests limit"""

querystring = {
    'confidenceMinimum':'90',
    'limit':'1'
}

headers = {
    'Accept': 'application/json',
    'Key': '8d250d6b3db4149c389b4aa6e6e5ebe3573cd02c93893c5e13c51f7488eee46e96d804f466b0fae6'
}

response = requests.request(method='GET',url=url, headers=headers, params=querystring)

json_Data = json.loads(response.content)
print(json_Data)
json_main = json_Data["data"]

csv_columns = ['ipAddress']




index=0;
for i in json_main:
    ip=json_main[index]["ipAddress"]
    with open('RecentBlackListedIPs.txt', 'a')  as IPv4:
        IPv4.write(ip + "\n")
    index+=1
    print(ip)    

