# Smart Dancing Robot

Project aims to create a robot that is able to dance under any music by counting the BPM (Beats per minute) and and realize a real-time dance by using Raspberry Pi (Python language) and EV3 brick. In other words the robot dances by feeling the rhythm of the music. This program consist of two parts: BPM counter and dance part. 


### Robot's algorithm
##### 1. BPM Counter for Raspberry Pi
-  Input has two modes: microphone (doesn't work effective in practice because of motor noises) or file (.wav).
-  Analysing inputs: making correlation between amplitude and frequency.
-  Finding peaks and predicting coming peaks.
-  Counting BPM and sending it to EV3.  
##### 2. EV3 Programs
- Waiting for BPM value.
- Receiving from Raspberry Pi.
- Converting BPM to motor power (calculated equation).
- Movement sequence random generating.
- Execution.
### How to install, use and run
- I used Wi-Fi adapter to control Raspberry Pi with SSH Protocol.
- Install libraries (links).
- Install this image file on your EV3 to control it with Raspberry Pi (you can use this guideline.
- Connect your EV3 with Raspberry Pi (via USB) and send codes to Raspberry Pi by SSH.
- BPMFinal.py must stay in Raspberry Pi, but others should be sended to EV3 via SSH.
- Preferred music file should have .wav extension, otherwise program wouldn't run it.
- Finally rename your music file's name to "demo.wav". 
- Change the IP address in 147th line of BPMFinal.py program.
- Run this "sudo python BPMFinal.py && aplay demo.wav"


References:
 - https://gist.github.com/virtuald/c30032a5b8cdacd1a6c0
 - https://2017.spaceappschallenge.org/challenges/ideate-and-create/bring-your-own-solution/teams/untitled_1/project


#### Have fun :) 
