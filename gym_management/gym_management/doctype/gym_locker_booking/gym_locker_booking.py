import frappe
import random
from frappe.model.document import Document

class GymLockerBooking(Document):

    def before_insert(self):
        """Assign a random locker before inserting the document."""
        number = random.randint(1, 100)  # Random number between 1 and 100
        self.locker_number = str(number)
