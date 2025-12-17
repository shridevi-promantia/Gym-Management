# Copyright (c) 2025, Shridevi Shrishail Madiwalar and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe.model.document import Document
from frappe.utils import validate_email_address


class GymMember(Document):

    def validate(self):
        self.validate_email()

    def validate_email(self):
        if self.email:
            # validate_email_address throws error automatically if invalid
            validate_email_address(self.email, throw=True)
