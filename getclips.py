#!/usr/bin/python3
# -*- coding: UTF-8 -*-# enable debugging

#https://dev.twitch.tv/docs/api/reference/#get-clips

import cgi
import cgitb
cgitb.enable()
import time
import requests
debug=False

#will need a config file for client_id
def getclips(client_id, args):
        url = 'https://www.googleapis.com/qpxExpress/v1/trips/search?key=mykeyhere'
        payload = "payload"
        headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
        r = requests.post(url, data=payload, headers=headers)
        return r

print("Content-Type: application/json; charset=utf-8")

r = getclips('uo6dggojyb8d6soh92zknwmi5ej1q2')

print("Status: "+str(r.status_code) )

print("")
print(r.text)
