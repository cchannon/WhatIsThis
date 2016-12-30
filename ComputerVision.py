from __future__ import print_function
import time
import picamera
from datetime import datetime
import requests
import operator
import numpy as np
import json
import urllib2 

def processRequest( json, data, headers, params, lcd ):
    lcd.set_color(1.0, 1.0, 0.0)
    lcd.clear()
    lcd.message('Uploading...')
    retries = 0
    result = None

    while True:
        response = requests.request( 'post', _url, json = jsonObj, data = data, headers = headers, params = params )
        if response.status_code == 429: 
            lcd.message( "Message: %s" % ( response.json()['message'] ) )
            if retries <= _maxNumRetries: 
                time.sleep(1) 
                retries += 1
                continue
            else: 
                lcd.message( 'Error: failed after retrying!' )
                break
        elif response.status_code == 200 or response.status_code == 201:
            if 'content-length' in response.headers and int(response.headers['content-length']) == 0: 
                result = None 
            elif 'content-type' in response.headers and isinstance(response.headers['content-type'], str): 
                if 'application/json' in response.headers['content-type'].lower(): 
                    result = response.json() if response.content else None 
                elif 'image' in response.headers['content-type'].lower(): 
                    result = response.content
        else:
            lcd.message( "Error code: %d" % ( response.status_code ) )
            lcd.message( "Message: %s" % ( response.json()['message'] ) )
        break
    lcd.set_color(0.0, 1.0, 0.0)
    lcd.clear()
    lcd.message('Complete!')
    time.sleep(1.0)
    lcd.clear()
    lcd.set_color(1.0, 1.0, 1.0)
    return result

def renderResult (result, lcd) :
    descriptionText = result['description']['captions'][0]['text']
    if len(descriptionText) <= 16:
        lcd.message(descriptionText)
    i = 15
    while i <= len(descriptionText) :
        lcd.clear()
        lcd.message(descriptionText[i-15:i])
        time.sleep(0.3)
        if lcd.is_pressed(LCD.SELECT):
            return
        if lcd.is_pressed(LCD.LEFT):
            i = 15
            continue
        if i == len(descriptionText):
            while True:
                if lcd.is_pressed(LCD.SELECT):
                    break
                if lcd.is_pressed(LCD.LEFT):
                    i = 14
                    break
        i += 1

LCD = None
import Adafruit_CharLCD as LCD

# API parameters
_url = 'https://api.projectoxford.ai/vision/v1.0/analyze'
_key = '' # insert your API key here
_maxNumRetries = 10
params = {'visualFeatures' : 'Color, Categories, Description'} 
headers = dict()
headers['Ocp-Apim-Subscription-Key'] = _key
headers['Content-Type'] = 'application/octet-stream'
jsonObj = None

# Initialize the LCD using the pins
lcd = LCD.Adafruit_CharLCDPlate()
lcd.set_color(1.0, 1.0, 1.0)
lcd.clear()
# This part isn't really necessary, but it's fun and it buys a bit of time to connect to internet
for i in range(1,3):
    for j in range (1,4):
        lcd.clear()
        displayMessage = 'Bootup\nin progress.'
        if j == 2:
            displayMessage +='.'
        if j == 3:
            displayMessage +='..'
        lcd.message(displayMessage)
        time.sleep(1.0)

## Validate internet connection
while True:
    try:
        urllib2.urlopen("http://www.bing.com").close()
    except urllib2.URLError:
        lcd.clear()
        lcd.set_color(1.0, 1.0, 0.0)
        lcd.message("Please wait\nfor internets")
        time.sleep(1)
    else:
        lcd.clear()
        lcd.message("Connected to\nthe internet!")
        time.sleep(2)
        break

# Initialize the camera and set parameters
camera = picamera.PiCamera()
camera.resolution = (1920, 1080)
camera.rotation = 90 # you may not need this; depends on how you set up your camera. 
lcd.clear()
lcd.message('Take a picture!')
while True:
    # Loop through each button and check if it is pressed.
    if lcd.is_pressed(LCD.SELECT):
        # Button is pressed, change the message and backlight.
        lcd.clear()
        lcd.message('Capturing...')
        imageName = r'/home/pi/CV/image' + str(datetime.now()) + '.jpg'
        camera.capture(imageName)
        time.sleep(2.0)
        with open(imageName, 'rb') as f:
            data = f.read()
        result = processRequest(json, data, headers, params, lcd)
        if result is not None:
            renderResult(result, lcd)