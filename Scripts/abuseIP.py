import requests
import json
import pandas
import csv

file_path ="ip.csv"
IP_CSV = pandas.read_csv((file_path))

ip=IP_CSV['ip'].tolist()


API_KEY = '642ee89e29c14e80c77a727a35f92ca885cb729db26a9ff28a15fd67973384ad8579da2d350bdf3d'
url = 'https://api.abuseipdb.com/api/v2/check'

csv_columns = ['ipAddress','abuseConfidenceScore']

headers = {
    'Accept': 'application/json',
    'Key': API_KEY
}
with open("AbuseIP_MaliciousResults.csv","a", newline='') as filecsv:
    writer = csv.DictWriter(filecsv, fieldnames=csv_columns)
    writer.writeheader()
with open("AbuseIP_CleanResults.csv","a", newline='') as filecsv:
    writer = csv.DictWriter(filecsv, fieldnames=csv_columns)
    writer.writeheader()
for i in ip:
    parameters = {
        'ipAddress': i,
        'maxAgeInDays': '90'}

    respnse= requests.get( url=url,headers=headers,params=parameters)
    json_Data = json.loads(respnse.content)
    json_main = json_Data["data"]
    if(json_main['abuseConfidenceScore']>40):
        with open("AbuseIP_MaliciousResults.csv","a", newline='')as filecsv:
            writer= csv.DictWriter(filecsv,fieldnames=csv_columns,extrasaction='ignore')
            writer.writerow(json_main)
    else:
        with open("AbuseIP_CleanResults.csv","a", newline='')as filecsv:
            writer= csv.DictWriter(filecsv,fieldnames=csv_columns,extrasaction='ignore')
            writer.writerow(json_main)