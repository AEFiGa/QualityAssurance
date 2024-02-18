# -*- coding: utf-8 -*-
"""
6.2 Ejercicio de programación 3 y pruebas de unidad

Hotel Management - UnitTest
"""

import os
import os.path
import unittest
import pandas as pd
from total_management import HotelManagement
from total_management import CustomerManagement
from total_management import BookingManagement

unittest.TestLoader.sortTestMethodsUsing = None


class TestTotal(unittest.TestCase):
    """UnitTest Class"""
    def test_not_file_hotel(self):
        """UnitTest for unexisting file"""
        if os.path.isfile('hotel.csv'):
            os.remove('hotel.csv')
        hotel_management = HotelManagement()
        test1 = hotel_management.display('Hotel_1')
        test2 = hotel_management.delete('Hotel_1')
        test3 = hotel_management.modify('Hotel_1', 'Address_1.1', '3 Stars')
        result_ok = "Hotel register missing"
        self.assertEqual(test1, result_ok)
        self.assertEqual(test2, result_ok)
        self.assertEqual(test3, result_ok)

    def test_create_hotel(self):
        """UnitTest for create"""
        if os.path.isfile('hotel.csv'):
            os.remove('hotel.csv')
        hotel_management = HotelManagement()
        test1 = hotel_management.create('Hotel_1', 'Address_1', '3 Stars')
        test2 = hotel_management.create('Hotel_2', 'Address_2', '4 Stars')
        test3 = hotel_management.create('Hotel_3', 'Address_3', '5 Stars')
        test4 = hotel_management.create('Hotel_1', 'Address_1', '3 Stars')
        result_ok = "Hotel created"
        result_nok = "Hotel already registered"
        self.assertEqual(test1, result_ok)
        self.assertEqual(test2, result_ok)
        self.assertEqual(test3, result_ok)
        self.assertEqual(test4, result_nok)

    def test_delete_hotel(self):
        """UnitTest for delete"""
        if os.path.isfile('hotel.csv'):
            os.remove('hotel.csv')
        hotel_management = HotelManagement()
        hotel_management.create('Hotel_1', 'Address_1', '3 Stars')
        hotel_management.create('Hotel_2', 'Address_2', '4 Stars')
        hotel_management.create('Hotel_3', 'Address_3', '5 Stars')

        hotel_management = HotelManagement()
        test1 = hotel_management.delete('Hotel_3')
        test2 = hotel_management.delete('Hotel_4')
        result_ok = "Hotel deleted"
        result_nok = "Hotel not registered"
        self.assertEqual(test1, result_ok)
        self.assertEqual(test2, result_nok)

    def test_display_hotel(self):
        """UnitTest for display"""
        if os.path.isfile('hotel.csv'):
            os.remove('hotel.csv')
        hotel_management = HotelManagement()
        hotel_management.create('Hotel_1', 'Address_1', '3 Stars')
        hotel_management.create('Hotel_2', 'Address_2', '4 Stars')

        hotel_management = HotelManagement()
        test1 = hotel_management.display('Hotel_1')
        test2 = hotel_management.display('Hotel_3')
        data = {'name': 'Hotel_1', 'address': 'Address_1', 'rating': '3 Stars'}
        test_df = pd.DataFrame(data=data, index=[0])
        result_ok = test_df.equals(test1)
        result_nok = "Hotel not registered"
        self.assertTrue(result_ok)
        self.assertEqual(test2, result_nok)

    def test_modify_hotel(self):
        """UnitTest for modify"""
        if os.path.isfile('hotel.csv'):
            os.remove('hotel.csv')
        hotel_management = HotelManagement()
        hotel_management.create('Hotel_1', 'Address_1', '3 Stars')
        hotel_management.create('Hotel_2', 'Address_2', '4 Stars')

        hotel_management = HotelManagement()
        test1 = hotel_management.modify('Hotel_1', 'Address_1.1', '3 Stars')
        test2 = hotel_management.modify('Hotel_3', 'Address_3.1', '5 Stars')
        result_ok = "Hotel modified"
        result_nok = "Hotel not registered"
        self.assertEqual(test1, result_ok)
        self.assertEqual(test2, result_nok)

    def test_not_file_customer(self):
        """UnitTest for unexisting file"""
        if os.path.isfile('customer.csv'):
            os.remove('customer.csv')
        customer_management = CustomerManagement()
        test1 = customer_management.display('Name_1', 'Lastname_1')
        test2 = customer_management.delete('Name_1', 'Lastname_1')
        test3 = customer_management.modify(
            'Name_1', 'Lastname_1', 'Name_1.1', 'Lastname_1.1', '12345')
        result_ok = "Customer register missing"
        self.assertEqual(test1, result_ok)
        self.assertEqual(test2, result_ok)
        self.assertEqual(test3, result_ok)

    def test_create_customer(self):
        """UnitTest for create"""
        if os.path.isfile('customer.csv'):
            os.remove('customer.csv')
        customer_management = CustomerManagement()
        test1 = customer_management.create('Name_1', 'Lastname_1', '12345')
        test2 = customer_management.create('Name_2', 'Lastname_2', '23456')
        test3 = customer_management.create('Name_3', 'Lastname_3', '34567')
        test4 = customer_management.create('Name_1', 'Lastname_1', '12345')
        result_ok = "Customer created"
        result_nok = "Customer already registered"
        self.assertEqual(test1, result_ok)
        self.assertEqual(test2, result_ok)
        self.assertEqual(test3, result_ok)
        self.assertEqual(test4, result_nok)

    def test_delete_customer(self):
        """UnitTest for delete"""
        if os.path.isfile('customer.csv'):
            os.remove('customer.csv')
        customer_management = CustomerManagement()
        customer_management.create('Name_1', 'Lastname_1', '12345')
        customer_management.create('Name_2', 'Lastname_2', '23456')
        customer_management.create('Name_3', 'Lastname_3', '34567')

        customer_management = CustomerManagement()
        test1 = customer_management.delete('Name_3', 'Lastname_3')
        test2 = customer_management.delete('Name_4', 'Lastname_4')
        result_ok = "Customer deleted"
        result_nok = "Customer not registered"
        self.assertEqual(test1, result_ok)
        self.assertEqual(test2, result_nok)

    def test_display_customer(self):
        """UnitTest for display"""
        if os.path.isfile('customer.csv'):
            os.remove('customer.csv')
        customer_management = CustomerManagement()
        customer_management.create('Name_1', 'Lastname_1', '12345')
        customer_management.create('Name_2', 'Lastname_2', '23456')

        customer_management = CustomerManagement()
        test1 = customer_management.display('Name_1', 'Lastname_1')
        test2 = customer_management.display('Name_3', 'Lastname_3')
        data = {'name': 'Name_1', 'lastname': 'Lastname_1', 'number': '12345'}
        test_df = pd.DataFrame(data=data, index=[0])
        test1 = test1[['name', 'lastname']]
        test_df = test_df[['name', 'lastname']]
        result_ok = test_df.equals(test1)
        result_nok = "Customer not registered"
        self.assertTrue(result_ok)
        self.assertEqual(test2, result_nok)

    def test_modify_customer(self):
        """UnitTest for modify"""
        if os.path.isfile('customer.csv'):
            os.remove('customer.csv')
        customer_management = CustomerManagement()
        customer_management.create('Name_1', 'Lastname_1', '12345')
        customer_management.create('Name_2', 'Lastname_2', '23456')

        customer_management = CustomerManagement()
        test1 = customer_management.modify(
            'Name_1', 'Lastname_1', 'Name_1.1', 'Lastname_1.1', '12345')
        test2 = customer_management.modify(
            'Name_3', 'Lastname_3', 'Name_3.1', 'Lastname_3.1', '34567')
        result_ok = "Customer modified"
        result_nok = "Customer not registered"
        self.assertEqual(test1, result_ok)
        self.assertEqual(test2, result_nok)

    def test_not_file_booking(self):
        """UnitTest for unexisting file"""
        if os.path.isfile('hotel.csv'):
            os.remove('hotel.csv')
        if os.path.isfile('customer.csv'):
            os.remove('customer.csv')
        if os.path.isfile('reservation.csv'):
            os.remove('reservation.csv')

        booking_management = BookingManagement()
        test1 = booking_management.create('Name_1', 'Lastname_1',
                                          'Hotel_1', '01/03/24')

        hotel_management = HotelManagement()
        hotel_management.create('Hotel_1', 'Address_1', '3 Stars')
        hotel_management.create('Hotel_2', 'Address_2', '4 Stars')
        hotel_management.create('Hotel_3', 'Address_3', '5 Stars')

        test2 = booking_management.create('Name_1', 'Lastname_1',
                                          'Hotel_1', '01/03/24')

        customer_management = CustomerManagement()
        customer_management.create('Name_1', 'Lastname_1', '12345')
        customer_management.create('Name_2', 'Lastname_2', '23456')
        customer_management.create('Name_3', 'Lastname_3', '34567')

        test3 = booking_management.cancel('Name_1', 'Lastname_1',
                                          'Hotel_1', '01/03/24')

        self.assertEqual(test1, "Hotel register missing")
        self.assertEqual(test2, "Customer register missing")
        self.assertEqual(test3, "Reservation register missing")

    def test_create_booking(self):
        """UnitTest for create"""
        if os.path.isfile('hotel.csv'):
            os.remove('hotel.csv')
        if os.path.isfile('customer.csv'):
            os.remove('customer.csv')
        if os.path.isfile('reservation.csv'):
            os.remove('reservation.csv')

        hotel_management = HotelManagement()
        hotel_management.create('Hotel_1', 'Address_1', '3 Stars')
        hotel_management.create('Hotel_2', 'Address_2', '4 Stars')
        hotel_management.create('Hotel_3', 'Address_3', '5 Stars')

        customer_management = CustomerManagement()
        customer_management.create('Name_1', 'Lastname_1', '12345')
        customer_management.create('Name_2', 'Lastname_2', '23456')
        customer_management.create('Name_3', 'Lastname_3', '34567')

        booking_management = BookingManagement()
        test1 = booking_management.create('Name_1', 'Lastname_1',
                                          'Hotel_1', '01/03/24')
        test2 = booking_management.create('Name_1', 'Lastname_1',
                                          'Hotel_4', '01/03/24')
        test3 = booking_management.create('Name_4', 'Lastname_4',
                                          'Hotel_1', '01/03/24')
        test4 = booking_management.create('Name_1', 'Lastname_1',
                                          'Hotel_1', '01/03/24')
        test5 = booking_management.create('Name_1', 'Lastname_1',
                                          'Hotel_1', '02/03/24')
        self.assertEqual(test1, "Reservation created")
        self.assertEqual(test2, "Hotel not registered")
        self.assertEqual(test3, "Customer not registered")
        self.assertEqual(test4, "Reservation already registered")
        self.assertEqual(test5, "Reservation created")

    def test_cancel_booking(self):
        """UnitTest for delete"""
        if os.path.isfile('hotel.csv'):
            os.remove('hotel.csv')
        if os.path.isfile('customer.csv'):
            os.remove('customer.csv')
        if os.path.isfile('reservation.csv'):
            os.remove('reservation.csv')

        hotel_management = HotelManagement()
        hotel_management.create('Hotel_1', 'Address_1', '3 Stars')
        hotel_management.create('Hotel_2', 'Address_2', '4 Stars')
        hotel_management.create('Hotel_3', 'Address_3', '5 Stars')

        customer_management = CustomerManagement()
        customer_management.create('Name_1', 'Lastname_1', '12345')
        customer_management.create('Name_2', 'Lastname_2', '23456')
        customer_management.create('Name_3', 'Lastname_3', '34567')

        booking_management = BookingManagement()
        booking_management.create('Name_1', 'Lastname_1',
                                  'Hotel_1', '02/03/24')
        test1 = booking_management.cancel('Name_1', 'Lastname_1',
                                          'Hotel_1', '02/03/24')
        test2 = booking_management.cancel('Name_1', 'Lastname_1',
                                          'Hotel_1', '03/03/24')
        result_ok = "Reservation canceled"
        result_nok = "Reservation not registered"
        self.assertEqual(test1, result_ok)
        self.assertEqual(test2, result_nok)


if __name__ == '__main__':
    unittest.main()
