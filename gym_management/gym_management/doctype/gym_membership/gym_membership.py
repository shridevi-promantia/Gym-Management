import frappe
from frappe.model.document import Document
from frappe.utils import today,getdate
from frappe import _


class GymMembership(Document):
    
    def validate(self):
        self.validate_dates_and_duration()
        self.update_status_based_on_date()

    def validate_dates_and_duration(self):
        if self.start_date and self.end_date:
            from frappe.utils import date_diff
            diff = date_diff(self.end_date, self.start_date)

            if diff < 0:
                frappe.throw(_("End Date cannot be before Start Date"))

            # inclusive
            self.duration = diff + 1
        else:
            self.duration = 0
            
    def update_status_based_on_date(self):
        if self.end_date:
            if getdate(self.end_date) < getdate(today()):
                self.status = "Expired"
            else:
                # keep Draft as-is, otherwise Active
                if self.status != "Draft":
                    self.status = "Active"



def auto_expire_memberships():
    """Expire memberships where end_date is today or older"""

    memberships = frappe.get_all(
        "Gym Membership",
        filters={
            "end_date": ["<=", today()],
            "status": "Active"
        },
        fields=["name", "member", "end_date"]
    )

    if not memberships:
        frappe.logger().info("No memberships to expire today")
        return

    for m in memberships:
        # Update status
        frappe.db.set_value("Gym Membership", m.name, "status", "Expired")

        # Fetch member email
        email = frappe.get_value("Gym Member", m.member, "email")

        # Send notification email (if email exists)
        if email:
            frappe.sendmail(
                recipients=[email],
                subject="Your Gym Membership Has Expired",
                message=f"""
Hello,

Your gym membership expired on {m.end_date}.
Please renew to continue accessing the gym.

Regards,
Gym Management Team
"""
            )

        # Log in scheduler log
        frappe.logger().info(f"Expired: {m.name} for member {m.member}")

    frappe.db.commit()
    frappe.logger().info(f"Total Updated: {len(memberships)}")

