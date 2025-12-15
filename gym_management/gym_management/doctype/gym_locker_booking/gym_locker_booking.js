// Copyright (c) 2025, Shridevi Shrishail Madiwalar and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Gym Locker Booking", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on("Gym Locker Booking", {
    refresh(frm) {
        // Only generate if new doc and locker_number is empty
        if (frm.is_new() && !frm.doc.locker_number) {

            // Generate random locker number 1–100
            let number = Math.floor(Math.random() * 100) + 1;

            frm.set_value("locker_number", number.toString());
        }
    }
});
