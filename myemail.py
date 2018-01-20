import smtplib

from_address = 'applied4thyearproject@gmail.com'
to_address = 'budgie1984@gmail.com'
password = 'omonujaku'


boxMoved = "Your medicine box has being moved and the lid has been removed,Did you take your tablets?"
boxNotMoved = "Your medicine box has not being moved, You forgot to take tablets!!!"

smokeAlert = "Smoke has been detected in your home"

lid_opened = "The lid on your med bas has been opened, Did you take your tablets?"
lid_not_opened = "The lid on your med bas has been not been opened, You forgot to take your tablets!!!"


def sendMailBoxMoved():
 mail = smtplib.SMTP('smtp.gmail.com',587)

 mail.ehlo()
 mail.starttls()
 mail.login(from_address, password)
 mail.sendmail(from_address,to_address,boxMoved)
 mail.close()

def sendMailBoxNotMoved():
 mail = smtplib.SMTP('smtp.gmail.com', 587)
 mail.ehlo()
 mail.starttls()
 mail.login(from_address, password)
 mail.sendmail(from_address,to_address, boxNotMoved)
 mail.close()

def smokeDetected():
 mail = smtplib.SMTP('smtp.gmail.com', 587)
 mail.ehlo()
 mail.starttls()
 mail.login(from_address, password)
 mail.sendmail(from_address,to_address, smokeAlert)
 mail.close()

def lidOpened():
 mail = smtplib.SMTP('smtp.gmail.com', 587)
 mail.ehlo()
 mail.starttls()
 mail.login(from_address, password)
 mail.sendmail(from_address,to_address, lid_opened)
 mail.close()

def lidNotOpened():
 mail = smtplib.SMTP('smtp.gmail.com', 587)
 mail.ehlo()
 mail.starttls()
 mail.login(from_address, password)
 mail.sendmail(from_address,to_address, lid_not_opened)
 mail.close()
