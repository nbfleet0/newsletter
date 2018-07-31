import smtplib
from smtplib import SMTPException

me = "EMAIL@gmail.com"
you = "EMAIL@gmail.com"

stories = open("stories.txt", "r")
string_stories = stories.read().replace('\n', '</br>')
stories.close()

message = """From: Arbor Data <data@arborventures.com>
To: To Person <spark@arborventures.com>
MIME-Version: 1.0
Content-type: text/html; charset=us-ascii
Subject: Arbor Ventures Data Digest

See new stories below
""" + string_stories

server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login("USERNAME", "PASSWORD")
text = message
server.sendmail(me, you, text)
server.quit()




