#######################################################################
#   customer.py
#   This is the Customer class file
#   Written by: Ali Ba Wazir, May 2018
#######################################################################

class Customer():
    customers = [] # temporary list to act as database

    def __init__(self, name, phone_num):
        if name is None or type(name) is not str:
            raise ValueError('invalid argument: name')
        elif phone_num is None or type(phone_num) is not str:
            raise ValueError('invalid argument: phone_num')
        self.name = name
        self.phone_num = phone_num

        # add new customer to customers list if not already existed
        #self.add_to_list()

    def is_added_to_list(self):
        found= False
        for customer in Customer.customers:
            if customer.name == self.name and\
                customer.phone_number == self.phone_number:
                found = True
        return found

    def add_to_list(self):
        if not self.is_added_to_list():
            Customer.customers.append(self)

    def remove_from_list(self):
        for customer in Customer.customers:
            if customer.name == self.name and\
                customer.phone_number == self.phone_number:
                Customer.customers.remove(customer)
