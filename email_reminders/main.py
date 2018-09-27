import poplib
from email import parser
import email
import reminder_functions
import datetime
import quopri
import uuid
from subprocess import call
import os
import re
# from crontab import CronTab

#this file retrieves new messages from arborventuresdata@gmail.com. It determines if they have a "remind" clause, and if they do, it saves the message in messages.xml

# need to run command 'sudo launchctl load -w /System/Library/LaunchDaemons/com.apple.atrun.plist' before this can work 

# cron = CronTab()
pop_conn = poplib.POP3_SSL('pop.gmail.com')
pop_conn.user('arborventuresdata')
pop_conn.pass_('8arbor88')
#Get messages from server:
messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
# Concat message pieces:
messages = ["\n".join(mssg[1]) for mssg in messages]
#Parse message intom an email object:
messages = [parser.Parser().parsestr(mssg) for mssg in messages]
for message in messages:
	subject = message['subject']
	print(subject)

	sender = message['from']
	print(sender)

	date = message['date']
	print(date)
	date = date.split(" +")[0]
	date = date.split(" -")[0]
	# date = date.replace(", ", ", 0")
	dateobj = datetime.datetime.strptime(date, '%a, %d %b %Y %H:%M:%S')

	if(message.is_multipart()):
		body = message.get_payload(0)
	else:
		body = message.get_payload()
	
	body = quopri.decodestring(str(body))
	# body = body.split("\n\n")[1]
	print ('Body!')
	print(body)

	#Check whether the email contains "Remind"
	reminder_obj = reminder_functions.parseReminder(body)
	
	if not reminder_obj:
		print("no reminder")
	else:
		body = "Remind" + re.split("remind", body, flags=re.IGNORECASE)[1]
		# Add in name -> email conversion later
		print("FOR:")
		for i, recipient in enumerate(reminder_obj[0]):
			if recipient == "me":
				reminder_obj[0][i] = sender
			elif(reminder_obj[0][0] == "all" or reminder_obj[0][0] == "everyone"):
				eminder_obj[0][i] = "team@arborventures.com" #this is only possible if we have arborventures account

		time = reminder_obj[1]

		print("time info:")
		print(time)


		days = int(time["days"])+(int(time["months"])*30)+(int(time["years"])*365)
		weeks = int(time["weeks"])
		hours = int(time["hours"])

		timed = datetime.timedelta(weeks=int(time["weeks"]), days=days, hours=int(time["hours"]))

		rundate = dateobj + timed

		print("will send on:")
		print(rundate)
		print("sending content:")
		print(body)
		print("sending to:")
		print(reminder_obj)


		subject = "Reminder: " + subject

		email_message = [reminder_obj[0], subject, body] #[recipients, subject, message content]
		print(email_message)

		# writing the message to the file
		uid = str(uuid.uuid4()) #unique id for a message
		file = open("messages.xml", "a+")
		file.write("<message id='" + uid + "'>")
		file.write("<to>")
		for recipient in reminder_obj[0]:
			file.write(recipient + ",")
		file.write("</to>")
		file.write("<subject>" + subject + "</subject>")
		file.write("<body>" + body + "</body>")
		file.write("</message>")
		file.close()

		#schedule cron job to send email_message at rundate
		print(str(rundate))
		attime = rundate.strftime("%H:%M %B %d %Y")
		print(attime)
		# job = cron.new(attime + "python2.7 reminder.py")
		# cron.write()
		# need bash statement to access crontab


		print('echo "python remind.py ' + uid + '" | at ' + attime)

		os.system('echo "python remind.py ' + uid + '" | at ' + attime)



    # if()
pop_conn.quit()
#print ('hello world')