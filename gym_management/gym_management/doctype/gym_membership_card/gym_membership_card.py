# Copyright (c) 2025, Shridevi Shrishail Madiwalar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class GymMembershipCard(Document):
	pass

@frappe.whitelist()
def get_print_context(**kwargs):
    if frappe.session.user != "Administrator":
        frappe.throw("You are not permitted to print or download this document.")
