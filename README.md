# Smart Dancing Robot
Our aim is to create a soft for robots to undestand a BPM of random music and realize a real-time dance by using 
Raspberry Pi (Python language) and EV3 brick. Program consist of two parts: BPM counter and motor controller. First of all I researched about existing algorithms so I could use them for my project. 

Here is my used code.

### Robot's algorithm
##### 1. BPM Counter for Raspberry Pi
-  Input has two modes: microphone or file (.wav)
-  Analysing inputs: making correlation between amplitude and frequency
-  Finding peaks and predicting coming peaks.
-  Counting BPM and sending it to EV3  
##### 2. EV3 Programs
- Waiting for BPM value
- Receiving from Raspberry Pi
- Converting BPM to motor power (calculated equation)
- Movement sequence random generating
- Execution
