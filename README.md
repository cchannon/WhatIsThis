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

## Install Raspbian Linux and enable the camera
If you've never worked with a Raspberry Pi before, the first thing you'll need to do is install the operating system. 

If your MicroSD card came with NOOBS, just connect a monitor, keyboard, mouse and power supply to your Pi and follow the prompts to install Raspbian Linux (yes, it's that easy).

If your MicroSD did not come with NOOBS, [download it!](https://www.raspberrypi.org/downloads/noobs/ "Noobs Download")

Once Linux starts up, set up the camera following the instructions [here](https://www.raspberrypi.org/learning/getting-started-with-picamera/worksheet/ "Raspberry Pi foundation Getting Started with PiCamera")

## Building it!
The biggest chunk of your time will be in assembling the LCD display, for which Adafruit provides detailed instructions. (check adafruit for the latest link, but at the time of this posting was [here](https://learn.adafruit.com/adafruit-16x2-character-lcd-plus-keypad-for-raspberry-pi/assembly "16x2 Character lcd plud keypad from adafruit"))

Take your time, and if you've never done this kind of thing before, make sure you take the time to practice with soldering wire on a basic PCB in advance.

**Seriously, this is the shortest part of the instructions, but the hardest part to get right. TAKE YOUR TIME!

## Set up your Cognitive Services account
Not nearly as creepy as the name might suggest, Microsoft Cognitive Services is a set of web APIs that let developers access unbelievable artificial intelligence capabilities with just a few lines of code, including the ability to decipher what a picture is all about. We'll use this web API to figure out what it is you took a picture of, and to amaze your friends!

First, you'll need to create an account and subscribe to the appropriate services.

**I did this part a long time ago, so if I got the details wrong or if they've changed, please correct me, people!**

Go to the Microsoft [Cognitive Services webiste](https://www.microsoft.com/cognitive-services "Microsoft Cognitive Services") and click "Get Started for Free"

The site will ask you to login with a Live ID (if you don't have one, just sign up; it's free) 
	
You'll then have your choice of many, many cognitive services APIs to use on a trial basis. You're looking for the Computer Vision API. Sign up for that one, and once it lists out your subscriptions, it should show you the key or something that looks like:

* Key 1: XXXXXXXXXXXXXXXXXXXXXXXXXXXX
	
...If you see that, click *show* to reveal the key, and copy it to a local notepad so you don't lose it

Don't worry - this preview isn't time-dependent (at the time I am writing this); It just limits you to 5000 photos per month for free (more than anyone should need, right?).

## a few dependencies...
To make it all work here you'll need to install a few python dependencies. Follow the instructions on these sites, and you should be good. If you have issues here, let me know and I will update the instructions.
* http://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c
* https://learn.adafruit.com/adafruit-16x2-character-lcd-plus-keypad-for-raspberry-pi/usage

## Let's write some code!
Grab the Python script from this Github lirary and copy it to your Raspberry Pi. I copied it directly to the /home/pi directory, but really you can put it anywhere you want the file and all its pictures to be saved.

Open the Python script in your Raspberry Pi (it should contain a Python IDE) and edit the _key variable on line 14 to match the API key you got from the Cognitive Services site for yout Computer Vision API.

You should now be ready to test execute. Run the Python code from your Raspberry Pi (with the entire pi, including camera and LCD assembled) and you should soon see the test prompts to work with the camera. Use the Select button to take pictures and the Left button to scroll back and repeat long text.

If everything works correctly in test, it is time to enable the app to execute on startup. I searched a lot for instructions for this online and found at least 6 ways to do it, but this seemed the easiest and most reliable. If this method doesn't work for you, I recommend checking your linux distribution, and then searching online for other ways to approach the problem.

Launch the Linux Terminal and enter **sudo crontab -e**

This launches a basic text editor window.
scroll to the bottom of the commented text (below all the # signs) and enter the following text: 

**@reboot sleep 30 ; python /home/pi/ComputerVision.py &**

Or, replace the /home/pi/ComputerVision.py with whatever location you used to save the python file (I mentioned earlier this is where I saved it, this is the only time that matters in this README)

Now press Ctrl + X to Exit the editor, then Y to accept changes and Enter to finish.

## Let's make it happen!
OK, assuming I missed nothing in the instructions here, you should now be ready to boot up your raspberry pi on any power source--even a battery one--and take some pictures.

If I've missed important steps here, please let me know. Also, I know there are many ways this file can be improved; if you're interested in contributing, just fork it and send me a pull request!

** 