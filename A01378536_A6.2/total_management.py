# -*- coding: utf-8 -*-
"""
6.2 Ejercicio de programación 3 y pruebas de unidad

Hotel Management
Customer Management
Reservation Management
"""

import os.path
import pandas as pd

# pylint: disable=R0913


class HotelManagement:
    """Class that manages hotels (create, delete, display, modify"""
    def create(self, name, address, rating):
        """Creates a hotel if the name does not exists in the csv file"""
        data = {'name': name, 'address': address, 'rating': rating}

        if os.path.isfile('hotel.csv'):
            file_df = pd.read_csv('hotel.csv')
            if (file_df == name).any().any():
                return "Hotel already registered"
            data_df = pd.DataFrame(data=data, index=[len(file_df)])
            frames = [file_df, data_df]
            final_df = pd.concat(frames)
            final_df.to_csv('hotel.csv', index=False)
            return "Hotel created"
        data_df = pd.DataFrame(data=data, index=[0])
        data_df.to_csv('hotel.csv', index=False)
        return "Hotel created"

    def delete(self, name):
        """Deletes a hotel if the name does exists in the csv file"""
        if os.path.isfile('hotel.csv'):
            file_df = pd.read_csv('hotel.csv')
            if (file_df == name).any().any():
                index_name = file_df[file_df['name'] == name].index
                file_df = file_df.drop(index_name)
                file_df.to_csv('hotel.csv', index=False)
                return "Hotel deleted"
            return "Hotel not registered"
        return "Hotel register missing"

    def display(self, name):
        """Displays a hotel if the name does exists in the csv file"""
        if os.path.isfile('hotel.csv'):
            file_df = pd.read_csv('hotel.csv')
            if (file_df == name).any().any():
                hotel_info = file_df[file_df['name'] == name]
                return hotel_info
            return "Hotel not registered"
        return "Hotel register missing"

    def modify(self, name, address, rating):
        """Modifies a hotel if the name does exists in the csv file"""
        data = {'name': name, 'address': address, 'rating': rating}

        if os.path.isfile('hotel.csv'):
            file_df = pd.read_csv('hotel.csv')
            if (file_df == name).any().any():
                index_name = file_df[file_df['name'] == name].index
                file_df = file_df.drop(index_name)
                data_df = pd.DataFrame(data=data, index=[index_name])
                frames = [file_df, data_df]
                final_df = pd.concat(frames)
                final_df.to_csv('hotel.csv', index=False)
                return "Hotel modified"
            return "Hotel not registered"
        return "Hotel register missing"


class CustomerManagement:
    """Class that manages customer (create, delete, display, modify"""
    def create(self, name, lastname, number):
        """Creates a cutomer if the name does not exists in the csv file"""
        data = {'name': name, 'lastname': lastname, 'number': number}

        if os.path.isfile('customer.csv'):
            file_df = pd.read_csv('customer.csv')
            if (file_df[file_df['name'] == name]
                    ['lastname'] == lastname).any().any():
                return "Customer already registered"
            data_df = pd.DataFrame(data=data, index=[len(file_df)])
            frames = [file_df, data_df]
            final_df = pd.concat(frames)
            final_df.to_csv('customer.csv', index=False)
            return "Customer created"
        data_df = pd.DataFrame(data=data, index=[0])
        data_df.to_csv('customer.csv', index=False)
        return "Customer created"

    def delete(self, name, lastname):
        """Deletes a customer if the name does exists in the csv file"""
        if os.path.isfile('customer.csv'):
            file_df = pd.read_csv('customer.csv')
            if (file_df[file_df['name'] == name]
                    ['lastname'] == lastname).any().any():
                index_name = file_df[(file_df['name'] == name)
                                     & (file_df['lastname'] == lastname)].index
                file_df = file_df.drop(index_name)
                file_df.to_csv('customer.csv', index=False)
                return "Customer deleted"
            return "Customer not registered"
        return "Customer register missing"

    def display(self, name, lastname):
        """Displays a customer if the name does exists in the csv file"""
        if os.path.isfile('customer.csv'):
            file_df = pd.read_csv('customer.csv')
            if (file_df[file_df['name'] == name]
                    ['lastname'] == lastname).any().any():
                customer_info = file_df[(file_df['name'] == name)
                                        & (file_df['lastname'] == lastname)]
                return customer_info
            return "Customer not registered"
        return "Customer register missing"

    def modify(self, name, lastname, n_name, n_lastname, n_number):
        """Modifies a customer if the name does exists in the csv file"""
        data = {'name': n_name, 'lastname': n_lastname, 'number': n_number}

        if os.path.isfile('customer.csv'):
            file_df = pd.read_csv('customer.csv')
            if (file_df[file_df['name'] == name]
                    ['lastname'] == lastname).any().any():
                index_name = file_df[(file_df['name'] == name)
                                     & (file_df['lastname'] == lastname)].index
                file_df = file_df.drop(index_name)
                data_df = pd.DataFrame(data=data, index=[index_name])
                frames = [file_df, data_df]
                final_df = pd.concat(frames)
                final_df.to_csv('customer.csv', index=False)
                return "Customer modified"
            return "Customer not registered"
        return "Customer register missing"


class BookingManagement:
    """Class that manages customer (create, delete, display, modify"""
    def create(self, name, lastname, hotel, date):
        """Creates a reservation if hotel, customer and dates are available"""
        hotel_management = HotelManagement()
        hotel_res = hotel_management.display(hotel)
        customer_management = CustomerManagement()
        customer_res = customer_management.display(name, lastname)

        if isinstance(hotel_res, str):
            if hotel_res in ("Hotel register missing",
                             "Hotel not registered"):
                return hotel_res
        if isinstance(customer_res, str):
            if customer_res in ("Customer register missing",
                                "Customer not registered"):
                return customer_res

        hotel_res = hotel_res.rename(columns={'name': 'hotel'})

        if os.path.isfile('reservation.csv'):
            file_df = pd.read_csv('reservation.csv')
            if (file_df[(file_df['name'] == name) &
                        (file_df['lastname'] == lastname) &
                        (file_df['hotel'] == hotel)]
                    ['date'] == date).any().any():
                return "Reservation already registered"
            data_df = pd.concat([customer_res, hotel_res], axis=1)
            data_df['date'] = date
            frames = [file_df, data_df]
            final_df = pd.concat(frames)
            final_df.to_csv('reservation.csv', index=False)
            return "Reservation created"
        data_df = pd.concat([customer_res, hotel_res], axis=1)
        data_df['date'] = date
        data_df.to_csv('reservation.csv', index=False)
        return "Reservation created"

    def cancel(self, name, lastname, hotel, date):
        """Cancels a reservation if it exists in the register"""
        if os.path.isfile('reservation.csv'):
            file_df = pd.read_csv('reservation.csv')
            if (file_df[(file_df['name'] == name) &
                        (file_df['lastname'] == lastname) &
                        (file_df['hotel'] == hotel)]
                    ['date'] == date).any().any():
                index_name = file_df[(file_df['name'] == name) &
                                     (file_df['lastname'] == lastname) &
                                     (file_df['hotel'] == hotel) &
                                     (file_df['date'] == date)].index
                file_df = file_df.drop(index_name)
                file_df.to_csv('reservation.csv', index=False)
                return "Reservation canceled"
            return "Reservation not registered"
        return "Reservation register missing"
