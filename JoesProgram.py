import JoesClass as J

name = "John Doe"
address = "123 Main St. Waco TX 76706"
phone = "214-555-1112"
carmake = "Honda"
carmodel = "Accord LX"
caryear = 2016
parts = 1210.5
labor = 765.00


customer = J.customer(name, address, phone)
car = J.car(carmake, carmodel, caryear)
service = J.service(parts, labor)

print(f"Customer: {customer.get_name()}  Address: {customer.get_address()}  Phone: {customer.get_phone()}")
print(f"Car Make: {car.get_carmake()}  Car Model: {car.get_carmodel()}  Car Year: {car.get_caryear()}")
print()
print("Service Quote")
print()
print(f"Parts: ${service.get_parts()}")
print(f"labor: ${service.get_labor()}")
print(f"Sales Tax: ${round(service.get_sale_tax(), 2)}")
print(f"Total Charges: ${round(service.set_total_charges(), 2)}")
