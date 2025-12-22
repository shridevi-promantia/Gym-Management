// Copyright (c) 2025, Shridevi Shrishail Madiwalar and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Gym Trainer", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('Gym Trainer', {
    refresh: function(frm) {
        // Add custom button
        frm.add_custom_button('Update Info', function() {
            
            // Create a dialog
            let d = new frappe.ui.Dialog({
                title: 'Update Trainer Info',
                fields: [
                    {
                        fieldname: 'trainer_name',
                        label: 'Trainer Name',
                        fieldtype: 'Data',
                        default: frm.doc.trainer_name
                    },
                    {
                        fieldname: 'email',
                        label: 'Email',
                        fieldtype: 'Data',
                        default: frm.doc.email
                    },
                    {
                        fieldname: 'phone',
                        label: 'Phone',
                        fieldtype: 'Data',
                        default: frm.doc.phone
                    },
                    {
                        fieldname: 'specialization',
                        label: 'Specialization',
                        fieldtype: 'Select',
                        options: 'Strength\nYoga\nZumba\nCardio\nCrossfit',
                        default: frm.doc.specialization
                    }
                ],
                primary_action_label: 'Update',
                primary_action(values) {
                    // Update the DocType fields
                    frm.set_value('trainer_name', values.trainer_name);
                    frm.set_value('email', values.email);
                    frm.set_value('phone', values.phone);
                    frm.set_value('specialization', values.specialization);
                    frm.save(); // Save the document
                    d.hide();   // Close dialog
                }
            });
            
            d.show(); // Show dialog
        });
    }
});
