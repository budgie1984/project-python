import magnet
import myemail
import distance as my_distance
import datetime

tabletsTakenConditions = False
tabletsNotTaken = False

start = datetime.time(17, 00)
end = datetime.time(16,32)
#dist = my_distance.distance()
#isLidOpen = magnet.isLidOpen()
if __name__ == '__main__':
    try:
        
        while(True):
            
                dist = my_distance.distance()
                isLidOpen = magnet.isLidOpen()
                

                if(datetime.datetime.now().time() > start): 
                        print("got here")
                        myemail.sendTabletsNotTakenEmail()        # currently gets to here and stops
                        #tabletsNotTaken = True

                        break
                        continue
                        sendTabletReminderEmail = False
                        print(datetime.datetime.now().time())
           
                    
        if ((dist > 50) & (isLidOpen == 1)):
            print ("Conditions met for tablets taken - tablets taken email sent")
            myemail.sendTabletsTakenEmail()
            tabletsTakenConditions = True
                     
         #   time.sleep(1)
                
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
