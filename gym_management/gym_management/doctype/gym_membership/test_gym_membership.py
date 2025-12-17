import frappe
import unittest
from frappe.utils import add_days, today
from gym_management.gym_management.doctype.gym_membership.gym_membership import (
    auto_expire_memberships
)

class TestGymMembership(unittest.TestCase):

    def setUp(self):
        frappe.set_user("Administrator")

        # Create Gym Member
        self.member = frappe.get_doc({
            "doctype": "Gym Member",
            "member_name": "Test Member",
            "email": "testmember@example.com"
        }).insert(ignore_permissions=True)

    def tearDown(self):
        frappe.db.rollback()

    def test_duration_calculation(self):
        doc = frappe.get_doc({
            "doctype": "Gym Membership",
            "member": self.member.name,
            "start_date": today(),
            "end_date": add_days(today(), 9)
        }).insert(ignore_permissions=True)

        self.assertEqual(doc.duration, 10)

    def test_end_date_before_start_date(self):
        with self.assertRaises(frappe.ValidationError):
            frappe.get_doc({
                "doctype": "Gym Membership",
                "member": self.member.name,
                "start_date": today(),
                "end_date": add_days(today(), -1)
            }).insert(ignore_permissions=True)

    def test_auto_expire_membership(self):
        # Create expired membership
        membership = frappe.get_doc({
            "doctype": "Gym Membership",
            "member": self.member.name,
            "start_date": add_days(today(), -10),
            "end_date": add_days(today(), -1),
            "status": "Active"
        }).insert(ignore_permissions=True)

        auto_expire_memberships()

        membership.reload()
        self.assertEqual(membership.status, "Expired")
