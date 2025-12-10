# Copyright (c) 2025, Shridevi Shrishail Madiwalar and contributors
# For license information, please see license.txt

# import frappe


import frappe

def execute(filters=None):
    columns = [
        {
            "label": "Active Plan",
            "fieldname": "active_plan",
            "fieldtype": "Data",
            "width": 200,
        },
        {
            "label": "Total Revenue",
            "fieldname": "revenue",
            "fieldtype": "Currency",
            "width": 150,
        },
    ]

    # Fetch Subscription Records
    records = frappe.get_all(
        "Gym Subscription",
        fields=["amount", "active_plan"],
        filters={"active_plan": ["!=", ""]}  # avoid null plan
    )

    revenue_by_plan = {}

    # Summarize revenue by each active plan
    for record in records:
        plan = record.active_plan
        amount = record.amount or 0

        if plan in revenue_by_plan:
            revenue_by_plan[plan] += amount
        else:
            revenue_by_plan[plan] = amount

    data = []
    for plan, revenue in revenue_by_plan.items():
        data.append({
            "active_plan": plan,
            "revenue": revenue
        })

    return columns, data
