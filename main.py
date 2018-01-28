import datetime
import magnet
import myemail
import distance as my_distance
import publish

#movement = False  # distance sensor < 50cm
#sendReminderEmail = True

#times to check(for testing at the current time)
start = datetime.time(21, 30)
end = datetime.time(22,57)



def initScan():
    movement = False
    while(movement == False):
        dist = my_distance.distance()
        isLidOpen = magnet.isLidOpen()
        if ((dist > 50) & (isLidOpen==1)):
            movement = True
           sendReminderEmail = False
        checkReminders()    
    sendEmail()

def checkReminders():
    if((datetime.datetime.now().time() >= end) & (sendReminderEmail == True)):
        myemail.sendTabletsNotTakenEmail()
        sendReminderEmail = False

        
def sendEmail():
    print ("EMAIL SENT")
    myemail.sendTabletsTakenEmail()
                        #publish.publish_callback()
    initScan()      

if __name__ == '__main__':
    try:
        sendReminderEmail = True
        initScan()



    except KeyboardInterrupt:
        print("Measuring stopped by user")
        GPIO.cleanup()
