import smtplib
from smtplib import SMTPException


me = "arborventuresdata@gmail.com"
you = "adambarrneuwirth@gmail.com"

stories = open("stories.txt", "r")
string_stories = stories.read().replace('\n', '</br>')
stories.close()

buzz = open("buzz.txt", "r")
string_buzz = buzz.read().replace('\n', '</br>')
buzz.close()

message = """From: Arbor Ventures <arborventuresdata@gmail.com>
To: Adam Barr-Neuwirth <adambarrneuwirth@gmail.com>
MIME-Version: 1.0
Content-type: text/html; charset=us-ascii
Subject: Arbor Ventures Data Digest

<html style="background-color:#ecf0f1; font-family: Helvetica, Arial, sans-serif; a{color:#006699;}">
<center><img src="http://www.arborventures.com/images/common/arbor-ventures.svg" height="100" alt="logo"/></center></br></br>
""" + string_stories + string_buzz

server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login("arborventuresdata", "8arbor88")
text = message
server.sendmail(me, you, text)
server.quit()