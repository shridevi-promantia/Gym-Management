import frappe
from frappe.model.document import Document
from frappe.utils import today


class GymMembership(Document):
    pass


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
