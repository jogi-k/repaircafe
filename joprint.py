import cups
conn = cups.Connection()
printers = conn.getPrinters ()
prin = conn.getDefault()
myfile = "Reparaturblatt_filled.pdf"
conn.printFile (prin, myfile, "Project Report", {})

