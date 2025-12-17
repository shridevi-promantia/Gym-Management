import frappe

def execute(filters=None):
    if not filters:
        filters = {}

    columns = [
        {
            "label": "Month",
            "fieldname": "month",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": "Total Revenue",
            "fieldname": "total_revenue",
            "fieldtype": "Currency",
            "width": 180
        },
        {
            "label": "Membership Count",
            "fieldname": "membership_count",
            "fieldtype": "Int",
            "width": 180
        }
    ]

    conditions = ""
    values = {}

    # From Date filter
    if filters.get("from_date"):
        conditions += " AND start_date >= %(from_date)s"
        values["from_date"] = filters["from_date"]

    # To Date filter
    if filters.get("to_date"):
        conditions += " AND start_date <= %(to_date)s"
        values["to_date"] = filters["to_date"]

    data = frappe.db.sql(
        f"""
        SELECT
            DATE_FORMAT(start_date, '%%M %%Y') AS month,
            SUM(amount) AS total_revenue,
            COUNT(name) AS membership_count
        FROM `tabGym Membership`
        WHERE
            docstatus = 1
            AND payment_status = 'Paid'
            AND status IN ('Active', 'Expired')
            {conditions}
        GROUP BY YEAR(start_date), MONTH(start_date)
        ORDER BY YEAR(start_date), MONTH(start_date)
        """,
        values,
        as_dict=True
    )

    return columns, data
