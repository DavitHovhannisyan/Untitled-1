from ev3dev.ev3 import *
from os import *
import random
import time

#A=LargeMotor('outA')
#B=LargeMotor('outB')

f=open("bpm.txt","r")
bpm = int(f.readline()) #Must be fixed
print(bpm)
sleepTime = 0.092*1.5
power = ((bpm-80)/120)*300+200

M1A1 = MediumMotor('outA')
M1A2 = MediumMotor('outB')
M2A1 = MediumMotor('outC')
M2A2 = MediumMotor('outD')

#M1A1 = LargeMotor('in1:i2c3:M1')
#M1A2 = LargeMotor('in1:i2c3:M2')
#M2A1 = LargeMotor('in2:i2c3:M1')
#M2A2 = LargeMotor('in2:i2c3:M2')

while 1:

    number = random.choice([1,2,3,4,5])#1,,2,3,4,5
    print(number)
    if number == 1:


        #Zero

        time1=time.time()
        M1A2.run_forever(speed_sp = -power)
        M2A2.run_forever(speed_sp = -power)
        while time.time() - time1 < (sleepTime*2): #and
            M1A2.run_forever(speed_sp = -power)
            M2A2.run_forever(speed_sp = -power)

        M1A2.stop(stop_action = "brake")
        M2A2.stop(stop_action = "brake")

        time.sleep(sleepTime)

        #Hands down

        M1A2.reset()
        M2A2.reset()


        M1A2.run_forever(speed_sp = power)
        M2A2.run_forever(speed_sp = power)

        time1=time.time()
        while M2A2.position < 30 or M1A2.position < 30: #and
            if time.time() - time1 > sleepTime*4:
                M1A2.stop(stop_action = "brake")
                M2A2.stop(stop_action = "brake")
                break
            if M1A2.position > 30:
                M1A2.stop(stop_action = "brake")
            else:
                M1A2.run_forever(speed_sp = power)
            if M2A2.position > 30:
                M2A2.stop(stop_action = "brake")
            else:
                M2A2.run_forever(speed_sp = power)


        M1A2.stop(stop_action = "brake")
        M2A2.stop(stop_action = "brake")

        time.sleep(sleepTime)

        #Turn Hand Right

        M1A1.reset()
        M2A1.reset()

        M1A1.run_forever(speed_sp = power)
        M2A1.run_forever(speed_sp = -power)

        while M1A1.position < 90 or M2A1.position > -90:
            if M1A1.position > 90:
                M1A1.stop(stop_action = "brake")
            else:        
                M1A1.run_forever(speed_sp = power)
            if M2A1.position < -90:
                M2A1.stop(stop_action = "brake")
            else:        
                M2A1.run_forever(speed_sp = -power)
            
        M1A1.stop(stop_action = "brake")
        M2A1.stop(stop_action = "brake")

        time.sleep(sleepTime/2)

        """
        """
        #1-st Combination

        for x in range(5):
            

            #Turn Hands Right

            M1A1.reset()
            M2A1.reset()

            M1A1.run_forever(speed_sp = -power)
            M2A1.run_forever(speed_sp = power)

            while M1A1.position > -180 or M2A1.position < 180:
                if M1A1.position < -180:
                    M1A1.stop(stop_action = "brake")
                else:        
                    M1A1.run_forever(speed_sp = -power)
                if M2A1.position > 180:
                    M2A1.stop(stop_action = "brake")
                else:        
                    M2A1.run_forever(speed_sp = power)
                
            M1A1.stop(stop_action = "brake")
            M2A1.stop(stop_action = "brake")

            #Turn Hand Right

            M1A1.reset()
            M2A1.reset()

            M1A1.run_forever(speed_sp = power)
            M2A1.run_forever(speed_sp = -power)

            while M1A1.position < 180 or M2A1.position > -180:
                if M1A1.position > 180:
                    M1A1.stop(stop_action = "brake")
                else:        
                    M1A1.run_forever(speed_sp = power)
                if M2A1.position < -180:
                    M2A1.stop(stop_action = "brake")
                else:        
                    M2A1.run_forever(speed_sp = -power)
                
            M1A1.stop(stop_action = "brake")
            M2A1.stop(stop_action = "brake")

            time.sleep(sleepTime/2)

            
        #Turn Hands Right

        M1A1.reset()
        M2A1.reset()

        M1A1.run_forever(speed_sp = -power)
        M2A1.run_forever(speed_sp = power)

        while M1A1.position > -90 or M2A1.position < 90:
            if M1A1.position < -90:
                M1A1.stop(stop_action = "brake")
            else:        
                M1A1.run_forever(speed_sp = -power)
            if M2A1.position > 90:
                M2A1.stop(stop_action = "brake")
            else:        
                M2A1.run_forever(speed_sp = power)
            
        M1A1.stop(stop_action = "brake")
        M2A1.stop(stop_action = "brake")


    if number == 2:
        #Zero
        
        time1=time.time()
        M1A2.run_forever(speed_sp = -power)
        M2A2.run_forever(speed_sp = -power)
        while time.time() - time1 < (sleepTime*2): #and
            M1A2.run_forever(speed_sp = -power)
            M2A2.run_forever(speed_sp = -power)

        M1A2.stop(stop_action = "brake")
        M2A2.stop(stop_action = "brake")

        time.sleep(sleepTime)

        #Hands down

        M1A2.reset()
        M2A2.reset()


        M1A2.run_forever(speed_sp = power)
        M2A2.run_forever(speed_sp = power)

        time1=time.time()
        while M2A2.position < 30 or M1A2.position < 30: #and
            if time.time() - time1 > sleepTime*4:
                M1A2.stop(stop_action = "brake")
                M2A2.stop(stop_action = "brake")
                break
            if M1A2.position > 30:
                M1A2.stop(stop_action = "brake")
            else:
                M1A2.run_forever(speed_sp = power)
            if M2A2.position > 30:
                M2A2.stop(stop_action = "brake")
            else:
                M2A2.run_forever(speed_sp = power)


        M1A2.stop(stop_action = "brake")
        M2A2.stop(stop_action = "brake")

        time.sleep(sleepTime)




        #2-nd Combination

        #Hands down

        M1A2.reset()
        M2A2.reset()


        M1A2.run_forever(speed_sp = -power)
        #M2A2.run_forever(speed_sp = power)


        time1 = time.time()
        while time.time() - time1 < (sleepTime/1.5)*4: #and
            M1A2.run_forever(speed_sp = -power)
            M2A2.run_forever(speed_sp = power)
                
        M1A2.stop(stop_action = "brake")
        M2A2.stop(stop_action = "brake")

        time.sleep(sleepTime/2)

        print("OK")

        for x in range(5):
            time1 = time.time()
            M1A2.run_forever(speed_sp = power)
            M2A2.run_forever(speed_sp = -power)
            while time.time() - time1 < (sleepTime/1.5)*8: #and
                M1A2.run_forever(speed_sp = power)
                M2A2.run_forever(speed_sp = -power)
                    
            M1A2.stop(stop_action = "brake")
            M2A2.stop(stop_action = "brake")

            time.sleep(sleepTime/2)
            time1 = time.time()
            M1A2.run_forever(speed_sp = -power)
            M2A2.run_forever(speed_sp = power)
            while time.time() - time1 < (sleepTime/1.5)*8: #and
                M1A2.run_forever(speed_sp = -power)
                M2A2.run_forever(speed_sp = power)
                    
            M1A2.stop(stop_action = "brake")
            M2A2.stop(stop_action = "brake")

            time.sleep(sleepTime/2)

        time.sleep(sleepTime)

        print("OK")
        M1A2.reset()
        M2A2.reset()

        M1A2.run_forever(speed_sp = power)
        M2A2.run_forever(speed_sp = -power)

        while M1A2.position < 10 or M2A2.position > -80:
            if M1A2.position > 10:
                M1A2.stop(stop_action = "brake")
            else:
                M1A2.run_forever(speed_sp = power)
            if M2A2.position < -80:
                M2A2.stop(stop_action = "brake")
            else:
                M2A2.run_forever(speed_sp = -power)

        M1A2.stop(stop_action = "brake")
        M2A2.stop(stop_action = "brake")

        time.sleep(sleepTime/2)






    if number == 3:
        #Zero

        time1=time.time()
        M1A2.run_forever(speed_sp = -power)
        M2A2.run_forever(speed_sp = -power)
        while time.time() - time1 < (sleepTime*2): #and
            M1A2.run_forever(speed_sp = -power)
            M2A2.run_forever(speed_sp = -power)

        M1A2.stop(stop_action = "brake")
        M2A2.stop(stop_action = "brake")

        time.sleep(sleepTime)

        #Hands down

        M1A2.reset()
        M2A2.reset()


        M1A2.run_forever(speed_sp = power)
        M2A2.run_forever(speed_sp = power)

        time1=time.time()
        while M2A2.position < 30 or M1A2.position < 30: #and
            if time.time() - time1 > sleepTime*4:
                M1A2.stop(stop_action = "brake")
                M2A2.stop(stop_action = "brake")
                break
            if M1A2.position > 30:
                M1A2.stop(stop_action = "brake")
            else:
                M1A2.run_forever(speed_sp = power)
            if M2A2.position > 30:
                M2A2.stop(stop_action = "brake")
            else:
                M2A2.run_forever(speed_sp = power)


        M1A2.stop(stop_action = "brake")
        M2A2.stop(stop_action = "brake")

        time.sleep(sleepTime)


        """
        """
        #3-rd Combination

        #Turn Hands left

        M1A1.reset()
        M2A1.reset()

        M1A1.run_forever(speed_sp = power)
        M2A1.run_forever(speed_sp = power)

        while M1A1.position < 90 or M2A1.position < 90:
            if M1A1.position > 90:
                M1A1.stop(stop_action = "brake")
            else:        
                M1A1.run_forever(speed_sp = power)
            if M2A1.position > 90:
                M2A1.stop(stop_action = "brake")
            else:        
                M2A1.run_forever(speed_sp = power)
            
        M1A1.stop(stop_action = "brake")
        M2A1.stop(stop_action = "brake")

        time.sleep(sleepTime)

        for x in range(5):
            

            #Turn Hands Right

            M1A1.reset()
            M2A1.reset()

            M1A1.run_forever(speed_sp = power)
            M2A1.run_forever(speed_sp = power)

            while M1A1.position > -180 or M2A1.position > -180:
                if M1A1.position < -180:
                    M1A1.stop(stop_action = "brake")
                else:        
                    M1A1.run_forever(speed_sp = -power)
                if M2A1.position < -180:
                    M2A1.stop(stop_action = "brake")
                else:        
                    M2A1.run_forever(speed_sp = -power)
                
            M1A1.stop(stop_action = "brake")
            M2A1.stop(stop_action = "brake")

            #Turn Hand Right

            M1A1.reset()
            M2A1.reset()

            M1A1.run_forever(speed_sp = power)
            M2A1.run_forever(speed_sp = power)

            while M1A1.position < 180 or M2A1.position < 180:
                if M1A1.position > 180:
                    M1A1.stop(stop_action = "brake")
                else:        
                    M1A1.run_forever(speed_sp = power)
                if M2A1.position > 180:
                    M2A1.stop(stop_action = "brake")
                else:        
                    M2A1.run_forever(speed_sp = power)
                
            M1A1.stop(stop_action = "brake")
            M2A1.stop(stop_action = "brake")

            time.sleep(sleepTime/2)

        #Turn Hand Right

        M1A1.reset()
        M2A1.reset()

        M1A1.run_forever(speed_sp = -power)
        M2A1.run_forever(speed_sp = -power)

        while M1A1.position > -70 or M2A1.position > -90:
            if M1A1.position < -70:
                M1A1.stop(stop_action = "brake")
            else:        
                M1A1.run_forever(speed_sp = -power)
            if M2A1.position < -90:
                M2A1.stop(stop_action = "brake")
            else:        
                M2A1.run_forever(speed_sp = -power)
            
        M1A1.stop(stop_action = "brake")
        M2A1.stop(stop_action = "brake")

        time.sleep(sleepTime/2)









    if number == 4:
        #Zero

        time1=time.time()
        M1A2.run_forever(speed_sp = -power)
        M2A2.run_forever(speed_sp = -power)
        while time.time() - time1 < (sleepTime*2): #and
            M1A2.run_forever(speed_sp = -power)
            M2A2.run_forever(speed_sp = -power)

        M1A2.stop(stop_action = "brake")
        M2A2.stop(stop_action = "brake")

        time.sleep(sleepTime)

        #Hands down

        M1A2.reset()
        M2A2.reset()


        M1A2.run_forever(speed_sp = power)
        M2A2.run_forever(speed_sp = power)

        time1=time.time()
        while M2A2.position < 30 or M1A2.position < 30: #and
            if time.time() - time1 > sleepTime*4:
                M1A2.stop(stop_action = "brake")
                M2A2.stop(stop_action = "brake")
                break
            if M1A2.position > 30:
                M1A2.stop(stop_action = "brake")
            else:
                M1A2.run_forever(speed_sp = power)
            if M2A2.position > 30:
                M2A2.stop(stop_action = "brake")
            else:
                M2A2.run_forever(speed_sp = power)


        M1A2.stop(stop_action = "brake")
        M2A2.stop(stop_action = "brake")

        time.sleep(sleepTime)



        """
        """
        #4-th Combination


        #Turn Hands inside

        M1A1.reset()
        M2A1.reset()

        M1A1.run_forever(speed_sp = -power)
        M2A1.run_forever(speed_sp = power)

        while M1A1.position > -45 or M2A1.position < 45:
            if M1A1.position < -45:
                M1A1.stop(stop_action = "brake")
            else:        
                M1A1.run_forever(speed_sp = -power)
            if M2A1.position > 45:
                M2A1.stop(stop_action = "brake")
            else:        
                M2A1.run_forever(speed_sp = power)
            
        M1A1.stop(stop_action = "brake")
        M2A1.stop(stop_action = "brake")

        time.sleep(sleepTime)

        M1A2.run_forever(speed_sp = -power)
        M2A2.run_forever(speed_sp = power)


        time1 = time.time()
        while time.time() - time1 < (sleepTime/1.5)*2: #and
            M1A2.run_forever(speed_sp = -power)
            M2A2.run_forever(speed_sp = power)
                
        M1A2.stop(stop_action = "brake")
        M2A2.stop(stop_action = "brake")

        time.sleep(sleepTime/2)

        print("OK")

        for x in range(5):
            time1 = time.time()
            M1A2.run_forever(speed_sp = power)
            M2A2.run_forever(speed_sp = -power)
            while time.time() - time1 < (sleepTime/1.5)*6: #and
                M1A2.run_forever(speed_sp = power)
                M2A2.run_forever(speed_sp = -power)
                    
            M1A2.stop(stop_action = "brake")
            M2A2.stop(stop_action = "brake")

            time.sleep(sleepTime/2)
            time1 = time.time()
            M1A2.run_forever(speed_sp = -power)
            M2A2.run_forever(speed_sp = power)
            while time.time() - time1 < (sleepTime/1.5)*6: #and
                M1A2.run_forever(speed_sp = -power)
                M2A2.run_forever(speed_sp = power)
                    
            M1A2.stop(stop_action = "brake")
            M2A2.stop(stop_action = "brake")

            time.sleep(sleepTime/2)

        time.sleep(sleepTime)

        print("OK")
        M1A2.reset()
        M2A2.reset()

        M1A2.run_forever(speed_sp = power)
        M2A2.run_forever(speed_sp = -power)

        while M1A2.position < 60 or M2A2.position > -60:
            if M1A2.position > 60:
                M1A2.stop(stop_action = "brake")
            else:
                M1A2.run_forever(speed_sp = power)
            if M2A2.position < -60:
                M2A2.stop(stop_action = "brake")
            else:
                M2A2.run_forever(speed_sp = -power)

        M1A2.stop(stop_action = "brake")
        M2A2.stop(stop_action = "brake")

        time.sleep(sleepTime/2)


        #Turn Hands outside

        M1A1.reset()
        M2A1.reset()

        M1A1.run_forever(speed_sp = power)
        M2A1.run_forever(speed_sp = -power)

        while M1A1.position < 45 or M2A1.position > -45:
            if M1A1.position > 45:
                M1A1.stop(stop_action = "brake")
            else:
                M1A1.run_forever(speed_sp = power)
            if M2A1.position < -45:
                M2A1.stop(stop_action = "brake")
            else:
                M2A1.run_forever(speed_sp = -power)

            
        M1A1.stop(stop_action = "brake")
        M2A1.stop(stop_action = "brake")

        time.sleep(sleepTime)











    if number == 5:
        #Zero

        time1=time.time()
        M1A2.run_forever(speed_sp = -power)
        M2A2.run_forever(speed_sp = -power)
        while time.time() - time1 < (sleepTime*2): #and
            M1A2.run_forever(speed_sp = -power)
            M2A2.run_forever(speed_sp = -power)

        M1A2.stop(stop_action = "brake")
        M2A2.stop(stop_action = "brake")

        time.sleep(sleepTime)

        #Hands down

        M1A2.reset()
        M2A2.reset()


        M1A2.run_forever(speed_sp = power)
        M2A2.run_forever(speed_sp = power)

        time1=time.time()
        while M2A2.position < 30 or M1A2.position < 30: #and
            if time.time() - time1 > sleepTime*4:
                M1A2.stop(stop_action = "brake")
                M2A2.stop(stop_action = "brake")
                break
            if M1A2.position > 30:
                M1A2.stop(stop_action = "brake")
            else:
                M1A2.run_forever(speed_sp = power)
            if M2A2.position > 30:
                M2A2.stop(stop_action = "brake")
            else:
                M2A2.run_forever(speed_sp = power)


        M1A2.stop(stop_action = "brake")
        M2A2.stop(stop_action = "brake")

        time.sleep(sleepTime)



        #5-th Combination



        #Turn Hands inside

        M1A1.reset()
        M2A1.reset()

        M1A1.run_forever(speed_sp = -power)
        M2A1.run_forever(speed_sp = power)

        while M1A1.position > -45 or M2A1.position < 45:
            if M1A1.position < -45:
                M1A1.stop(stop_action = "brake")
            else:        
                M1A1.run_forever(speed_sp = -power)
            if M2A1.position > 45:
                M2A1.stop(stop_action = "brake")
            else:        
                M2A1.run_forever(speed_sp = power)
            
        M1A1.stop(stop_action = "brake")
        M2A1.stop(stop_action = "brake")

        time.sleep(sleepTime)

        M1A2.run_forever(speed_sp = -power)
        M2A2.run_forever(speed_sp = power)


        time1 = time.time()
        while time.time() - time1 < (sleepTime/1.5)*2: #and
            M1A2.run_forever(speed_sp = -power)
            M2A2.run_forever(speed_sp = power)
                
        M1A2.stop(stop_action = "brake")
        M2A2.stop(stop_action = "brake")

        time.sleep(sleepTime/2)

        print("OK")

        for x in range(5):
            time1 = time.time()
            M1A2.run_forever(speed_sp = power)
            M2A2.run_forever(speed_sp = power)
            while time.time() - time1 < (sleepTime/1.5)*6: #and
                M1A2.run_forever(speed_sp = power)
                M2A2.run_forever(speed_sp = power)
                    
            M1A2.stop(stop_action = "brake")
            M2A2.stop(stop_action = "brake")

            time.sleep(sleepTime/2)
            time1 = time.time()
            M1A2.run_forever(speed_sp = -power)
            M2A2.run_forever(speed_sp = -power)
            while time.time() - time1 < (sleepTime/1.5)*6: #and
                M1A2.run_forever(speed_sp = -power)
                M2A2.run_forever(speed_sp = -power)
                    
            M1A2.stop(stop_action = "brake")
            M2A2.stop(stop_action = "brake")

            time.sleep(sleepTime/2)

        time.sleep(sleepTime)

        print("OK")
        M1A2.reset()
        M2A2.reset()

        M1A2.run_forever(speed_sp = -power)
        M2A2.run_forever(speed_sp = -power)

        time1=time.time()
        while M1A2.position > -60 or M2A2.position > -60:
            if time.time() - time1 > sleepTime:
                break
            if M1A2.position < -60:
                M1A2.stop(stop_action = "brake")
            else:
                M1A2.run_forever(speed_sp = -power)
            if M2A2.position < -60:
                M2A2.stop(stop_action = "brake")
            else:
                M2A2.run_forever(speed_sp = -power)

        M1A2.stop(stop_action = "brake")
        M2A2.stop(stop_action = "brake")

        time.sleep(sleepTime/2)


        #Turn Hands outside

        M1A1.reset()
        M2A1.reset()

        M1A1.run_forever(speed_sp = power)
        M2A1.run_forever(speed_sp = -power)

        while M1A1.position < 45 or M2A1.position > -45:
            if M1A1.position > 45:
                M1A1.stop(stop_action = "brake")
            else:
                M1A1.run_forever(speed_sp = power)
            if M2A1.position < -45:
                M2A1.stop(stop_action = "brake")
            else:
                M2A1.run_forever(speed_sp = -power)

            
        M1A1.stop(stop_action = "brake")
        M2A1.stop(stop_action = "brake")

        time.sleep(sleepTime)

        #Zero

        M1A2.run_forever(speed_sp = -power)
        M2A2.run_forever(speed_sp = -power)
        while time.time() - time1 < (sleepTime/2): #and
            M1A2.run_forever(speed_sp = -power)
            M2A2.run_forever(speed_sp = -power)

        #Hands down

        M1A2.reset()
        M2A2.reset()


        M1A2.run_forever(speed_sp = power)
        M2A2.run_forever(speed_sp = power)

        time1=time.time()
        while M2A2.position < 60 or M1A2.position < 60: #and
            if time.time() - time1 > sleepTime*4:
                M1A2.stop(stop_action = "brake")
                M2A2.stop(stop_action = "brake")
                break
            if M1A2.position > 60:
                M1A2.stop(stop_action = "brake")
            else:
                M1A2.run_forever(speed_sp = power)
            if M2A2.position > 60:
                M2A2.stop(stop_action = "brake")
            else:
                M2A2.run_forever(speed_sp = power)


        M1A2.stop(stop_action = "brake")
        M2A2.stop(stop_action = "brake")

        time.sleep(sleepTime)
