class customer:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    def set_name(self, name):
        self.name = name
    def set_address(self, address):
        self.address = address
    def set_phone(self, phone):
        self.phone = phone

    def get_name(self):
        return self.name
    def get_address(self):
        return self.address
    def get_phone(self):
        return self.phone
    

class car:
    def __init__(self, carmake, carmodel, caryear):
        self.carmake = carmake
        self.carmodel = carmodel
        self.caryear = caryear

    def set_carmake(self, carmake):
        self.carmake = carmake
    def set_carmodel(self, carmodel):
        self.carmodel = carmodel
    def set_caryear(self, caryear):
        self.caryear = caryear

    def get_carmake(self):
        return self.carmake
    def get_carmodel(self):
        return self.carmodel
    def get_caryear(self):
        return self.carmodel
    
    
class service:
    def __init__(self, parts, labor):
        self.parts = parts
        self.labor = labor
        self.sale_tax = .0825
        self.total_cost = 0

    def set_parts(self, parts):
        self.parts = parts
    def set_labor(self, labor):
        self.labor = labor

    def get_parts(self):
        return self.parts
    def get_labor(self):
        return self.labor
    def get_sale_tax(self):
        self.total_cost = self.parts + self.labor
        self.sales_tax = self.total_cost * .0825
        return self.sales_tax
    def set_total_charges(self):
        total = self.total_cost + self.sales_tax
        return total
