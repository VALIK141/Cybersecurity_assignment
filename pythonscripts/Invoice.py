
class Invoice:
    def __init__(sales, number, description, quantity, unit_price):
        sales.number = number
        sales.product_description = description
        sales.quantity = quantity
        sales.unit_price = unit_price

def getNumber(sales):
    return sales.number
def setNumber (sales, value):
    return f"{sales.number} = {value}"

def getDescription(sales):
    return sales.description
def setDescription(sales, value):
    return f"{sales.description} = {value}"

def getQuantity(sales):
    return sales.quantity
def setQuantity(sales, value):
    if value < 0:
        return {value}
    else: return f"{sales.quantity} = {value}"

def getUnit_price(sales):e
    return sales.unit_price
def setUnit_price(sales, value):
    if value >= 0:
        return f"{sales.unit_price} = {value}"

def getInvoiceAmount(sales):
    return f"{sales.quantity} * {sales.unitprice}"

invoice = Invoice("010", "Nutri_choco", "50", "650.00")

print("number:", invoice.number)
print("description:", invoice.quantity)
print("quantity:", invoice.quantity) 
print("unit_price:", invoice.unit_price)
print("Invoice_Amount:", invoice.getInvoiceAmount())   




