from terminaltables import AsciiTable
table_data = [
    ('id', 'invoice_no', "supplier_level", "container_name", "temp", "item_categories", "contractual_documents", "shipment_received", "document_submission_date"),
    ('0', '001', '1', 'Jina', '25 cc','rice', 'Packing List', "01-01-2019",'01-01-2019')
]
table = AsciiTable(table_data)
print (table.table)

def add():
    id = input("Enter id: ")
    invoice_no = input("Enter invoice number: ")
    supplier_level = input("Enter supplier_level: ")
    container_name = input("Enter container_name: ")
    temp = input("Enter temperature. Choose between dry, reeefer or chilled:  ")
    item_categories = input("Enter item_category: ")
    contractual_documents = input("Enter contractual_documents: ")
    shipment_received = input("Enter shipment_received date: ")
    document_submission_date = input("Enter document submission date: ")

    new = (id, invoice_no, supplier_level, container_name, temp, item_categories, contractual_documents, shipment_received, document_submission_date )
    table_data.append(new)
    return table.table
print(add())
