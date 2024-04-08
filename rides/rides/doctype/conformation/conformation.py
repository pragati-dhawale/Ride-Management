# # Copyright (c) 2024, Pragati Dhawale and contributors
# # For license information, please see license.txt
import frappe
from frappe.model.document import Document
from frappe import _ 
from frappe.utils import cint


class conformation(Document):
    def validate(self):        
         self.check_minimum_cost_of_petrol()
    def check_minimum_cost_of_petrol(self):
        minimum_cost_for_petrol= frappe.db.get_single_value("Ride Settings","minimum_cost_for_petrol")

        for row in self.cost_breakup:
            if row.item == "Petrol" and cint(row.amount) < minimum_cost_for_petrol:                
                frappe.throw(_("Cost of petrol can't be less than {0}.").format(minimum_cost_for_petrol))
