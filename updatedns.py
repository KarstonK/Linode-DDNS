#! python3

ipv4Link = 'http://ipv4.icanhazip.com/'
ipv6Link = 'http://ipv6.icanhazip.com/'
domainId = '<id>'
apiToken = '<api>'
waitTime = 30

from config import *
import requests
import json
from linode_api4 import LinodeClient
from linode_api4.objects.domain import Domain, DomainRecord
import ipaddress

client = LinodeClient(apiToken)

while true:
    ipv4 = requests.get(ipv4Link, verify = True)
    ipv6 = requests.get(ipv6Link, verify = True)

    if ((ipv4 != ipv4Old) or (ipv4 != ipv4Old)):
        for record in Domain(client, domainId).records:
            if (':' in record.target):
                if (ipv6 != ipv6Old):
                    DomainRecord().target = 

            else:
                if ((ipv4 != ipv4Old) and (record.target == ipv4Old)):
                    DomainRecord().target = ipv4

    wait(waitTime)
