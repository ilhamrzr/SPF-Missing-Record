from termcolor import colored as warna
from os import system
from urllib import request
import json

system("clear")
banner = '''
╔═╗╔═╗╔═╗  ╔╦╗┬┌─┐┌─┐┬┌┐┌┌─┐  ╦═╗┌─┐┌─┐┌─┐┬─┐┌┬┐
╚═╗╠═╝╠╣   ║║║│└─┐└─┐│││││ ┬  ╠╦╝├┤ │  │ │├┬┘ ││
╚═╝╩  ╚    ╩ ╩┴└─┘└─┘┴┘└┘└─┘  ╩╚═└─┘└─┘└─┘┴└──┴┘

        # Coded by Ilham | @tigabelassec
'''
print(warna(banner, 'green'))
domain = input("Domain > ")
port = input("Port   > ")
apiKey = ""  # API from mxtoolbox.com
apiUrl = 'https://api.mxtoolbox.com/api/v1/Lookup/spf/?argument=' + \
    domain+'&port='+port+'&Authorization='+apiKey

response = request.urlopen(apiUrl)

data = json.loads(response.read())

for mydata in data['Passed']:
    system("clear")
    print(warna(banner, 'green'))
    print("Domain : "+domain+warna(" Not Vulnerable", 'red'))
    print(f"Name   : {mydata['Name']}")
    print(f"Status : {mydata['Info']}")
    print(f"Url    : {mydata['Url']}")
for mydata in data['Failed']:
    system("clear")
    print(warna(banner, 'green'))
    print("Domain : "+domain+warna(" Vulnerable", 'green'))
    print(f"Name   : {mydata['Name']}")
    print(f"Status : {mydata['Info']}")
    print(f"Url    : {mydata['Url']}")
