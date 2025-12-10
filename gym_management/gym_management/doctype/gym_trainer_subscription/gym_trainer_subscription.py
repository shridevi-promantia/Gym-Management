# Copyright (c) 2025, Shridevi Shrishail Madiwalar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class GymTrainerSubscription(Document):
	def on_submit(doc, method=None):
		print("🚀 Trainer Alert Event Fired!", doc.user)

		if doc.user:
			frappe.publish_realtime(
				event='new_subscription_alert',
				message={
					"member": doc.member,
					"plan": doc.membership_plan,
					"date": doc.subscription_date,
					"contact": doc.contact_number
				},
				user=doc.user
			)
