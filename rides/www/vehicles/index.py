# import frappe
# def get_context(context):
#     context.no_cache = 1
#     context.vehicles=frappe.get_all("Vehicle",fields=["name","make","model","status"])
#     return context

import frappe

def get_context(context):
    context.no_cache = 1
    context.vehical = frappe.get_all("Vehical", fields=["name", "make", "model", "year"])
    return context
