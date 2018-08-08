import re

def checkQuantity(body, array):

	quantity_start = re.search("\d", body)
	if(quantity_start):
		quantity_start = quantity_start.start()
	else:
		return array
	quantity_end = body.find(" ", quantity_start)
	quantity = body[quantity_start:quantity_end]

	units_end = body.find(" ", quantity_end+1)
	# units_end = body.find(" ", quantity_end+1)
	
	if units_end == -1:
		units = body[quantity_end+1:]

		if("hour" in units.lower()):
			array["hours"] = quantity
		elif("day" in units.lower()):
			array["days"] = quantity
		elif("week" in units.lower()):
			array["weeks"] = quantity
		elif("month" in units.lower()):
			array["months"] = quantity
		elif("year" in units.lower()):
			array["years"] = quantity

		return array
	else:
		units = body[quantity_end+1:units_end]
		more = str(body[units_end:])

		if("hour" in units.lower()):
			array["hours"] = quantity
		elif("day" in units.lower()):
			array["days"] = quantity
		elif("week" in units.lower()):
			array["weeks"] = quantity
		elif("month" in units.lower()):
			array["months"] = quantity
		elif("year" in units.lower()):
			array["years"] = quantity

		return checkQuantity(more, array)


def parseReminder(body):
	# body = body.split("Content-Type")
	# if(len(body) > 1):
	# 	body = body[1]
	# else:
	# 	body = body[0]
		
	subject = body.lower().split("remind ")
	if len(subject) < 2:
		return []

	subject = subject[1].split("in")
	if(len(subject) == 1):
		number_pos = re.search("\d", subject[0]).start()
		subject = subject[0][:int(number_pos)]
		subject = re.split('and |, ',subject)
		for i, s in enumerate(subject):
			subject[i] = s.replace(" ", "")
	else:
		subject = subject[0]
		subject = re.split('and |, ',subject)
		for i, s in enumerate(subject):
			subject[i] = s.replace(" ", "")
	

	body = body.split(subject[-1])[1].split("\n")[0]

	obj = checkQuantity(body, {"years":0,"months":0,"weeks":0,"days":0,"hours":0,})

	return [subject, obj]
