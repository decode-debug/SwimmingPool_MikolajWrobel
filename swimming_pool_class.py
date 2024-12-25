from typing import List
import json
from random import random
from pandas import DataFrame
from numpy import array
import datetime

class Swimming_pool:
    def __init__(self, name, day, tracks=1):
        """
        defining Swimming_pool class
        self :: str
        name :: str
        working_hours :: typle
        """
        self._name = name
        self._day = day
        self._working_hours = Swimming_pool.get_working_hours()
        self._tracks = tracks

    def get_working_hours(self):
        '''asking for workinghours of Swimming_pool'''
        file = "Working_hours_weekly.json"
        with open(file, "r") as json_file:
            Data = json.load(json_file)
        return Data['Week'][f'{self._day}']

    def set_working_hours(self, new_working_hours):
        '''setting workinghours of Swimming_pool'''
        file = "Working_hours_weekly.json"
        with open(file, 'r') as json_file:
            Day = json.load(json_file)
            Day['Week'][f'{self._day}'] = list(new_working_hours)
        with open(file, 'w') as json_file:
            json_file.write(json.dumps(Day))


class Client:
    def __init__(self, number, name, maturity, class_or_cust, group_size=1):
        """
        defining Client class
        self :: str
        name :: str
        maturity :: str
        group_size :: int
        class_or_cust :: bool
        """
        self._name = name
        self._maturity = maturity
        self._group_size = group_size
        self._class_or_cust = class_or_cust
        self._number = number

    def name(self) -> str:
        """returning client's name"""
        return self._name

    def maturity(self) -> str:
        if self._class_or_cust is False:
            if self._maturity == 1:
                return f"Klient {self._name} jest dorosły"
            else:
                return f"Klient {self._name} nie jest dorosły"
        else:
            return f"Szkółka {self._name} ma {self._maturity} dorosłych pływaków"

    def class_or_cust(self) -> str:
        if self._class_or_cust is False:
            return f"{self._name} jest kleintem"
        else:
            return f"{self._name} jest szkółką "

    def group_size(self) -> str:
        return f"{self._name}'s group size is  {self._group_size}"

    def Create_client_from_clientsFile():
        return Create_client.create_client()


class Create_client(Client):
    def __init__(self, number, name, maturity, class_or_cust, group_size=1):
        super().__init__(number, name, maturity, class_or_cust, group_size)

    def input_class_or_cust(self):
        print("Jeśli klient to szółka pływcka podaj 1 w przeciwnym razie 0")
        self._class_or_cust = bool(input())
        if self._class_or_cust is not True or False:
            print("Źle podałeś wartość - podaj 0 lub 1")
            Create_client.input_class_or_cust()

    def input_name(self):
        if self._class_or_cust == 0:
            name = input("Podaj imię i nazwisko klienta")
            if (len(name.split(" ")) == 2):
                self._name = name
            else:
                Create_client.input_name
        elif self._class_or_cust == 1:
            self._name = input("Podaj nazwę szkółki pływackiej")

    def input_group_size(self):
        if self._class_or_cust == 1:
            print("Podaj liczbę osób zamierzających pływać w szkółce")
            self._group_size = input()
        if self._group_size < 0:
            print("Źle podałeś wartość - podaj liczbę od 1 do nieksończoności")
            Create_client.input_group_size()

    def input_marurity(self):
        if self._group_size == 1:
            string = "(jeśli tak podaj 1 w przeciwnym razie 0)"
            maturity = int(input(f"Czy pływak jest dorosły {string}"))
        elif self._group_size > 1:
            maturity = int(input("Podaj liczbę dorosłych pływaków"))
        if maturity <= 0:
            Create_client.input_marurity()

    def create_clients_number(self):
        number = []
        name, surname = self._name.split(" ")
        number.append((ord(name[0]) % 10))
        number.append((ord(surname[0]) % 10))
        number.append()  # ????????????

    def create_client(self):
        Create_client.input_class_or_cust
        Create_client.input_name
        Create_client.input_group_size
        Create_client.input_marurity
        Create_client.create_clients_number
        check = False
        check = List_of_clients.Add_client
        if check is False:
            SystemError("Something went seriously wrong")

    def client_from_file(number):
        List_of_clients.Find_client(number)


class List_of_clients(Create_client):
    def __init__(self, number, name, maturity, class_or_cust,
                 list, group_size=1):
        super().__init__(number, name, maturity, class_or_cust, group_size)
        self._list = list

    def get_list(self):
        with open("clients.json", "r") as json_file:
            data = json.load(json_file)
        self._list = data

    def Find_client(self, number):
        """Check's if client is on list"""
        for client in self._list:
            if client[0] == number:
                return client

    def Add_client(client):
        with open("clients.json", "a") as json_file:
            json_file.truncate()
            json_file.write(' , '.encode())
            json_file.write(json.dumps(client).encode())
            json_file.write(']'.encode())
        List_of_clients.get_list()
        return True


class Reservation:
    def __init__(self, client_id, track, water_entry, booked_hours,):
        """
        client_id :: int
        track :: int
        water_entry :: int
        booked_hours :: int
        """
        self._client_id = client_id
        self._track = track
        self._water_entry = water_entry
        self._booked_hours = booked_hours

    def tracks(self) -> str:
        """Printing track occupied by client"""
        if self._group_size == 1:
            return f"{self._name} occupies track {self._track[0]}"
        if self._class_or_cust == 0:
            a = f"{self._name} occupies track {self._track[0]} "
            b = f"with {self._group_size-1} other customers"
            return a+b
        else:
            a = ""
            for i in self._track:
                a = a + f" {i}"
            return f"group of {self._group_size} named {self._name} occupies tracks{a}"


class Tickets:
    pass


class Aviability_and_prices(Swimming_pool):
    def __init__(self, starting_hour, ending_hour,
                 working_hours, track=(-1), tracks=1):
        """
        defining Aviability_and_prices class
        self :: str
        starting_hour :: int
        ending_hour :: int
        track :: int
        """
        super().__init__(working_hours, tracks)
        self._starting_hour = starting_hour
        self._ending_hour = ending_hour
        self._track = track
        self._swimming_time = ending_hour - starting_hour
        self._Table = None
        self._num_rows = None

    def track_aviable(self) -> bool or int:
        """checks if track is free at asked hour"""
        Table = TimeTable.table()
        datetime_format = "%Y-%m-%d %H:%M:%S"
        starting_hour = datetime.strptime(self._starting_hour, datetime_format)
        ending_hour = datetime.strptime(self._ending_hour, datetime_format)
        filtered_Table = Table[Table['starting_hour'] > 30] #?????????????????????

    def suggest_hour(self):
        for i in range(0, self._num_rows):
            if self._starting_hour <= self._Table.iloc[i, 2]:
                if self._eding_hour >= self._Table.iloc[i, 1]:
                    return self._Table.iloc[i, 2]

    def book_hour(self):
        TimeTable.book(self)


class TimeTable(Aviability_and_prices):
    def __init__(self):
        """stores datatable about reservations"""
        self._Data = []

    def import_Data_from_Reservations(self):
        file = "Reservations.json"
        with open(file, 'r') as json_file:
            Data = json.load(json_file)
        self._Data = Data["Data"]

    def table(self):
        """Sorts and decrypts Data"""
        if len(self._Data) == 0:
            TimeTable.import_Data_from_Reservations()
        else:
            list_numbers, list_starting_hour, list_ending_hour, list_track = list(map(list, zip(*sorted(self._Data))))
            Table = DataFrame(array([list_numbers, list_starting_hour,
                                     list_ending_hour, list_track]),
                              columns=["clent's_number", "starting_hour",
                                       "ending_hour", "track"])
        return Table

    def book(self, name, strating_hour, eding_hour, track):
        """Booking track for client"""
        self._Data.append([name, strating_hour, eding_hour, track])

    def safe_Data_to_Reservations(self):
        file = "Reservations.json"
        with open(file, 'w') as json_file:
            json_file.write(self._Data)


class Finance_raport:
    pass
