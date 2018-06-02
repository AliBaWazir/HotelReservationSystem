#######################################################################
#   hotel.py
#   This is the Hotel class file
#   Written by: Ali Ba Wazir, May 2018
#######################################################################

class Hotel():
    hotels = [] # temporary list to act as database

    def __init__(self, number, hotel_name, city, total_rooms):
        if number < 0 or type(number) is not int:
            raise ValueError('invalid argument: number')
        elif hotel_name is None or type(hotel_name) is not str:
            raise ValueError('invalid argument: hotel_name')
        elif city is None or type(city) is not str:
            raise ValueError('invalid argument: city')
        elif total_rooms < 0 or type(total_rooms) is not int:
            raise ValueError('invalid argument: total_rooms')
        self.number = number
        self.name = hotel_name
        self.city = city
        self.total_rooms = total_rooms

        # add the new hotel to hotels list
        #self.add_to_list()

    def is_added_to_list(self):
        found= False
        for hotel in Hotel.hotels:
            if hotel.name == self.name and hotel.city == self.city:
                found = True
        return found

    def add_to_list(self):
        # if the new hotel already exists in list, remove it
        if self.is_added_to_list():
            self.remove_from_list()
        # append the new hotel object to hotels list
        Hotel.hotels.append(self)

    def remove_from_list(self):
        for hotel in Hotel.hotels:
            if hotel.name == self.name and hotel.city == self.city:
                Hotel.hotels.remove(hotel)
