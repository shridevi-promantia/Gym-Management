import frappe

def get_context(context):
    context.plans = frappe.get_all(
        "Gym Workout Plan",
        filters={"is_published": 1},
        fields=["name", "plan_name", "level", "description"]
    )
