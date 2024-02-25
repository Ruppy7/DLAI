import csv

# Parse Invoice Function
def parse_invoice(text):
    invoice_data = {}

    # Extract invoice number, invoice date, and payment date
    for line in text.split('\n'):
        if "Invoice no." in line:
            invoice_data["Invoice Number"] = line.split("Invoice no.")[-1].strip()
        elif "Payment date" in line:
            invoice_data["Payment Date"] = line.split("Payment date:")[-1].strip()

    # Extract sender's and recipient's information
    sender_info = []
    recipient_info = []
    is_recipient = False
    for line in text.split('\n'):
        if "Payment:" in line:
            is_recipient = True
        if not is_recipient:
            sender_info.append(line)
        else:
            recipient_info.append(line)

    invoice_data["Sender"] = ' '.join(sender_info)
    invoice_data["Recipient"] = ' '.join(recipient_info)

    # Extract item details
    items = []
    start_parsing_items = False
    for line in text.split('\n'):
        if "Sales" in line:
            start_parsing_items = True
            continue
        if start_parsing_items and line.strip():
            parts = line.split()
            if len(parts) >= 5:  # Assuming the line contains item details
                description = ' '.join(parts[:-4])
                quantity = parts[-4]
                unit_price = parts[-3]
                total = parts[-2]
                items.append({
                    "Description": description,
                    "Quantity": quantity,
                    "Unit Price": unit_price,
                    "Total": total
                })

    invoice_data["Items"] = items

    # Extract total amount
    for line in text.split('\n'):
        if "Total CHF" in line:
            invoice_data["Total Amount"] = line.split("Total CHF")[-1].strip()

    return invoice_data

def save_to_csv(invoice_data, csv_file):
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ["Invoice Number", "Invoice Date", "Payment Date", "Total Amount", "Sender", "Recipient", "Description", "Quantity", "Unit Price", "Total"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Write main invoice data
        writer.writerow({
            "Invoice Number": invoice_data["Invoice Number"],
            "Payment Date": invoice_data["Payment Date"],
            "Total Amount": invoice_data["Total Amount"],
            "Sender": invoice_data["Sender"],
            "Recipient": invoice_data["Recipient"],
            "Description": "",  # Leave these fields empty for the main invoice data
            "Quantity": "",
            "Unit Price": "",
            "Total": ""
        })

        # Write item data
        for item in invoice_data["Items"]:
            writer.writerow({
                "Description": item["Description"],
                "Quantity": item["Quantity"],
                "Unit Price": item["Unit Price"],
                "Total": item["Total"],
                "Invoice Number": "",
                "Invoice Date": "",
                "Payment Date": "",
                "Total Amount": "",
                "Sender": "",
                "Recipient": ""
            })


# Test with the invoice text
invoice_text = """
D. Brawn Manufacture     

Invoice no. DVT-AX-345678

Payment date: 03/12/2006 

Reference Designation Qty Unit price Total CHF Sales
Work
SERVICE D COMPLETE OVERHAUL 1 5500.00 5500.00 220
SERVICE D REFRESHING COMPLETE CASE 1 380.00 380.00 220
AND RHODIUM BATH
Exterior parts:
JO.297.065.FP FLAT GASKET 1 3.00 3.00 220
JO.197.075.FP FLAT GASKET 1 4.00 4.00 220
JO.199.059.0S FLAT ROUND GASKET 1 6.00 6.00 220
VI.261.036.BC W.G.FIXATION SCREWS 10 4.00 40.00 220
Al.465.055.BC WHITE GOLD "FOIL" 1 70.00 70.00 220
PAIR OF HAND
LENGTH: 10/13.50MM
CALIBRE 2868
SPECIAL DISCOUNT -3003.00 -3003.00
Discount -900.00 -900.00
Total CHF 2100.00
RETURN AFTER REPAIR
NO COMMERCIAL VALUE
Payment:
Mr. John Doe

Green Street 15, Office 4

1234 Vermut

New Caledonia

Credit Card: Visa
Card No: 112345678
"""

invoice_data = parse_invoice(invoice_text)
print("Extracted Invoice Data:")
print(invoice_data)

# Save invoice data to CSV
save_to_csv(invoice_data, "invoice_data.csv")