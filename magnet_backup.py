
    while True: 

        if io.input(door_pin):
            print("OPEN")
            time.sleep(0.5)
    
        else:
            print("CLOSED")
            time.sleep(0.5)




if __name__ == '__main__':
    try:
        while(hasSentEmailToday == False):
                lidPosition = isLidOpen()

                if io.input(door_pin):
                    hasSentEmailToday = True
                    print('Email sent')
                    myemail.lidOpened()
                 
        
         #   time.sleep(1)
                
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()