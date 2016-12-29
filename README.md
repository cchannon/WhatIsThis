# WhatIsThis?
A basic Python file for image capture and recognition on a Raspberry Pi

## Basics
This Python library (and README) will help you to create just about the coolest camera you've ever seen. From scratch. Yourself. No, seriously. 
I wrote this to enable people who have NEVER written a line of code to build their very own magicitasital camera, and this README will walk you through it.

Instead of just showing you a picture, this camera will actually describe what it sees when you take a picture (how cool is that?)

Together, we'll take a basic Raspberry Pi computer running Linux, and use it to write a Python program which accesses a free Microsoft API service to analyze photographs nearly instantaneously. The result we'll render on a basic LCD display from Adafruit (just about the coolest place on the internet for an IOT geek).

Once we're done, you'll have a compact device you can carry around and show to friends, taking pictures and amazing them with how awesome a tiny computer like that can be!

## Requirements
YOU DO NOT NEED TO BE A PROGRAMMER FOR THIS TUTORIAL (although it wouldn't hurt)

There are some basic hardware requriements, and I have listed some links below to take you to websites where you can buy them.

1. Raspberry Pi:

	> You can buy a Raspberry Pi from just about anywhere and get the same result. I proofed this concept on a Pi 3, which you can buy direct from the [Raspberry Pi Foundation](https://raspberrypi.org "Raspberry Pi Foundation") or with lots beyond the basics from [Adafruit] (https://adafruit.com "Adafruit")
2. Raspberry Pi Camera: 

	> The camera rarely comes with starter sets, so check the set you're buying and if it doesn't include a camera, you'll need to buy one from one of the sites listed above
3. Adafruit multicolor LCD Display
	
	> For this project, I used a [basic multicolor LCD display from Adafruit](https://www.adafruit.com/products/1110 "16x2 character lcd plus keypad from Adafruit"), designed for the Raspberry Pi. You can certainly use others, but you may need to make minor chages to the code.
4. Soldering gear
	
	> In order to assemble the LCD display, you're going to need a soldering iron, wire, goggles, etc. Make sure you're well equipped! safety-first!
5. MicroSD Card with NOOBS
	
	> Most Raspberry Pi kits come with a MicroSD card included with an installation of NOOBS (this is a basic program which lets you insall the common RPi operating systems). If yours doesn't, make sure you buy / download one (use a search engine!)

## Install Raspbian Linux
If you've never worked with a Raspberry Pi before, the first thing you'll need to do is install the operating system. 

If your MicroSD card came with NOOBS, just connect a monitor, keyboard, mouse and power supply to your Pi and follow the prompts to install Raspbian Linux (yes, it's that easy).

If your MicroSD did not come with NOOBS, [download it!](https://www.raspberrypi.org/downloads/noobs/ "Noobs Download")

## Building it!
The biggest chunk of your time will be in assembling the LCD display, for which Adafruit provides detailed instructions. (check adafruit for the latest link, but at the time of this posting was [here](https://learn.adafruit.com/adafruit-16x2-character-lcd-plus-keypad-for-raspberry-pi/assembly "16x2 Character lcd plud keypad from adafruit"))

Take your time, and if you've never done this kind of thing before, make sure you take the time to practice with soldering wire on a basic PCB in advance.

## Set up your Cognitive Services account
Not nearly as creepy as the name might suggest, Microsoft Cognitive Services is a set of web APIs that let developers access unbelievable artificial intelligence capabilities with just a few lines of code, including the ability to decipher what a picture is all about. We'll use this web API to figure out what it is you took a picture of, and to amaze your friends!

First, you'll need to create an account and subscribe to the appropriate services.

**I did this part a long time ago, so if I got the details wrong or if they've changed, please correct me, people!**

	1. Go to the Microsoft [Cognitive Services webiste](https://www.microsoft.com/cognitive-services "Microsoft Cognitive Services") and click "Get Started for Free"

	2. The site will ask you to login with a Live ID (if you don't have one, just sign up) then will give you your choice of many, many cognitive services APIs to use on a trial basis. You're looking for the Computer Vision API. Sign up for that one, and once it lists out your subscriptions, it should show you the key or something that looks like:

		* Key 1: XXXXXXXXXXXXXXXXXXXXXXXXXXXX
	
	3. If you see that, click *show* to reveal the key, and copy it to a local notepad so you don't lose it
	
	4. Don't worry - this preview isn't time-dependent (at the time I am writing this). It just limits you to 5000 photos per month for free.

## Let's write some code!
