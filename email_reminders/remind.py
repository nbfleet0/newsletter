import smtplib
from email.mime.text import MIMEText
import sys

#this file is triggered automatically by linux's 'at' command. this parses the saved email and sends it to the recipient

uid = sys.argv[1]


messages = open("messages.xml", "r")

message = messages.read().split("<message id='" + uid + "'>")[1].split("</message>")[0]

to = message.split("<to>")[1].split("</to>")[0]
to_recipients = to.split(",")

subject = message.split("<subject>")[1].split("</subject>")[0]
body = message.split("<body>")[1].split("</body>")[0]


#what to delete when we're done
messages.close()
messages = open("messages.xml", "r")
split = messages.read().split("<message id='" + uid + "'>")
first_half = split[0]
second_half = split[1].split("</message>")[1]
messages.close()


s = smtplib.SMTP('smtp.gmail.com:587')
s.ehlo()
s.starttls()
s.login("arborventuresdata", "8arbor88")

s.set_debuglevel(1)
msg = MIMEText(body)
sender = "arborventuresdata@gmail.com"
recipients = to_recipients
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = ", ".join(recipients)
s.sendmail(sender, recipients, msg.as_string())
s.quit()


# remove message from xml

messages = open("messages.xml", "w")
new_file = first_half + second_half
messages.write(new_file)
messages.close()


