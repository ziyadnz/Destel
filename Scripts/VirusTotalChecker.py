import requests
import time
import json
import pandas as pd

file_name = "ip_intel_tracking.csv"
#file_path = str(input('onlyips.csv'))
domain_CSV = pd.read_csv((file_name))

Urls = domain_CSV['ioc'].tolist()

API_key = '64857d0f2d98c1be3d940966278b4577ffc957cc579ab62a6d919babb79cd987'
url = 'https://www.virustotal.com/vtapi/v2/url/report'


parameters = {'apikey': API_key, 'resource': Urls}

for i in Urls:
    parameters = {'apikey': API_key, 'resource': i}

    response= requests.get(url=url, params=parameters)
    json_response= json.loads(response.text)
    if(type(i) != str):
        print(json_response)
        if json_response['response_code'] <= 0:
            with open('NotFoundResults.txt', 'a')  as notfound:
                notfound.write(str(i)) and notfound.write("\tNOT found please Scan it manually\n")
        elif json_response['response_code'] >= 1:

            if json_response['positives'] <= 0:
                with open('CleanResults.txt', 'a')  as clean:
                    clean.write(str(i)) and clean.write("\t NOT malicious \n")
            else:
                with open('MaliciousResult.txt', 'a')  as malicious:
                    malicious.write(str(i)) and malicious.write("\t Malicious") and malicious.write(" this Domains Detectd by "+ str(json_response['positives']) + "  Solutions\n")

        time.sleep(15)
    else:
        print(json_response)
        if json_response['response_code'] <= 0:
            with open('NotFoundResults.txt', 'a')  as notfound:
                notfound.write(i) and notfound.write("\tNOT found please Scan it manually\n")
        elif json_response['response_code'] >= 1:

            if json_response['positives'] <= 0:
                with open('CleanResults.txt', 'a')  as clean:
                    clean.write(i) and clean.write("\t NOT malicious \n")
            else:
                with open('MaliciousResult.txt', 'a')  as malicious:
                    malicious.write(i) and malicious.write("\t Malicious") and malicious.write(" this Domains Detectd by "+ str(json_response['positives']) + "  Solutions\n")

        time.sleep(15)