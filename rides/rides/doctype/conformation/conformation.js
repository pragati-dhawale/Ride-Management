// Copyright (c) 2024, Pragati Dhawale and contributors
// For license information, please see license.txt

frappe.ui.form.on("conformation", {
	refresh(frm) {

	},
});

frappe.ui.form.on("Cost Breakup",{  
     amount(frm,cdt,cdn){
        let total =0;
        frm.doc.cost_breakup.forEach(function(d){
            total += parseInt(d.amount);
        });
        frm.set_value("total",total);
     }

    })