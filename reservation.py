'''
    This is the Reservation class file
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

from datetime import datetime
from hotel import Hotel
from customer import Customer
from notification import Notification

class Reservation():
    reservations = [] # temporary list to act as database

    def __init__(self, hotel, customer, check_in_date, check_out_date):
        if hotel is None or not isinstance(hotel, Hotel):
            raise ValueError('invalid argument: hotel')
        elif customer is None or not isinstance(customer, Customer):
            raise ValueError('invalid argument: customer')
        elif check_in_date is None or type(check_in_date) is not str:
            raise ValueError('invalid argument: check_in_date')
        elif check_out_date is None or type(check_out_date) is not str:
            raise ValueError('invalid argument: check_out_date')
        elif datetime.strptime(check_out_date, '%m/%d/%y') <= datetime.strptime(check_in_date, '%m/%d/%y'):
            raise ValueError('check_out_date should be after check_in_date')
        self.hotel = hotel
        self.customer = customer
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.room_index = None #room index will be determined after invoking reservation.reserve()

    def is_added_to_list(self):
        found= False
        for rsrv in Reservation.reservations:
            if rsrv.hotel == self.hotel and\
                rsrv.customer == self.customer and\
                rsrv.check_in_date == self.check_in_date and\
                rsrv.check_out_date == self.check_out_date:
                found = True
        return found

    def add_to_list(self):
        if not self.is_added_to_list():
            Reservation.reservations.append(self)

    def remove_from_list(self):
        for rsrv in Reservation.reservations:
            if rsrv.hotel == self.hotel and\
                rsrv.customer == self.customer and\
                rsrv.check_in_date == self.check_in_date and\
                rsrv.check_out_date == self.check_out_date:
                Reservation.reservations.remove(rsrv)

    def reserve(self):
        '''Invokes the reservation. Returns True if room is reserved successfully, False otherwise'''

        empty_room_indices = []
        retcode = True

        # check if there is at least one empty room in hotel for the time period
        reservable_rooms = self.get_reservable_rooms()
        if len(reservable_rooms) == 0:
            # no empty room is found in hotel for specified time period.
            print 'sorry no available rooms in %s %s between %s and %s'\
            %(self.hotel.name, self.hotel.city, self.check_in_date, self.check_out_date)
            retcode = False
        else:
            # set the reservation room_index to the first empty room index in list
            self.room_index = reservable_rooms[0]

            # add the new reservation into reservation list
            self.add_to_list()

            # print booking confirmation
            print '------------ BOOKING CONFIRMATION ------------'
            print'\t Hotel Name: %s'%self.hotel.name
            print'\t Hotel City: %s'%self.hotel.city
            print'\t Guest Name: %s'%self.customer.name
            print'\t Room Number: %d'%(self.room_index+1)
            print'\t Check-in Date: %s'%self.check_in_date
            print'\t Check-out Date: %s'%self.check_out_date
            print'\t Booked at: %s'%(datetime.now())
            print '----------------------------------------------'

            # send booking confirmation to customer mobile
            message = 'Hi %s,\nThis is to confirm your reservation for hotel %s in %s from %s to %s'\
            %(self.customer.name, self.hotel.name, self.hotel.city, self.check_in_date, self.check_out_date)
            notif = Notification(message)
            #notif.send_text_message(self.customer.phone_num)
        return retcode

    def get_reservable_rooms(self):
        '''Return a list of indices of possible reservable rooms for the given reservation'''

        reservable_rooms_indices = []
        check_in_dt_obj = datetime.strptime(self.check_in_date, '%m/%d/%y')
        check_out_dt_obj = datetime.strptime(self.check_out_date, '%m/%d/%y')

        if  check_out_dt_obj <= check_in_dt_obj:
            print 'get_reservable_rooms: check_out_date: %s should be after check_in_date: %s'\
            %(self.check_in_date, self.check_out_date)
        else:
            total_rooms = self.hotel.total_rooms
            for room_index in range (total_rooms):
                reserved_room_index = False
                # check that this room with room_index is not already reserved with the given time period
                for rsrv in Reservation.reservations:
                    if reserved_room_index:
                        # no need to continue looping through reservations
                        break
                    rsrv_check_in_dt_obj = datetime.strptime(rsrv.check_in_date, '%m/%d/%y')
                    rsrv_check_out_dt_obj = datetime.strptime(rsrv.check_out_date, '%m/%d/%y')

                    if rsrv.hotel.name == self.hotel.name and\
                        rsrv.hotel.city == self.hotel.city and\
                        rsrv.room_index == room_index:
                            #check if booking period is outside reservation period
                            if check_out_dt_obj <= rsrv_check_in_dt_obj:
                                reserved_room_index = False
                            elif check_in_dt_obj >= rsrv_check_out_dt_obj:
                                reserved_room_index = False
                            else:
                                reserved_room_index = True
                # if this room index is not already reserved, return it
                if not reserved_room_index:
                    reservable_rooms_indices.append(room_index)

        return reservable_rooms_indices
