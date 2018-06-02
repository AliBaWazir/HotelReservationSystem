'''
    This is the Hotel class file
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
    
    @staticmethod
    def get_hotels_in_city(city):
        hotels_in_city = []
        if city is None or type(city) is not str:
            print 'get_hotels_in_city: invalid argument: city'
            return hotels_in_city
        for hotel in Hotel.hotels:
            if hotel.city == city:
                hotels_in_city.append(hotel)
        return hotels_in_city
    
    @staticmethod         
    def list_hotels_in_city(city): 
        hotels_in_city = Hotel.get_hotels_in_city(city)
        if len(hotels_in_city) == 0:
            print 'No hotel is found in %s'%city
        else:
            print 'Hotels in %s:'%city
            for hotel in hotels_in_city:
                print '\tHotel Number: %d, Name: %s, Total Rooms: %d'%(hotel.number, hotel.name, hotel.total_rooms)
