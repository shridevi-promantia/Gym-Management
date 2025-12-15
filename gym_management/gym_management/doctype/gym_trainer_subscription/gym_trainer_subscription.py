from frappe.model.document import Document


class GymTrainerSubscription(Document):
    pass



import frappe

def after_insert(doc, method):
    trainer_user = frappe.db.get_value("Gym Trainer", doc.trainer, "trainer_user")

    if not trainer_user:
        frappe.throw(f"Trainer '{doc.trainer}' does not have a linked User account!")

    # 1️⃣ Real-time popup notification
    frappe.publish_realtime(
        event="trainer_subscription_alert",
        message={
            "member": doc.member,
            "plan": doc.plan_name,
            "start_date": str(doc.subscription_date),
            "status": doc.status
        },
        user=trainer_user
    )

    message = f"""
    Member: {doc.member}<br>
    Plan: {doc.plan_name}<br>
    Subscription Date: {doc.subscription_date}<br>
    Status: {doc.status}
    """

    notification = frappe.get_doc({
        "doctype": "Notification Log",
        "subject": "New Subscription",
        "email_content": message,
        "for_user": trainer_user,
        "document_type": doc.doctype,
        "document_name": doc.name,
        "type": "Alert",
        "read": 0
    })

    notification.insert(ignore_permissions=True)
    frappe.db.commit()
