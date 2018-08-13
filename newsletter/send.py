import smtplib
from smtplib import SMTPException


me = "arborventuresdata@gmail.com"
you = "spark@arborventures.com"

#Send news stories
stories = open("./data/stories.txt", "r")
string_stories = stories.read().replace('\n', '</br>')
stories.close()

#Send top buzz startups

#buzz = open("./data/buzz.txt", "r")
#string_buzz = buzz.read().replace('\n', '</br>')
#buzz.close()

#Send top fintech buzz startups

#fintech_buzz = open("./datafintech_buzz.txt", "r")
#string_fintech_buzz = fintech_buzz.read().replace('\n', '</br>')
#fintech_buzz.close()

message = """From: Arbor Ventures <arborventuresdata@gmail.com>
To: Sang Ha Park <spark@arborventures.com>
MIME-Version: 1.0
Content-type: text/html; charset=us-ascii
Subject: Arbor Ventures Data Digest

<html style="background-color:#ecf0f1; font-family: Helvetica, Arial, sans-serif; a{color:#006699;}">
<center><img src="http://fintechnews.hk/wp-content/uploads/2018/07/Arbor-Ventures.png" height="100" alt="logo"/></center></br></br>
""" + string_stories #+ string_buzz + string_fintech_buzz


server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login("arborventuresdata", "8arbor88")
text = message
server.sendmail(me, you, text)
server.quit()