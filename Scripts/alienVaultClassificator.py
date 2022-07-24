from calendar import c
from numpy import integer
import pandas as pd


file_name = open("files.txt", "r")
filenames=file_name.readlines()

#file_path = str(input('onlyips.csv'))


for x in filenames:
    csv_file = pd.read_csv((x.strip()))

    indicatorTypes = csv_file['Indicator type'].tolist()
    indicators = csv_file['Indicator'].tolist()


    index=0
    for i in indicatorTypes:
    
        if (indicatorTypes[index] == "IPv4"):
            with open('IPv4.txt', 'a')  as IPv4:
                IPv4.write(indicators[index] + "\n")
        elif (indicatorTypes[index] =="FileHash-SHA256"):
            with open('FileHash-SHA256.txt', 'a')  as Sha256:
                 Sha256.write(indicators[index] + "\n")
        elif  (indicatorTypes[index] =="domain"):
            with open('domain.txt', 'a')  as domain:
                domain.write(indicators[index] + "\n")
        else:
            print(indicatorTypes[index])
        index=index+1
        # else:
        #     with open('MaliciousResult.txt', 'a')  as malicious:
            #        malicious.write(str(i)) and malicious.write("\t Malicious") and malicious.write(" this Domains Detectd by "+ str(json_response['positives']) + "  Solutions\n")
