#if the script fails, check your mail for a security warning
#you may have to change your settings to allow apps to send mail
import smtplib
import time

#setup
server = smtplib.SMTP('smtp.gmail.com:587') #set client (gmail currently)
server.starttls()
server.login("your username", "your password") #set credentials
print("Logged on!")
mailcount = 0

#message
msg = "Test\nThe script is running!" #set message
server.sendmail("your full email", "recipient's full email", msg) #set addresses
print("Message sent!")
mailcount += 1
#you may may send as many emails as you want before closing the connection
#e.g. cycling through a list of recipients using a loop
#could use conditional logic to decide between sending different messages

#close
print("Total mail sent: ", mailcount)
print("Ending operations.")
server.quit()