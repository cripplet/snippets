from time import strftime

index = 0;

class note(object):
	def __init__(self, name, email, task, date, is_urgent):
		global index
		index += 1
		self.id = index
		self.name = name
		self.email = email
		self.task = task
		self.date = date
		self.urgent = is_urgent
	def __str__(self):
		if self.urgent:
			tmp = " (F)"
		else:
			tmp = ""
		return " (" + str(self.id) + ") " + self.name + " (" + self.email + "):" + tmp + "\n\n\t" + self.task + "\n\ndue " + strftime("%m.%d.%Y, %H:%M CST", self.date)
