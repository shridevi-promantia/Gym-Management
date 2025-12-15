frappe.realtime.on("new_subscription_alert", (data) => {
    frappe.show_alert({
        message: `
            <b>New Subscription!</b><br>
            Member: ${data.member}<br>
            Plan: ${data.plan}<br>
            Date: ${data.date}<br>
            Contact: ${data.contact}
        `,
        indicator: 'green'
    }, 10);
});
