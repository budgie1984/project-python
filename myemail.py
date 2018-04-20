import smtplib
import datetime

from_address = 'applied4thyearproject@gmail.com'
to_address = 'budgie1984@gmail.com'
password = 'omonujaku'


tabletsTaken = "Your medicine box has being moved and the lid has been removed,Did you take your tablets?"
tabletsNotTaken = "Your medicine box has not being moved, You forgot to take tablets!!!"


timeStamp = 0
dateSet = False


def setTimeStamp():
    global timeStamp
    global dateSet
    timeStamp = datetime.datetime.now()
    dateSet = True


def sendTabletsTakenEmail():
 mail = smtplib.SMTP('smtp.gmail.com',587)
 mail.ehlo()
 mail.starttls()
 mail.login(from_address, password)
 mail.sendmail(from_address,to_address,tabletsTaken)
 mail.close()
 setTimeStamp()

def sendTabletsNotTakenEmail():
 mail = smtplib.SMTP('smtp.gmail.com', 587)
 mail.ehlo()
 mail.starttls()
 mail.login(from_address, password)
 mail.sendmail(from_address,to_address,tabletsNotTaken)
 mail.close()
 setTimeStamp()



