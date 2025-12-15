import frappe
from frappe.utils import nowdate, add_days

def send_weekly_class_summary():
    # 1. Get last 7 days range
    today = nowdate()
    last_week = add_days(today, -7)

    # 2. Count number of classes in last week
    total_classes = frappe.db.count(
        "Gym Class Booking",
        filters={
            "date": ["between", [last_week, today]]
        }
    )

    # 3. Count bookings per class
    popular = frappe.db.sql("""
        SELECT class_name, COUNT(*) AS total
        FROM `tabGym Class Booking`
        WHERE date BETWEEN %s AND %s
        GROUP BY class_name
        ORDER BY total DESC
        LIMIT 5
    """, (last_week, today), as_dict=True)

    # 4. Format popular class list
    popular_html = ""
    for p in popular:
        popular_html += f"<li>{p.class_name} — {p.total} bookings</li>"

    if not popular_html:
        popular_html = "<li>No classes held this week</li>"

    # 5. Email message
    message = f"""
    <h2>Weekly Gym Class Summary</h2>
    <p><b>Date Range:</b> {last_week} to {today}</p>
    <p><b>Total Class Bookings:</b> {total_classes}</p>

    <h3>Most Popular Classes</h3>
    <ul>
        {popular_html}
    </ul>
    """

    # 6. Get all system managers & trainers (if trainer doctype exists)
    recipients = frappe.get_all("User", filters={"role_profile_name": "System Manager"}, pluck="email")

    if not recipients:
        recipients = ["Administrator"]

    # 7. Send email
    frappe.sendmail(
        recipients=recipients,
        subject="Weekly Class Summary Report",
        message=message
    )

    return "Weekly class summary sent."
