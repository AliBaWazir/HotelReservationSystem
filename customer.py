'''
    This is the Customer class file
    Copyright (C) <2018>  <Ali Ba Wazir>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

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
