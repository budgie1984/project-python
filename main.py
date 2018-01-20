import magnet
import myemail
import distance as my_distance

sendTabletReminderEmail = False

if __name__ == '__main__':
    try:
        while(sendTabletReminderEmail == False):
                dist = my_distance.distance()
                isLidOpen = magnet.isLidOpen()
             
                if ((dist > 50) & (isLidOpen==1)):
                        print ("EMAIL SENT")
                        myemail.sendMailBoxMoved()
                        sendTabletReminderEmail = True
        
         #   time.sleep(1)
                
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
