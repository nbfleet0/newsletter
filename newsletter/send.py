import smtplib
from smtplib import SMTPException


me = "arbordata@arborventures.com"
you = "adambarrneuwirth@gmail.com"

stories = open("stories.txt", "r")
string_stories = stories.read().replace('\n', '</br>')
stories.close()

message = """From: Arbor Data <arbordata@arborventures.com>
To: Adam Barr-Neuwirth <adambarrneuwirth@gmail.com>
MIME-Version: 1.0
Content-type: text/html; charset=us-ascii
Subject: Arbor Ventures Data Digest

<html style="background-color:#ecf0f1; font-family: Helvetica, Arial, sans-serif; a{color:#006699;}">
<center><img src="http://www.arborventures.com/images/common/arbor-ventures.svg" height="100" alt="logo"/></center></br></br>
""" + string_stories

server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login("adambarrneuwirth", "PASSWORD")
text = message
server.sendmail(me, you, text)
server.quit()