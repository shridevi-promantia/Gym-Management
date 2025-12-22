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
            "label": "Gym Member",
            "fieldname": "gym_member",
            "fieldtype": "Link",
            "options": "Gym Member",
            "width": 180,
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
        {
            "label": "Workout Plan",
            "fieldname": "workouts",
            "fieldtype": "Link",
            "options": "Gym Workout Plan",
            "width": 180,
        },
    ]

    query_filters = {}
    if filters.get("gym_member"):
        query_filters["gym_member"] = filters.get("gym_member")

    records = frappe.get_all(
        "Fitness Journey",
        fields=[
            "date",
            "gym_member",
            "weight",
            "calories",
            "workouts",
        ],
        filters=query_filters,
        order_by="date asc",
    )

    data = []
    labels = []
    weight_values = []
    calorie_values = []

    for row in records:
        data.append(row)

        label = row.get("date") or "N/A"
        labels.append(label)
        weight_values.append(row.get("weight") or 0)
        calorie_values.append(row.get("calories") or 0)

    # ✅ BAR CHART (WORKS FOR 1 OR MANY RECORDS)
    chart = {
        "data": {
            "labels": labels,
            "datasets": [
                {
                    "name": "Weight Progress",
                    "values": weight_values,
                },
                {
                    "name": "Calories Burned",
                    "values": calorie_values,
                },
            ],
        },
        "type": "bar",
    }

    return columns, data, None, chart
