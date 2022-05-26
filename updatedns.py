#! python3

ipv4Link = 'http://ipv4.icanhazip.com/'
ipv6Link = 'http://ipv6.icanhazip.com/'
domainId = '<id>'
apiToken = '<api>'
waitTime = 30

from config import *
import requests
import json

ipv4 = requests.get(ipv4Link, verify = True)
ipv6 = requests.get(ipv6Link, verify = True)

