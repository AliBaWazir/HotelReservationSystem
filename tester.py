'''
    This is the Tester class file
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

import unittest
import re

from hotel import Hotel
from customer import Customer
from reservation import Reservation

class HotelTestCase(unittest.TestCase):
    def setUp(self):
        self.hotel1 = Hotel(20, 'Rotana', 'Abu Dhabi', 200)
        self.hotel2 = Hotel(21, 'Sheraton', 'Abu Dhabi', 300)

    def tearDown(self):
        self.hotel1.remove_from_list()
        self.hotel2.remove_from_list()

    def test_01_add_hotel_to_list(self):
        self.hotel1.add_to_list()
        #Verify that hotel1 exists in list
        self.assertTrue(self.hotel1.is_added_to_list(),
                        msg='new hotel1 should have been in hotels list')
        self.hotel2.add_to_list()
        #Verify that hotel2 and hotel2 exists in list
        self.assertTrue(self.hotel2.is_added_to_list(),
                        msg='new hotel2 should have been in hotels list')
    
    def test_02_get_hotels_in_city(self):
        #Verify that no hotels in Abu Dhabi initially exist
        hotels = Hotel.get_hotels_in_city('Abu Dhabi')
        self.assertTrue(len(hotels) == 0,
                        msg='No hotels in Abu Dhabi should have been initially existing')
        #Add 2 hotels to list
        self.hotel1.add_to_list()
        self.hotel2.add_to_list()
        #Verify that 2 hotels are in Abu Dhabi
        hotels = Hotel.get_hotels_in_city('Abu Dhabi')
        self.assertTrue(len(hotels) == 2 and\
                        hotels[0] == self.hotel1 and\
                        hotels[1] == self.hotel2,
                        msg='2 hotels in Abu Dhabi should have been existing')

class ReservationTestCase(unittest.TestCase):
    def setUp(self):
        self.hotel = Hotel(1, 'Rotana', 'Abu Dhabi', 3)
        self.hotel.add_to_list()

    def tearDown(self):
        self.hotel.remove_from_list()

    def test_01_reserve_room_from_24_to_28(self):
        check_in_date = '5/24/18'
        check_out_date = '5/28/18'
        customer = Customer('Ali', '+12345678901')
        reservation = Reservation(self.hotel, customer, check_in_date, check_out_date)
        self.assertTrue(reservation.reserve(),
                        msg='a room should have been reserved from %s to %s'\
                        %(check_in_date, check_out_date))

    def test_02_reserve_room_from_24_to_26(self):
        check_in_date = '5/24/18'
        check_out_date = '5/26/18'
        customer = Customer('Ahmed', '+12345678901')
        reservation = Reservation(self.hotel, customer, check_in_date, check_out_date)
        self.assertTrue(reservation.reserve(),
                        msg='a room should have been reserved from %s to %s'\
                        %(check_in_date, check_out_date))

    def test_03_reserve_room_from_25_to_27(self):
        check_in_date = '5/25/18'
        check_out_date = '5/27/18'
        customer = Customer('Heba', '+12345678901')
        reservation = Reservation(self.hotel, customer, check_in_date, check_out_date)
        self.assertTrue(reservation.reserve(),
                        msg='a room should have been reserved from %s to %s'\
                        %(check_in_date, check_out_date))

    def test_04_reserve_room_from_24_to_25(self):
        check_in_date = '5/24/18'
        check_out_date = '5/25/18'
        customer = Customer('Ali', '+16132614041')
        reservation = Reservation(self.hotel, customer, check_in_date, check_out_date)
        self.assertTrue(reservation.reserve(),
                        msg='a room should have been reserved from %s to %s'\
                        %(check_in_date, check_out_date))

    def test_05_reserve_room_from_25_to_27(self):
        check_in_date = '5/25/18'
        check_out_date = '5/27/18'
        customer = Customer('Ali', '+16132614041')
        reservation = Reservation(self.hotel, customer, check_in_date, check_out_date)
        # Hotel is full from 25 to 27
        self.assertFalse(reservation.reserve(),
                        msg='no room should have been reserved from %s to %s'\
                        %(check_in_date, check_out_date))

def suite():
    Suite = unittest.TestSuite()
    Suite.addTest(HotelTestCase('test_01_add_hotel_to_list'))
    Suite.addTest(HotelTestCase('test_02_get_hotels_in_city'))
    Suite.addTest(ReservationTestCase('test_01_reserve_room_from_24_to_28'))
    Suite.addTest(ReservationTestCase('test_02_reserve_room_from_24_to_26'))
    Suite.addTest(ReservationTestCase('test_03_reserve_room_from_25_to_27'))
    Suite.addTest(ReservationTestCase('test_04_reserve_room_from_24_to_25'))
    Suite.addTest(ReservationTestCase('test_05_reserve_room_from_25_to_27'))

    return Suite

def run_tests():
    runner = unittest.TextTestRunner()
    runner.run(suite())

if __name__ == "__main__":
    run_tests()
