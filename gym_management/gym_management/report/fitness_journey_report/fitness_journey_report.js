frappe.query_reports["Fitness Journey Report"] = {
    filters: [
        {
            fieldname: "gym_member",
            label: "Gym Member",
            fieldtype: "Link",
            options: "Gym Member",
        },
        {
            fieldname: "month",
            label: "Month",
            fieldtype: "Select",
            options: [
                "",
                "January",
                "February",
                "March",
                "April",
                "May",
                "June",
                "July",
                "August",
                "September",
                "October",
                "November",
                "December",
            ],
            default: "",
        },
        {
            fieldname: "year",
            label: "Year",
            fieldtype: "Int",
            default: new Date().getFullYear(),
        },
    ],

    formatter: function (value, row, column, data, default_formatter) {
        value = default_formatter(value, row, column, data);

        if (column.fieldname === "gym_member" && data && data.gym_member) {
            value = `
                <a href="#"
                   class="gym-member-link"
                   data-member="${data.gym_member}">
                   ${value}
                </a>`;
        }

        return value;
    },

    onload: function (report) {
        $(document)
            .off("click", ".gym-member-link")
            .on("click", ".gym-member-link", function (e) {
                e.preventDefault();

                const member = $(this).data("member");
                report.set_filter_value("gym_member", member);
                report.refresh();
            });
    },
};
