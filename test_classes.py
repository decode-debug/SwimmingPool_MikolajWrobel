from swimming_pool_class import Swimming_pool, Client
from swimming_pool_class import Dict_of_clients, Price
from swimming_pool_class import Aviability_and_prices, TimeTable
from swimming_pool_class import File_menagement
from pandas import DataFrame
from datetime import date as dt


def test_File_menagement_import_file():
    menage = File_menagement()
    data = {
            "Pools": {
                "Maly": 6,
                "Obrotny": 8
                }
        }
    assert menage.import_file("Pools.json") == data


def test_File_menagement_import__from_file():
    menage = File_menagement()
    data = {"Maly": 6, "Obrotny": 8}
    assert menage.import_from_file("Pools.json", "Pools") == data


def test_File_menagement_save_to_file_dict():
    menage = File_menagement()
    Data = menage.import_from_file("Working_hours_weekly.json", "Week")
    menage.safe_to_file_dict("Working_hours_weekly.json", Data, "w", '"Week"')


def test_Swimming_pool_class():
    pool = Swimming_pool("Maly")
    assert pool





def test_Swimming_pool_get_name():
    pool = Swimming_pool("Maly")
    assert pool.get_name == 'Maly'


def test_Swimming_pool_get_tracks():
    pool = Swimming_pool("Maly")
    assert pool.get_tracks == 6


def test_Swimming_pool_load_tracks():
    pool = Swimming_pool("Maly")
    assert pool.load_tracks() == 6





def test_set_tracks():
    pool = Swimming_pool("Maly")
    assert pool.load_tracks() == 6
    pool.set_tracks(8)


def test_set_tracks_revarse():
    pool = Swimming_pool("Maly")
    assert pool.load_tracks() == 8
    pool.set_tracks(6)


def test_Client_as_customer():
    client = Client(570002)
    assert client


def test_Client_as_group():
    client = Client(80008)
    assert client


def test_Client_maturity_group():
    client = Client(80008)
    assert client.get_maturity == 5


def test_Client_class_or_cust_group():
    client = Client(80008)
    assert client.get_class_or_cust == 1


def test_Client_group_size_group():
    client = Client(80008)
    assert client.get_group_size == 10


def test_Client_name():
    client = Client(570002)
    assert client.get_name == "Ala Makota"


def test_Client_maturity_as_customer():
    client = Client(570002)
    assert client.get_maturity == 0


def test_Client_class_or_cust_as_customer():
    client = Client(570002)
    assert client.get_class_or_cust == 0


def test_Client_group_size_as_customer():
    client = Client(570002)
    assert client.get_group_size == 1


def test_Client__str__immature_client():
    client = Client(570002)
    string = str(client)
    sentance = "Klient/tka Ala Makota nie jest dorosły/a. "
    assert string == f'Ala Makota jest kleintem/ką. {sentance}'


def test_Client__str__mature_client():
    client = Client(500005)
    string = str(client)
    sentance = "Klient/tka Alice Police jest dorosły/a. "
    assert string == f'Alice Police jest kleintem/ką. {sentance}'


def test_Client__str__swimmingclass():
    client = Client(80008)
    string = str(client)
    sentance = "Szkółka Pletewka ma 5 dorosłych pływaków/czek."
    sentance2 = " W szkółce Pletewka pływa dziś 10 pływaków/czek."
    assert string == f'Pletewka jest szkółką. {sentance}{sentance2}'


def test_Client_client_from_file():
    pass


def test_Dict_of_clients_get_dict():
    get = Dict_of_clients()
    Data = {
       "570002": ["Ala Makota", "2010-12-09", 0, 0, 1],
       "500005": ["Alice Police", "1989-07-09", 1, 0, 1],
       "580003": ["Arthur Davidson", "1978-09-07", 1, 0, 1],
       "670003": ["Bob Marley", "1978-09-07", 1, 0, 1],
       "720009": ["Charlie Hudson", "1978-09-07", 0, 0, 1],
       "080008": ["Pletewka", "Not a person", 5, 1, 10],
       "570013": ["Ania Mapsa", "2024-09-07", 0, 0, 1]
    }
    assert get.get_dict == Data


def test_Dict_of_clients_find_client():
    find = Dict_of_clients()
    assert find.find_client(570013) == (570013, ['Ania Mapsa',
                                                 "2024-09-07", 0, 0, 1])


def test_Dict_of_clients_Add_client():
    add = Dict_of_clients()
    add.Add_client(570024, ["Ani Mal", 0, 0, 1])


def test_Dict_of_clients_remove_client():
    add = Dict_of_clients()
    add.remove_client(570024)


def test_Timetable_get_Data():
    timetable = TimeTable()
    timetable.table()
    data = {
        "reservation_num": [1, 1, 1, 1, 1],
        "client's_id": ["500005", "580003", "670003", "720009", "080008"],
        "starting_hour": ["2024-11-04 11:00:00", "2024-11-04 11:00:00",
                          "2024-11-04 11:00:00", "2024-11-04 11:00:00",
                          "2024-11-04 11:00:00"],
        "ending_hour": ["2024-11-04 13:00:00", "2024-11-04 11:00:00",
                        "2024-11-04 11:00:00", "2024-11-04 11:00:00",
                        "2024-11-04 11:00:00"],
        "track": [2, 6, 3, 1, 5]
    }
    assert timetable.get_Data == data


def test_TimeTable_table():
    timetable = TimeTable()

    def import_Data_from_Reservations():
        get = File_menagement()
        return get.import_from_file("Reservations.json", "Data")

    def table():
        """Sorts and decrypts Data"""
        Data = {}
        if len(Data) == 0:
            Data = import_Data_from_Reservations()
        Table = DataFrame(Data, columns=["reservation_num", "client's_id",
                                         "starting_hour", "ending_hour",
                                         "track"])
        Table_dict = Table.to_dict(orient="records")
        return Table_dict
    Table = timetable.table()
    Table_dict = Table.to_dict(orient="records")
    assert Table_dict == table()


def test_TimeTable_book():
    timetable = TimeTable()
    timetable.table()
    timetable.book("570002", "2024-11-04 11:00:00",
                   "2024-11-04 11:00:00", 4)
    data = {
        "reservation_num": [1, 1, 1, 1, 1, 1],
        "client's_id": ["500005", "580003", "670003",
                        "720009", "080008", "570002"],
        "starting_hour": ["2024-11-04 11:00:00", "2024-11-04 11:00:00",
                          "2024-11-04 11:00:00", "2024-11-04 11:00:00",
                          "2024-11-04 11:00:00", "2024-11-04 11:00:00"],
        "ending_hour": ["2024-11-04 13:00:00", "2024-11-04 11:00:00",
                        "2024-11-04 11:00:00", "2024-11-04 11:00:00",
                        "2024-11-04 11:00:00", "2024-11-04 11:00:00"],
        "track": [2, 6, 3, 1, 5, 4]
    }
    assert timetable.get_Data == data


def test_TimeTable_remove_book():
    timetable = TimeTable()
    timetable.table()
    timetable.remove_booking("570002", "2024-11-04 11:00:00",
                             "2024-11-04 11:00:00", 4)
    data = {
        "reservation_num":[1, 1, 1, 1, 1],
        "client's_id": ["500005", "580003", "670003", "720009", "080008"],
        "starting_hour": ["2024-11-04 11:00:00", "2024-11-04 11:00:00",
                          "2024-11-04 11:00:00", "2024-11-04 11:00:00",
                          "2024-11-04 11:00:00"],
        "ending_hour": ["2024-11-04 13:00:00", "2024-11-04 11:00:00",
                        "2024-11-04 11:00:00", "2024-11-04 11:00:00",
                        "2024-11-04 11:00:00"],
        "track": [2, 6, 3, 1, 5]
    }
    assert timetable.get_Data == data


def test_Aviability_and_prices_get_working_hours():
    available = Aviability_and_prices("2024-11-04 12:00:00", "2:00",
                                      "Maly")
    assert available.get_working_hours == ["09:00", "20:00"]


def test_Aviability_and_prices_get_swimming_time():
    available = Aviability_and_prices("2024-11-04 12:00:00", "2:00",
                                      "Maly")
    assert available.get_swimming_time == "2:00"


def test_get_swimming_time():
    aviavble = Aviability_and_prices("2024-11-04 12:00:00", "2:00",
                                     "Maly")
    assert aviavble.get_tracks == 6


def test_Aviability_and_prices_get_tracks():
    available = Aviability_and_prices("2024-11-04 12:00:00", "2:00",
                                      "Maly")
    assert available.get_tracks == 6


def test_Aviability_and_prices_get_track():
    available = Aviability_and_prices("2024-11-04 12:00:00", "2:00",
                                      "Maly")
    assert available.get_track == 0


def test_Aviability_and_prices_get_ending_hour():
    available = Aviability_and_prices("2024-11-04 12:00:00", "2:00",
                                      "Maly")
    assert available.get_ending_hour == '2024-11-04 14:00:00'


def test_Swimming_pool_load_working_hours():
    available = Aviability_and_prices("2024-11-04 12:00:00", "2:00",
                                      "Maly")
    assert available.load_working_hours() == ["09:00", "20:00"]


def test_set_working_hours():
    available = Aviability_and_prices("2024-11-04 12:00:00", "2:00",
                                      "Maly")
    assert available.load_working_hours() == ["09:00", "20:00"]
    available.set_working_hours(["09:00", "20:00"])


def test_Aviability_and_prices_find_available_track():
    available = Aviability_and_prices("2024-11-04 12:00:00", "2:00",
                                      "Maly", 1)
    test = available.risky_reservations("2024-11-04 12:00:00",
                                        "2024-11-04 14:00:00")
    assert available.find_available_track(test) == 1


def test_Aviability_and_prices_track_available():
    available = Aviability_and_prices("2024-11-04 12:00:00", "2:00",
                                      "Maly")
    test = available.risky_reservations("2024-11-04 12:00:00",
                                        "2024-11-04 14:00:00")
    assert available.track_available(1, test) is True


def test_Aviability_and_prices_any_track_available():
    available = Aviability_and_prices("2024-11-04 12:00:00", "2:00",
                                      "Maly")
    test = available.risky_reservations("2024-11-04 12:00:00",
                                        "2024-11-04 14:00:00")
    assert available.any_track_available(test) is True


def test_Aviability_and_prices_risky_reservations():
    available = Aviability_and_prices("2024-11-04 12:00:00", "2:00",
                                      "Maly")
    Table = available.risky_reservations("2024-11-04 12:00:00",
                                         "2024-11-04 14:00:00")
    Table_dict = Table.to_dict(orient="records")  # this step is needed because
    # in vanilla pytest has not assertion for pd.Datdaframe and I dont want to
    # force user to get one more datapack. This datapack crashed my python 3.12
    Data = [{'reservation_num': 1,
             "client's_id": '500005',
             'starting_hour': '2024-11-04 11:00:00',
             'ending_hour': '2024-11-04 13:00:00',
             'track': 2}]
    assert Table_dict == Data


def test_Aviability_and_prices_set_next_day():
    available = Aviability_and_prices("2024-11-04 12:00:00", "2:00",
                                      "Maly")
    assert available.set_next_day("2024-11-04 12:00:00") == ("2024-11-05 09:00:00", "2024-11-05 11:00:00")


def test_Aviability_and_prices_hour_in_working_hours():
    available = Aviability_and_prices("2024-11-04 12:00:00", "2:00",
                                      "Maly")
    returned = available.hour_in_working_hours("2024-11-04 12:00:00",
                                               "2024-11-04 14:00:00")
    assert returned is True


def test_Aviability_and_prices_hour_not_in_working_hours_1():
    available = Aviability_and_prices("2024-11-04 19:00:00", "2:00",
                                      "Maly")
    returned = available.hour_in_working_hours("2024-11-04 19:00:00",
                                               "2024-11-04 21:00:00")
    assert returned is False


def test_Aviability_and_prices_hour_not_in_working_hours_2():
    available = Aviability_and_prices("2024-11-04 08:00:00", "2:00",
                                      "Maly")
    returned = available.hour_in_working_hours("2024-11-04 08:00:00",
                                               "2024-11-04 10:00:00")
    assert returned is False


def test_Aviability_and_prices_datetime_to_time():
    available = Aviability_and_prices("2024-11-04 08:00:00", "2:00",
                                      "Maly")
    returned = available.datetime_to_time("2024-11-04 08:00:00")
    assert returned == "08:00:00"


def test_Aviability_and_prices_potential_reser_hour():
    available = Aviability_and_prices("2024-11-04 12:00:00", "2:00",
                                      "Maly")
    returned = available.potential_reser_hour("2024-11-04 12:00:00",
                                              "2024-11-04 14:00:00")
    assert returned == ("2024-11-04 12:15:00", "2024-11-04 14:15:00")


def test_Aviability_and_prices_suggest_resevation():
    available = Aviability_and_prices("2024-11-04 12:00:00", "2:00",
                                      "Maly")
    returned = available.suggest_resevation()
    assert returned == ("2024-11-04 12:00:00", "2024-11-04 14:00:00", 1)


def test_Price__init__():
    prices = Price(500005, 1)


def test_Price_price():
    prices = Price(500005, 1)
    assert prices.price() == 7500
