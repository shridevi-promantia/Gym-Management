# Copyright (c) 2025, Shridevi Shrishail Madiwalar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class GymMembershipCard(Document):
    pass


@frappe.whitelist()
def check_print_permission(docname):
    if frappe.session.user != "Administrator":
        frappe.throw(
            "You do not have permission to print or download this document.",
            frappe.PermissionError
        )
    return True
