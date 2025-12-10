# Copyright (c) 2025, Shridevi Shrishail Madiwalar and contributors
# For license information, please see license.txt

# import frappe


import frappe

def execute(filters=None):
    filters = filters or {}

    columns = [
        {
            "label": "Date",
            "fieldname": "date",
            "fieldtype": "Date",
            "width": 120,
        },
        {
            "label": "Weight (kg)",
            "fieldname": "weight",
            "fieldtype": "Float",
            "width": 120,
        },
        {
            "label": "Calories Burned",
            "fieldname": "calories",
            "fieldtype": "Int",
            "width": 150,
        },
    ]

    query_filters = {}
    if filters.get("gym_member"):
        query_filters["gym_member"] = filters.get("gym_member")

    records = frappe.get_all(
        "Fitness Journey",
        fields=["date", "weight", "calories"],
        filters=query_filters,
        order_by="date asc"
    )

    data = []
    weight_data = []
    calories_data = []

    for row in records:
        data.append(row)
        if row.date:
            weight_data.append([row.date, row.weight])
            calories_data.append([row.date, row.calories])

    chart = {
        "data": {
            "labels": [d[0] for d in weight_data],
            "datasets": [
                {
                    "name": "Weight Progress",
                    "values": [d[1] for d in weight_data]
                },
                {
                    "name": "Calories Burned",
                    "values": [d[1] for d in calories_data]
                }
            ]
        },
        "type": "line"
    }

    return columns, data, None, chart
