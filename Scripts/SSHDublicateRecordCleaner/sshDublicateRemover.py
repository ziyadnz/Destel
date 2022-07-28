from fileinput import filename
from trace import Trace
from paramiko import SSHClient, AutoAddPolicy
import argparse
from rich import print, pretty, inspect
import pandas as pd

pretty.install()

pars=argparse.ArgumentParser()
pars.add_argument("-i", "--ip", required=True,help="hostName")
pars.add_argument("-u", "--userName", required=True,help="userName")
pars.add_argument("-p", "--password", required=True,help="password")
pars.add_argument("-d", "--destfile", help="Destination File Name & Path (server) ")

args = vars(pars.parse_args()) 
ip=args["ip"]
userName=args["userName"]
password1=args["password"]
destFile=args["destfile"]
sourceFile='sshGet.txt'

client = SSHClient()

#LOAD HOST KEYS
#client.load_host_keys('~/.ssh/known_hosts')
client.load_host_keys('C:/Users/zd/.ssh/known_hosts')
client.load_system_host_keys()

client.set_missing_host_key_policy(AutoAddPolicy())


#client.connect('10.x.x.x', username='root', password='password1')
client.connect(ip, username=userName,password=password1)

sftp = client.open_sftp()
edittedPath='hi2.txt'
sftp.get(destFile, sourceFile)

data = pd.read_csv((sourceFile), names=["ip"],skipinitialspace=True)

data.sort_values("ip", inplace = True)
 
# dropping ALL duplicate values
data.drop_duplicates(subset ="ip",keep ='first',inplace = True)

f = open(edittedPath, 'w')

data.to_csv(edittedPath,encoding='utf-8',index=False,header=None, sep=' ')
with open(edittedPath) as f:
    lines = f.readlines()
    last = len(lines) - 1
    lines[last] = lines[last].replace('\r','').replace('\n','')
with open(edittedPath, 'w') as wr:
    wr.writelines(lines)

sftp.put(edittedPath, destFile)

sftp.close()

client.close()
