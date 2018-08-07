import poplib
from email import parser
import email
import reminder_functions
import datetime
import quopri

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
	date = date.replace(", ", ", 0")
	dateobj = datetime.datetime.strptime(date, '%a, %d %b %Y %H:%M:%S')

	if(message.is_multipart()):
		body = message.get_payload(0)
	else:
		body = message.get_payload()
	
	body = quopri.decodestring(str(body))

	reminder_obj = reminder_functions.parseReminder(body)
	
	if not reminder_obj:
		print("no reminder")
	else:
		reminder_for = ""
		# Add in name -> email conversion later
		if(reminder_obj[0] == "me"):
			reminder_for = sender
		elif(reminder_obj[0] == "all"):
			reminder_for = "all@arborventures.com"
		else:
			reminder_for = reminder_obj[0]

		time = reminder_obj[1]

		print("time info:")
		print(time)

		days = int(time["days"])+(int(time["months"])*30)+(int(time["years"])*365)
		

		timed = datetime.timedelta(weeks=int(time["weeks"]), days=days, hours=int(time["hours"]))

		rundate = dateobj + timed
		print("will send on:")
		print(rundate)

		print("sending content:")
		content = body.split("Content-Type")[1].split("\n")[1]

		print("sending to:")
		print(reminder_for)


    # if()
pop_conn.quit()