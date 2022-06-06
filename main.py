#! python3

from config import *
import requests
from linode_api4 import LinodeClient
from linode_api4.objects.domain import Domain, DomainRecord
from time import sleep as wait

client = LinodeClient(apiToken)

def get_prefix(input_address):
    address_list = input_address.split(':')
    return ':'.join(address_list[:int(prefixLength / 16)])

def change_prefix(input_address, new_prefix):
    address_list = input_address.split(':')
    return new_prefix + ':' + ':'.join(address_list[int(prefixLength / 16):])

domain = Domain(client, domainId)

print('Started.')

while True:
    ipv4 = requests.get(ipv4Link, verify = True).text.rstrip()
    ipv6 = requests.get(ipv6Link, verify = True).text.rstrip()
    ipv6Prefix = get_prefix(ipv6)

    if ((ipv4 != ipv4Old) or (ipv6Prefix != ipv6Old)):
        print('Checking...')
        for record in domain.records:
            if (':' in record.target):
                if ((ipv6Prefix != ipv6Old) and (get_prefix(record.target) == ipv6Old)):
                    domain.record_create(record_type="AAAA",name=record.name,target=change_prefix(record.target, ipv6Prefix))
                    record.delete()

            else:
                if ((ipv4 != ipv4Old) and (record.target == ipv4Old)):
                    domain.record_create(record_type="A",name=record.name,target=ipv4)
                    record.delete()

        ipv4Old = ipv4
        ipv6Old = ipv6Prefix
        with open("config.py", "w") as file:
            file.write("ipv4Link = '" + ipv4Link + "'\nipv6Link = '" + ipv6Link + "'\ndomainId = " + str(domainId) + "\napiToken = '" + apiToken + "'\nwaitTime = " + str(waitTime) + "\nipv4Old = '" + ipv4 + "'\nipv6Old = '" + ipv6Prefix + "'\nprefixLength = " + str(prefixLength))
        print('Done!')

    wait(waitTime)
