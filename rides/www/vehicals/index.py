import frappe

def get_context(context):
    context.no_cach = 1
    context.vehicals = frappe.get_all("Vehical", fields=["name", "make", "model", "year"])
    return context