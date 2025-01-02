from swimming_pool_class import Swimming_pool, Client
from swimming_pool_class import Dict_of_clients
from swimming_pool_class import Aviability_and_prices, TimeTable
from swimming_pool_class import File_menagement
from pandas import DataFrame


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
    menage.safe_to_file_dict("Working_hours_weekly.json", Data, '"Week"')


def test_Swimming_pool_class():
    pool = Swimming_pool("Maly", "Poniedzialek")
    assert pool


def test_Swimming_pool_get_working_hours():
    pool = Swimming_pool("Maly", "Poniedzialek")
    assert pool.get_working_hours == [900, 2000]


def test_Swimming_pool_get_name():
    pool = Swimming_pool("Maly", "Poniedzialek")
    assert pool.get_name == 'Maly'


def test_Swimming_pool_get_day():
    pool = Swimming_pool("Maly", "Poniedzialek")
    assert pool.get_day == 'Poniedzialek'


def test_Swimming_pool_get_tracks():
    pool = Swimming_pool("Maly", "Poniedzialek")
    assert pool.get_tracks == 6


def test_Swimming_pool_load_tracks():
    pool = Swimming_pool("Maly", "Poniedzialek")
    assert pool.load_tracks() == 6


def test_Swimming_pool_load_working_hours():
    pool = Swimming_pool("Maly", "Poniedzialek")
    assert pool.load_working_hours() == [900, 2000]


def test_set_working_hours():
    pool = Swimming_pool("Maly", "Poniedzialek", 1)
    assert pool.load_working_hours() == [900, 2000]
    pool.set_working_hours([900, 2000])


def test_set_tracks():
    pool = Swimming_pool("Maly", "Poniedzialek")
    assert pool.load_tracks() == 6
    pool.set_tracks(8)


def test_set_tracks_revarse():
    pool = Swimming_pool("Maly", "Poniedzialek")
    assert pool.load_tracks() == 8
    pool.set_tracks(6)


def test_Client_as_customer():
    client = Client(666999, "Ania Makota", 0, 0)
    assert client


def test_Client_as_group():
    client = Client(666999, "Pletweka", 0, 1, 69)
    assert client


def test_Client_maturity_group():
    client = Client(666999, "Pletweka", 0, 1, 69)
    assert client.get_maturity == 0


def test_Client_class_or_cust_group():
    client = Client(666999, "Pletweka", 0, 1, 69)
    assert client.get_class_or_cust == 1


def test_Client_group_size_group():
    client = Client(666999, "Pletweka", 0, 1, 69)
    assert client.get_group_size == 69


def test_Client_name():
    client = Client(666999, "Ania Makota", 0, 0)
    assert client.get_name == "Ania Makota"


def test_Client_maturity_as_customer():
    client = Client(666999, "Ania Makota", 0, 0)
    assert client.get_maturity == 0


def test_Client_class_or_cust_as_customer():
    client = Client(666999, "Ania Makota", 0, 0)
    assert client.get_class_or_cust == 0


def test_Client_group_size_as_customer():
    client = Client(666999, "Ania Makota", 0, 0)
    assert client.get_group_size == 1


def test_Client__str__immature_client():
    client = Client(666999, "Ania Makota", 0, 0)
    string = str(client)
    sentance = "Klient/tka Ania Makota nie jest dorosły/a. "
    assert string == f'Ania Makota jest kleintem/ką. {sentance}'


def test_Client__str__mature_client():
    client = Client(666999, "Ania Makota", 1, 0)
    string = str(client)
    sentance = "Klient/tka Ania Makota jest dorosły/a. "
    assert string == f'Ania Makota jest kleintem/ką. {sentance}'


def test_Client__str__swimmingclass():
    client = Client(666999, "Płetewka", 1, 1, 10)
    string = str(client)
    sentance = "Szkółka Płetewka ma 1 dorosłych pływaków/czek."
    sentance2 = " W szkółce Płetewka pływa dziś 10 pływaków/czek."
    assert string == f'Płetewka jest szkółką. {sentance}{sentance2}'


def test_Client_client_from_file():
    pass


def test_Dict_of_clients_get_dict():
    get = Dict_of_clients()
    Data = {
       "570002": ["Ala Makota", 0, 0, 1],
       "500005": ["Alice Police", 1, 0, 1],
       "580003": ["Arthur Davidson", 1, 0, 1],
       "670003": ["Bob Marley", 1, 0, 1],
       "720009": ["Charlie Hudson", 0, 0, 1],
       "080008": ["Pletewka", 5, 1, 10],
       "570013": ["Ania Mapsa", 0, 0, 1]
    }
    assert get.get_dict == Data


def test_Dict_of_clients_find_client():
    find = Dict_of_clients()
    assert find.find_client(570013) == (570013, ['Ania Mapsa', 0, 0, 1])


def test_Dict_of_clients_Add_client():
    add = Dict_of_clients()
    add.Add_client(570024, ["Ani Mal", 0, 0, 1])


def test_Dict_of_clients_remove_client():
    add = Dict_of_clients()
    add.remove_client(570024)


def test_Aviability_and_prices_get_swimming_time():
    aviable = Aviability_and_prices("2024-11-04 12:00:00", "2:00",
                                    "Maly", "Poniedzialek")
    assert aviable.get_swimming_time == "2:00"


def test_Aviability_and_prices_get_tracks():
    aviable = Aviability_and_prices("2024-11-04 12:00:00", "2:00",
                                    "Maly", "Poniedzialek")
    assert aviable.get_tracks == 6


def test_Aviability_and_prices_get_track():
    aviable = Aviability_and_prices("2024-11-04 12:00:00", "2:00",
                                    "Maly", "Poniedzialek")
    assert aviable.get_track == 0


def test_Aviability_and_prices_get_ending_hour():
    aviable = Aviability_and_prices("2024-11-04 12:00:00", "2:00",
                                    "Maly", "Poniedzialek")
    assert aviable.get_ending_hour == '2024-11-04 14:00:00'


def test_Aviability_and_prices_find_aviable_track():
    aviable = Aviability_and_prices("2024-11-04 12:00:00", "2:00",
                                    "Maly", "Poniedzialek", 1)
    test = aviable.risky_reservations("2024-11-04 12:00:00",
                                      "2024-11-04 14:00:00")
    assert aviable.find_aviable_track(test) == 1


def test_Aviability_and_prices_track_aviable():
    aviable = Aviability_and_prices("2024-11-04 12:00:00", "2:00",
                                    "Maly", "Poniedzialek")
    test = aviable.risky_reservations("2024-11-04 12:00:00",
                                      "2024-11-04 14:00:00")
    assert aviable.track_aviable(1, test) is True

def test_Aviability_and_prices_any_track_aviable():
    aviable = Aviability_and_prices("2024-11-04 12:00:00", "2:00",
                                    "Maly", "Poniedzialek")
    test = aviable.risky_reservations("2024-11-04 12:00:00",
                                      "2024-11-04 14:00:00")
    assert aviable.any_track_aviable(test) is True


def test_Aviability_and_prices_risky_reservations():
    aviable = Aviability_and_prices("2024-11-04 12:00:00", "2:00",
                                    "Maly", "Poniedzialek")
    Table = aviable.risky_reservations("2024-11-04 12:00:00",
                                       "2024-11-04 14:00:00")
    Table_dict = Table.to_dict(orient="records")  # this step is needed because
    # in vanilla pytest has not assertion for pd.Datdaframe and I dont want to
    # force user to get one more datapack. This datapack crashed my python 3.12
    Data = [{"client's_number": '500005',
             'starting_hour': '2024-11-04 11:00:00',
             'ending_hour': '2024-11-04 13:00:00',
             'track': 2}]
    assert Table_dict == Data


def test_Aviability_and_prices_suggest_resevation():
    aviable = Aviability_and_prices("2024-11-04 12:00:00", "2:00",
                                    "Maly", "Poniedzialek")
    assert aviable.suggest_resevation() == ("2024-11-04 12:00:00",
                                            "2024-11-04 14:00:00", 0)


def test_get_swimming_time():
    aviavble = Aviability_and_prices("2024-11-04 12:00:00", "2:00",
                                     "Maly", "Poniedzialek")
    assert aviavble.get_tracks == 6


def test_Timetable_get_Data():
    timetable = TimeTable()
    timetable.table()
    data = {
        "client's_number": ["500005", "580003", "670003", "720009", "080008"],
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
        Table = DataFrame(Data, columns=["client's_number", "starting_hour",
                                         "ending_hour", "track"])
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
        "client's_number": ["500005", "580003", "670003",
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
        "client's_number": ["500005", "580003", "670003", "720009", "080008"],
        "starting_hour": ["2024-11-04 11:00:00", "2024-11-04 11:00:00",
                          "2024-11-04 11:00:00", "2024-11-04 11:00:00",
                          "2024-11-04 11:00:00"],
        "ending_hour": ["2024-11-04 13:00:00", "2024-11-04 11:00:00",
                        "2024-11-04 11:00:00", "2024-11-04 11:00:00",
                        "2024-11-04 11:00:00"],
        "track": [2, 6, 3, 1, 5]
    }
    assert timetable.get_Data == data
