// Copyright (c) 2025, Shridevi Shrishail Madiwalar and contributors
// For license information, please see license.txt
frappe.query_reports["Monthly Revenue Report"] = {
    filters: [
        {
            fieldname: "from_date",
            label: "From Date",
            fieldtype: "Date"
        },
        {
            fieldname: "to_date",
            label: "To Date",
            fieldtype: "Date"
        }
    ]
};
