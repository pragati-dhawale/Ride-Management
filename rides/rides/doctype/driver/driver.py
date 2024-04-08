# Copyright (c) 2024, Pragati Dhawale and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from datetime import datetime
from frappe.utils import getdate


# class Driver(Document):
# 	pass
class Driver(Document):
	

	def validate(self):
		# print(self.first_name)
		self.set_full_name()
		self.calculate_age()
		
	# 	self.set_full_name()
	# 	self.calculate_age()

	def set_full_name(self):
		self.full_name=f"{self.first_name} {self.last_name}"
	

	def calculate_age(self):
		print(getdate())
		# today = datetime.today()
		# year =today.year
		year= getdate().year
		dob = self.date_of_birth.split('-')
		print (dob)
		self.age = year -int (dob[0])
	# 	self.age= year int(dob[0])
