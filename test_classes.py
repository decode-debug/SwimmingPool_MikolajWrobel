from swimming_pool_class import Swimming_pool, Client, Create_client
from swimming_pool_class import List_of_clients, Reservation
from swimming_pool_class import Aviability_and_prices, TimeTable
from numpy import array
# import datetime as dt
from pandas import DataFrame
import json


def test_Swimming_pool_class():
    pool = Swimming_pool("Maly", "Poniedzialek", 1)
    assert pool


def test_Swimming_pool_get_working_hours():
    pool = Swimming_pool("Maly", "Poniedzialek", 1)
    assert pool.get_working_hours() == [900, 2000]


def test_Swimming_pool_get_name():
    pool = Swimming_pool("Maly", "Poniedzialek", 1)
    assert pool.get_name() == 'Maly'


def test_Swimming_pool_get_day():
    pool = Swimming_pool("Maly", "Poniedzialek", 1)
    assert pool.get_day() == 'Poniedzialek'


def test_Swimming_pool_get_tracks():
    pool = Swimming_pool("Maly", "Poniedzialek", 1)
    assert pool.get_tracks() == 1


def test_Swimming_pool_load_working_hours():
    pool = Swimming_pool("Maly", "Poniedzialek", 1)
    assert pool.load_working_hours() == [900, 2000]


def test_set_working_hours():
    pool = Swimming_pool("Maly", "Poniedzialek", 1)
    assert pool.load_working_hours() == [900, 2000]
    pool.set_working_hours([900, 2000])


def test_Client_as_customer():
    client = Client(666999, "Ania Makota", 0, 0)
    assert client


def test_Client_as_group():
    client = Client(666999, "Pletweka", 0, 1, 69)
    assert client


def test_Client_maturity_group():
    client = Client(666999, "Pletweka", 0, 1, 69)
    assert client.maturity() == 0


def test_Client_class_or_cust_group():
    client = Client(666999, "Pletweka", 0, 1, 69)
    assert client.class_or_cust() == 1


def test_Client_group_size_group():
    client = Client(666999, "Pletweka", 0, 1, 69)
    assert client.group_size() == 69


def test_Client_name():
    client = Client(666999, "Ania Makota", 0, 0)
    assert client.name() == "Ania Makota"


def test_Client_maturityas_customer():
    client = Client(666999, "Ania Makota", 0, 0)
    assert client.maturity() == 0


def test_Client_class_or_custas_customer():
    client = Client(666999, "Ania Makota", 0, 0)
    assert client.class_or_cust() == 0


def test_Client_group_sizeas_customer():
    client = Client(666999, "Ania Makota", 0, 0)
    assert client.group_size() == 1


def test_Client__str__():
    pass


def test_create_client_input_class_or_cust():
    pass


def test_Aviability_and_prices_track_aviable():
    aviability = Aviability_and_prices()
    pass


def test_TimeTable():
    timetable = TimeTable()

    def import_Data_from_Reservations():
        file = "Reservations.json"
        with open(file, 'r') as json_file:
            Data = json.load(json_file)
        Data = Data["Data"]
        return Data

    def table():
        """Sorts and decrypts Data"""
        Data = []
        if len(Data) == 0:
            Data = import_Data_from_Reservations()
        list_numbers, list_starting_hour, list_ending_hour, list_track = list(map(list, zip(*sorted(Data))))
        Table = DataFrame(array([list_numbers, list_starting_hour, list_ending_hour, list_track]), index=["clent's_number", "starting_hour", "ending_hour", "track"]).transpose()

        return Table
    assert timetable.table() == table()
