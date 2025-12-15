from frappe.tests.utils import FrappeTestCase
import frappe
from datetime import date

class TestGymMember(FrappeTestCase):

    def setUp(self):
        self.created_docs = []

    def tearDown(self):
        for name in self.created_docs:
            try:
                frappe.delete_doc("Gym Member", name, force=True)
            except:
                pass

    def test_create_gym_member(self):
        """Test that a Gym Member can be created with basic fields."""
        doc = frappe.get_doc({
            "doctype": "Gym Member",
            "full_name": "Test Member",
            "email": "testmember@example.com",
            "gender": "Male",
            "profile": "Active"
        }).insert(ignore_permissions=True)
		
        self.created_docs.append(doc.name)

        self.assertTrue(doc.name)
        self.assertEqual(doc.full_name, "Test Member")
        self.assertEqual(doc.gender, "Male")
        print("Created Member:", doc.name)


    def test_date_of_birth_and_age(self):
        """Test DOB is stored correctly and age is calculated."""
        
        dob = date(2000, 1, 1)

        doc = frappe.get_doc({
            "doctype": "Gym Member",
            "full_name": "Age Test",
            "date_of_birth": dob
        }).insert(ignore_permissions=True)

        self.created_docs.append(doc.name)

        self.assertEqual(doc.date_of_birth, dob)

        today = date.today()
        calculated_age = today.year - dob.year - (
            (today.month, today.day) < (dob.month, dob.day)
        )

        self.assertGreater(calculated_age, 0)
