// Copyright (c) 2025, Shridevi Shrishail Madiwalar and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Gym Membership Card", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on("Gym Membership Card", {
    refresh(frm) {
        frappe.call({
            method: "frappe.client.get_value",
            args: {
                doctype: "User",
                filters: { "name": frappe.session.user },
                fieldname: ["name"]
            },
            callback: function(r) {
                let current_user = frappe.session.user;

                // Allow only 'Administrator' to print or download
                if (current_user !== "Administrator") {

                    // Hide print button
                    frm.page.hide_icon_group();  

                    // Disable Print action dropdown
                    frm.page.wrapper.find('.menu-btn-group').hide();

                    // Disable print icon
                    frm.page.wrapper.find('.btn-print-print').hide();

                    // Disable PDF icon
                    frm.page.wrapper.find('.btn-download-pdf').hide();
                }
            }
        });
    }
});
