#######################################################################
#   tester.py
#   This is the Tester class file
#   Written by: Ali Ba Wazir, May 2018
#######################################################################
import unittest

from hotel import Hotel
from customer import Customer
from reservation import Reservation

class HotelTestCase(unittest.TestCase):
    def setUp(self):
        self.hotel = Hotel(20, 'Rotana', 'Abu Dhabi', 200)

    def tearDown(self):
        self.hotel.remove_from_list()

    def test_01_add_hotel_to_list(self):
        self.hotel.add_to_list()
        #Verify that new_hotel exists in list
        self.assertTrue(self.hotel.is_added_to_list(),
                        msg='new hotel should have been in hotels list')

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
