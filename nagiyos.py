#!/usr/bin/python3
"""Script to send a YO for Nagios/Icinga alerts. 

Given an API token, it will send a YO to everyone subscribed to that
account. If a cgi-path and host and/or service are also included, it
will include a link to the problematic service in the Nagios web
interface, or the Icinga Classic web interface

If you only want to notify a singe user, you can specify one with the --user flag.

"""

import requests
import argparse

base_yo_url = 'https://api.justyo.co/'

parser = argparse.ArgumentParser(description='Send a Yo notification')

parser.add_argument('--api-token', help='API token to use', required=True)
parser.add_argument('--cgi-path', help='Path to nagios cgi script. E.g. http://nagios.example.com/cgi-bin/icinga/extinfo.cgi')
parser.add_argument('--host', help='Hostname of problematic machine')
parser.add_argument('--service', help='Name of problematic sevice')
parser.add_argument('--username', help='Only yo a specific user')

args = parser.parse_args()

url=''
data = {'api_token': args.api_token}

if args.cgi_path:
    if not args.host:
        print(parser.format_help())
        exit(2)
    if args.service:
        data['link'] = '{cgi_path}?type=2&host={host}&service={service}'.format(cgi_path=args.cgi_path,
                                                                                host=args.host,
                                                                                service=args.service)
    else:
        data['link'] = '{cgi_path}?type=1&host={host}'.format(cgi_path=args.cgi_path,
                                                                                host=args.host)
if args.username:
    data['username'] = args.username
    yo_url = base_yo_url + 'yo/'
else: 
    yo_url = base_yo_url + 'yoall/'

yo = requests.post(yo_url, data=data)

print(yo.text)
