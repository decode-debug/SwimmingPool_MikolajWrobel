from swimming_pool_class import Swimming_pool, Client, Create_client
from swimming_pool_class import Dict_of_clients, Reservation
from swimming_pool_class import Aviability_and_prices, TimeTable
from swimming_pool_class import File_menagement
from numpy import array
# import datetime as dt
from pandas import DataFrame
import json


def test_File_menagement_import_file():
    menage = File_menagement()
    data = {"Pools": [
            "Maly", "Obrotny"
            ]}
    assert menage.import_file("Pools.json") == data


def test_File_menagement_import__from_file():
    menage = File_menagement()
    data = ["Maly", "Obrotny"]
    assert menage.import_from_file("Pools.json", "Pools") == data


# ??????????????????????
# def test_File_menagement_save_to_file_list():
#     menage = File_menagement()
#     Data = menage.import_from_file("Reservations.json", "Data")
#     menage.safe_to_file_list("Reservations.json", Data, '"Data"')


# ??????????????????????
def test_File_menagement_save_to_file_dict():
    menage = File_menagement()
    Data = menage.import_from_file("Working_hours_weekly.json", "Week")
    menage.safe_to_file_dict("Working_hours_weekly.json", Data, '"Week"')


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


def test_Client_maturity_as_customer():
    client = Client(666999, "Ania Makota", 0, 0)
    assert client.maturity() == 0


def test_Client_class_or_cust_as_customer():
    client = Client(666999, "Ania Makota", 0, 0)
    assert client.class_or_cust() == 0


def test_Client_group_size_as_customer():
    client = Client(666999, "Ania Makota", 0, 0)
    assert client.group_size() == 1


def test_Client__str__immature_client():
    client = Client(666999, "Ania Makota", 0, 0)
    string = str(client)
    assert string == 'Ania Makota jest kleintem/ką. Klient/tka Ania Makota nie jest dorosły/a. '


def test_Client__str__mature_client():
    client = Client(666999, "Ania Makota", 1, 0)
    string = str(client)
    assert string == 'Ania Makota jest kleintem/ką. Klient/tka Ania Makota jest dorosły/a. '


def test_Client__str__swimmingclass():
    client = Client(666999, "Płetewka", 1, 1, 10)
    string = str(client)
    assert string == 'Płetewka jest szkółką. Szkółka Płetewka ma 1 dorosłych pływaków/czek. W szkółce Płetewka pływa dziś 10 pływaków/czek.'


# def test_Client_create_client_input_class_or_cust():
#     new_client = Create_client()
#     new_client.create_client()


# def test_Client_client_from_clientsFile():
#     pass


def test_Dict_of_clients_get_dict():
    get = Dict_of_clients()
    Data = {'570000': ['Ala Makota', 0, 0, 1], '500000': ['Alice Police', 1, 0, 1], '580000': ['Arthur Davidson', 1, 0, 1], '670000': ['Bob Marley', 1, 0, 1], '720000': ['Charlie Hudson', 0, 0, 1], '080000': ['Pletewka', 5, 1, 10]}
    assert get.get_dict() == Data


def test_Aviability_and_prices_track_aviable():
    # aviability = Aviability_and_prices()
    pool = Swimming_pool("Maly", "Poniedzialek", 16)
    aviable = Aviability_and_prices("2024-11-04 13:00:00", "2024-11-04 14:00:00", "Maly", "Poniedzialek", 2, 6)
    assert aviable.track_aviable()


def test_Timetable_get_Data():
    timetable = TimeTable()
    timetable.table()
    data = {
        "client's_number": ["Alice Police", "Arthur Davidson", "Bob Marley", "Charlie Hudson", "Pletewka"],
        "starting_hour": ["2024-11-04 11:00:00", "2024-11-04 11:00:00", "2024-11-04 11:00:00", "2024-11-04 11:00:00", "2024-11-04 11:00:00"],
        "ending_hour": ["2024-11-04 13:00:00", "2024-11-04 11:00:00", "2024-11-04 11:00:00", "2024-11-04 11:00:00", "2024-11-04 11:00:00"],
        "track": [2, 6, 3, 1, 5]
    }
    assert timetable.get_Data() == data

# def test_TimeTable_table():
    # timetable = TimeTable()

    # def import_Data_from_Reservations():
    #     file = "Reservations.json"
    #     with open(file, 'r') as json_file:
    #         Data = json.load(json_file)
    #     Data = Data["Data"]
    #     return Data

    # def table():
    #     """Sorts and decrypts Data"""
    #     Data = []
    #     if len(Data) == 0:
    #         Data = import_Data_from_Reservations()
    #     list_numbers, list_starting_hour, list_ending_hour, list_track = list(map(list, zip(*sorted(Data))))
    #     Table = DataFrame(array([list_numbers, list_starting_hour,
    #                             list_ending_hour, list_track]),
    #                       index=["clent's_number", "starting_hour",
    #                              "ending_hour", "track"]).transpose()

    #     return Table
    # assert timetable.table() == table()


def test_TimeTable_book():
    timetable = TimeTable()
    timetable.table()
    timetable.book("Ala Makota", "2024-11-04 11:00:00",
                   "2024-11-04 11:00:00", 4)
    data = {
        "client's_number": ["Alice Police", "Arthur Davidson", "Bob Marley", "Charlie Hudson", "Pletewka", "Ala Makota"],
        "starting_hour": ["2024-11-04 11:00:00", "2024-11-04 11:00:00", "2024-11-04 11:00:00", "2024-11-04 11:00:00", "2024-11-04 11:00:00", "2024-11-04 11:00:00"],
        "ending_hour": ["2024-11-04 13:00:00", "2024-11-04 11:00:00", "2024-11-04 11:00:00", "2024-11-04 11:00:00", "2024-11-04 11:00:00", "2024-11-04 11:00:00"],
        "track": [2, 6, 3, 1, 5, 4]
    }
    assert timetable.get_Data() == data


def test_TimeTable_remove_book():
    timetable = TimeTable()
    timetable.table()
    timetable.remove_booking("Ala Makota", "2024-11-04 11:00:00",
                             "2024-11-04 11:00:00", 4)
    data = {
        "client's_number": ["Alice Police", "Arthur Davidson", "Bob Marley", "Charlie Hudson", "Pletewka"],
        "starting_hour": ["2024-11-04 11:00:00", "2024-11-04 11:00:00", "2024-11-04 11:00:00", "2024-11-04 11:00:00", "2024-11-04 11:00:00"],
        "ending_hour": ["2024-11-04 13:00:00", "2024-11-04 11:00:00", "2024-11-04 11:00:00", "2024-11-04 11:00:00", "2024-11-04 11:00:00"],
        "track": [2, 6, 3, 1, 5]
    }
    assert timetable.get_Data() == data
