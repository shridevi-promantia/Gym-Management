import frappe
import random
from frappe.model.document import Document

class GymLockerBooking(Document):

    def before_insert(self):
        # 1️⃣ Prevent same member from booking twice
        self.prevent_duplicate_booking()

        # 2️⃣ Assign random locker number
        self.assign_random_locker()

    def prevent_duplicate_booking(self):
        if not self.member:
            return

        existing = frappe.db.exists(
            "Gym Locker Booking",
            {
                "member": self.member
            }
        )

        if existing:
            frappe.throw(
                f"Member <b>{self.member}</b> already has a locker booking."
            )

    def assign_random_locker(self):
        number = random.randint(1, 100)
        self.locker_number = str(number)
