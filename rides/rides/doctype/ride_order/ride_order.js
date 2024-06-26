// Copyright (c) 2024, Pragati Dhawale and contributors
// For license information, please see license.txt


frappe.ui.form.on("Ride Order", {
    refresh(frm) {
        frm.set_query("user", () => {
            return {
                filters: {
                    "ignore_user_type": 1  // Use 1 instead of true for filters
                }
            };
        });

        frm.set_query("vehical",(frm) => {  
            return {
                filters: {
                    "status": "Available"
                }
            };
        });

        if (!frm.doc.__islocal){

            frm.add_custom_button(__("Create Ride"),()=>{
                let dialog = new frappe.ui.Dialog({
                    title: __("Select a Driver"),
                    fields: [  
                        {
                            "fieldname": "driver",
                            "fieldtype": "Link",
                            "label": __("Driver"),
                            "options": "Driver",
                            "reqd": 1
                        }
                    ],
                    primary_action_label: __("Create Ride"),
                    primary_action: (data) => {
                        frappe.new_doc("conformation",{
                            vehical: frm.doc.vehical,
                            driver: data.driver,
                            order:frm.doc.name
                        });
                    }
                });
                dialog.show();
            });
    }
    }
});
