
import frappe

def execute():
    """
    Patch to update all existing Gym Locker Booking records
    and set the status field to 'Available'.
    """
    frappe.reload_doc("Gym Management", "doctype", "gym_locker_booking")  # reload DocType

    # Update all records
    frappe.db.sql("""
        UPDATE `tabGym Locker Booking`
        SET status = 'Available'
        WHERE status IS NULL OR status != 'Available'
    """)
    frappe.db.commit()

    print("All Gym Locker Booking records updated to status = 'Available'")
