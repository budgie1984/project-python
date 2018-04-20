# Author: Brian Burroughs
# 4th Year Project

import datetime
import magnet
import myemail
import distance as my_distance
import publish
import time
import RPi.GPIO as GPIO

alarmAm = [14,36]
alarmPm = [21,33]
newTime = datetime.datetime.now()
print("Hour: " + str(newTime.hour) + " Mins: " + str(newTime.minute)) 
sleepInterval = 3
distSensitivity = 50
exitRequest = False
movement = False
alarmTriggered = False
emailFrequency = datetime.timedelta(seconds=61)
resetRequest = False


def monitorInputs(): 
    global exitRequest              
    global movement                 
    global distSensitivity          #  set to 50
    global alarmTriggered           
    while(exitRequest == False):
                                           
        if(movement == False):                     # the box has not been moved since the last update
           
            if ((my_distance.distance() > distSensitivity) &
                (magnet.isLidOpen()==True)):             # if the distance sensitivity has been triggered and the lid has been opened
                movement = True
                sendEmail(False,"")                       # boolean toggles reminder email or box moved email 
                alarmTriggered = True
        else:                                                 # only reached after box has moved at least once
                                                      
            if(magnet.isLidOpen() == False):                  # This will reset the movement after the box has been closed again
                movement = False
                                                # May need to reset the alarmTriggered to false here too????
            
        checkStatus()
        
        time.sleep(sleepInterval)                                   # Check again after the alotted time            

    
def checkStatus():
    global alarmAm
    global alarmPm
    global alarmTriggered
    global time
    global resetRequest
   
    newTime = datetime.datetime.now()
    print("Hour: " + str(newTime.hour) + " Mins: " + str(newTime.minute)) 
    if(alarmTriggered == False):
        print("Reached checkStatus() with alarmTriggered == False")
        am = newTime.hour == alarmAm[0] and newTime.minute == alarmAm[1]
        pm = newTime.hour == alarmPm[0] and newTime.minute == alarmPm[1]
        if(am) or (pm):
            print("Got to the check status>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            # Reset now that the email has been sent
            #alarmTriggered = False
            from myemail import timeStamp
            from myemail import dateSet
            print("Timestamp is: ",timeStamp)
            
            # Debugging
            print("Date Set is: : ",dateSet)
            
            msg = "Am" if am else "Pm"
            if(dateSet):
                print(datetime.datetime.now() - timeStamp)
                print("Got to the date set = true statement")
                if((datetime.datetime.now() - timeStamp) > emailFrequency):
                    sendEmail(True,msg)
            else:
                sendEmail(True,msg)
                print("Got to date not set")
    else:
        if(newTime.hour == alarmAm[0] and newTime.minute == alarmAm[1]) or (newTime.hour == alarmPm[0] and newTime.minute == alarmPm[1]):
            from myemail import timeStamp
            if(resetRequest == False):
                resetRequest = True
                myemail.setTimeStamp()
            else:
                # May need to change the below seconds to 57 if there is a double email bug
                if(datetime.datetime.now() - timeStamp > datetime.timedelta(seconds = 52)):
                    alarmTriggered = False
                    resetRequest = False
        
def sendEmail(sendReminderMessage,msg):
    
    if(sendReminderMessage == True):
        myemail.sendTabletsNotTakenEmail()
        print ("EMAIL SENT (" + msg + " Reminder " + "Tabs not taken!!!)")
        s = "morning" if msg == "Am" else "evening"
        publish.subscribe_pub("tabletbox","Your " + s + " tablets have not been taken")
    else:
        myemail.sendTabletsTakenEmail()
        print ("EMAIL SENT (Tabs Taken????)")
        publish.subscribe_pub("tabletbox","Tablets Taken")

if __name__ == '__main__':
    try:
        monitorInputs()
    except KeyboardInterrupt:
        print("Measuring stopped by user")
        exitRequest = True
        GPIO.cleanup()
