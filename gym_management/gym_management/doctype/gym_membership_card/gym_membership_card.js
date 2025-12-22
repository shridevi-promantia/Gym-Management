// Copyright (c) 2025, Shridevi Shrishail Madiwalar and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Gym Membership Card", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on("Gym Membership Card", {
    refresh(frm) {

        // Override Print action
        frm.page.set_primary_action(__('Print'), () => {
            frappe.call({
                method: "gym_management.gym_management.doctype.gym_membership_card.gym_membership_card.check_print_permission",
                args: {
                    docname: frm.doc.name
                },
                callback: function () {
                    // If permission passes, open print
                    frappe.ui.get_print_settings(frm.doc.doctype, frm.doc.name);
                }
            });
        });
    }
});
