// Copyright (c) 2025, Shridevi Shrishail Madiwalar and contributors
// For license information, please see license.txt

frappe.query_reports["Fitness Journey Report"] = {
    "filters": [
        {
            "fieldname": "gym_member",
            "label": "Gym Member",
            "fieldtype": "Link",
            "options": "Gym Member"
        }
    ],
    "formatter": function(value, row, column, data, default_formatter) {
        value = default_formatter(value, row, column, data);
        
        // Make Gym Member clickable
        if (column.fieldname === "gym_member" && value) {
            value = <a href="#" class="gym-member-link" data-member="${data.gym_member}">${value}</a>;
        }
        return value;
    },
    "onload": function(report) {
        // Add click event for Gym Member links
        $(document).on("click", ".gym-member-link", function(e) {
            e.preventDefault();
            let member = $(this).data("member");
            
            // Set filter and refresh report
            frappe.query_report.set_filter_value("gym_member", member);
            frappe.query_report.refresh();
        });
    }
};
