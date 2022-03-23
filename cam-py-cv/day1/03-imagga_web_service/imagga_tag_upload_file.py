#!/usr/bin/python3
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# imagga_tag_upload_file.py
# Upload file to imagga service and get the result of tag
#
# Author : sosorry
# Date   : 18/04/2015

import configparser 
import requests
import json

#
# replace "authorization: "Basic ..." with your Authorization in web_service.conf
#
config = configparser.ConfigParser()
config.read('web_service.conf')
api_key    = config.get('imagga', 'api_key')
api_secret = config.get('imagga', 'api_secret')
image_path = '/home/pi/test.jpg'

response = requests.post('https://api.imagga.com/v2/tags',
auth=(api_key, api_secret),
files={'image': open(image_path, 'rb')})

data = json.loads(response.text)
if True:
#try:
    tag = data["result"]["tags"][0]["tag"]["en"]
    print("Get tag... ")
    print("<< " + tag + " >>")
#except Exception as e:
    #print("type error: " + str(e))
