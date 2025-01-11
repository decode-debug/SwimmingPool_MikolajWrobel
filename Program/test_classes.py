from Program.swimming_pool_class import Swimming_pool, Client
from Program.swimming_pool_class import Dict_of_clients, Price
from Program.swimming_pool_class import Aviability_and_prices, TimeTable
from Program.swimming_pool_class import File_menagement, earnings_meanagement
from Program.swimming_pool_class import NieZnalezionoPliku
from pandas import DataFrame
import datetime as dt
import pytest


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


def test_Client_as_customer():
    client = Client(570002, "Maly")
    assert client


def test_File_menagement_check_file_exists():
    exists = File_menagement("Maly")
    with pytest.raises(NieZnalezionoPliku):
        exists.check_file_exists("NieMaMnie.json")


def test_File_menagement_import_file():
    menage = File_menagement("Maly")
    data = {
            "Pools": {
                "Maly": 6,
                "Obrotny": 8
                }
        }
    assert menage.import_file("Pools.json") == data


def test_File_menagement_import__from_file():
    menage = File_menagement("Maly")
    data = {"Maly": 6, "Obrotny": 8}
    assert menage.import_from_file("Pools.json", "Pools") == data


def test_File_menagement_save_to_file_dict():
    menage = File_menagement("Maly")
    Data = menage.import_from_file("Working_hours_weekly.json", "Week")
    menage.safe_to_file_dict("Working_hours_weekly.json", Data, "w", '"Week"')


def test_Client_as_group():
    client = Client(80008, "Maly")
    assert client


def test_Client_maturity_group():
    client = Client(80008, "Maly")
    assert client.get_maturity == 5


def test_Client_class_or_cust_group():
    client = Client(80008, "Maly")
    assert client.get_class_or_cust == 1


def test_Client_group_size_group():
    client = Client(80008, "Maly")
    assert client.get_group_size == 10


def test_Client_name():
    client = Client(570002, "Maly")
    assert client.get_name == "Ala Makota"


def test_Client_maturity_as_customer():
    client = Client(570002, "Maly")
    assert client.get_maturity == 0


def test_Client_class_or_cust_as_customer():
    client = Client(570002, "Maly")
    assert client.get_class_or_cust == 0


def test_Client_group_size_as_customer():
    client = Client(570002, "Maly")
    assert client.get_group_size == 1


def test_Client__str__immature_client():
    client = Client(570002, "Maly")
    string = str(client)
    sentance = "Klient/tka Ala Makota nie jest dorosły/a. "
    assert string == f'Ala Makota jest kleintem/ką. {sentance}'


def test_Client__str__mature_client():
    client = Client(500005, "Maly")
    string = str(client)
    sentance = "Klient/tka Alice Police jest dorosły/a. "
    assert string == f'Alice Police jest kleintem/ką. {sentance}'


def test_Client__str__swimmingclass():
    client = Client(80008, "Maly")
    string = str(client)
    sentance = "Szkółka Pletewka ma 5 dorosłych pływaków/czek."
    sentance2 = " W szkółce Pletewka pływa dziś 10 pływaków/czek."
    assert string == f'Pletewka jest szkółką. {sentance}{sentance2}'


def test_Client_client_from_file():
    pass


def test_Dict_of_clients_get_dict():
    get = Dict_of_clients("Maly")
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
    find = Dict_of_clients("Maly")
    assert find.find_client(570013) == (570013, ['Ania Mapsa',
                                                 "2024-09-07", 0, 0, 1])


def test_Dict_of_clients_Add_client():
    add = Dict_of_clients("Maly")
    add.Add_client(570024, ["Ani Mal", 0, 0, 1])


def test_Dict_of_clients_remove_client():
    add = Dict_of_clients("Maly")
    add.remove_client(570024)


def test_Timetable_get_Data():
    timetable = TimeTable("Maly")
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
        "track": [[2], [6], [3], [1], [5, 6]],
        'people_swimming': [1, 1, 1, 1, 10]
    }
    assert timetable.get_Data == data


def test_TimeTable_import_Data_from_Reservations():
    timetable = TimeTable("Maly")
    Data = {
        'reservation_num': [1, 1, 1, 1, 1],
        "client's_id": ['500005', '580003', '670003', '720009', '080008'],
        'starting_hour': ['2024-11-04 11:00:00', '2024-11-04 11:00:00',
                          '2024-11-04 11:00:00', '2024-11-04 11:00:00',
                          '2024-11-04 11:00:00'],
        'ending_hour': ['2024-11-04 13:00:00', '2024-11-04 11:00:00',
                        '2024-11-04 11:00:00', '2024-11-04 11:00:00',
                        '2024-11-04 11:00:00'],
        'track': [[2], [6], [3], [1], [5, 6]],
        'people_swimming': [1, 1, 1, 1, 10]
        }
    data = timetable.import_Data_from_Reservations()
    assert data == Data


def test_TimeTable_table():
    timetable = TimeTable("Maly")

    def import_Data_from_Reservations():
        get = File_menagement("Maly")
        return get.import_from_file("Reservations.json", "Data")

    def table():
        """Sorts and decrypts Data"""
        Data = {}
        if len(Data) == 0:
            Data = import_Data_from_Reservations()
        Table = DataFrame(Data, columns=["reservation_num", "client's_id",
                                         "starting_hour", "ending_hour",
                                         "track", 'people_swimming'])
        Table_dict = Table.to_dict(orient="records")
        return Table_dict
    Table = timetable.table()
    Table_dict = Table.to_dict(orient="records")
    assert Table_dict == table()


def test_TimeTable_check_if_reservations_same():
    timetable = TimeTable("Maly")
    answer = timetable.check_if_reservations_not_same("500005",
                                                      "2024-11-04 11:00:00",
                                                      "2024-11-04 13:00:00",
                                                      2, 1)
    assert answer is True


def test_TimeTable_check_if_reservations_not_same():
    timetable = TimeTable("Maly")
    answer = timetable.check_if_reservations_not_same("500005",
                                                      "2024-11-04 11:00:00",
                                                      "2024-11-04 13:00:00",
                                                      8, 1)
    assert answer is False


def test_TimeTable_filtered():
    timetable = TimeTable("Maly")
    filtered_Table = {
        "client's_id": {0: '500005'},
        'ending_hour': {0: '2024-11-04 13:00:00'},
        'reservation_num': {0: 1},
        'starting_hour': {0: '2024-11-04 11:00:00'},
        'track': {0: [2]},
        'people_swimming': {0: 1}
    }
    filtered_table = timetable.Table_filtered("500005", "client's_id")
    assert filtered_table.to_dict() == filtered_Table


def test_TimeTable_book():
    timetable = TimeTable("Maly")
    timetable.table()
    timetable.book("570002", "2024-11-04 11:00:00",
                   "2024-11-04 11:00:00", [4], 1)
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
        "track": [[2], [6], [3], [1], [5, 6], [4]],
        'people_swimming': [1, 1, 1, 1, 10, 1]
    }
    assert timetable.get_Data == data


def test_TimeTable_remove_book():
    timetable = TimeTable("Maly")
    timetable.table()
    timetable.remove_booking("570002", "2024-11-04 11:00:00",
                             "2024-11-04 11:00:00", 4, 1)
    data = {
        "reservation_num": [1, 1, 1, 1, 1],
        "client's_id": ["500005", "580003", "670003", "720009", "080008"],
        "starting_hour": ["2024-11-04 11:00:00", "2024-11-04 11:00:00",
                          "2024-11-04 11:00:00", "2024-11-04 11:00:00",
                          "2024-11-04 11:00:00"],
        "ending_hour": ["2024-11-04 13:00:00", "2024-11-04 11:00:00",
                        "2024-11-04 11:00:00", "2024-11-04 11:00:00",
                        "2024-11-04 11:00:00"],
        "track": [2, 6, 3, 1, 5],
        "people_swimming": [1, 1, 1, 1, 10]
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


def test_Aviability_and_prices_load_working_hours():
    available = Aviability_and_prices("2024-11-04 12:00:00", "2:00",
                                      "Maly")
    assert available.load_working_hours() == ["09:00", "20:00"]


def test_Aviability_and_prices_set_working_hours():
    available = Aviability_and_prices("2024-11-04 12:00:00", "2:00",
                                      "Maly")
    assert available.load_working_hours() == ["09:00", "20:00"]
    available.set_working_hours("Monday", ["09:00", "20:00"])


def test_Aviability_and_prices_weekdays_():
    available = Aviability_and_prices("2024-11-04 12:00:00", "2:00",
                                      "Maly")
    assert available.weekdays_(0) == "Monday"


def test_Aviability_and_prices_weekday_():
    available = Aviability_and_prices("2024-11-04 12:00:00", "2:00",
                                      "Maly")
    assert available.weekday_() == "Monday"


def test_Aviability_and_prices_ending_hour():
    available = Aviability_and_prices("2024-11-04 12:00:00", "2:00",
                                      "Maly")
    assert available.ending_hour() == '2024-11-04 14:00:00'


def test_Aviability_and_prices_add_time():
    available = Aviability_and_prices("2024-11-04 12:00:00", "2:00",
                                      "Maly")
    add = available.add_time("2024-11-04 12:00:00", "03:00", "2")
    assert add == "2024-11-06 15:00:00"


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


def test_Aviability_and_prices_any_track_available_group():
    available = Aviability_and_prices("2024-11-04 12:00:00", "2:00",
                                      "Maly")
    test = available.risky_reservations("2024-12-04 09:00:00",
                                        "2024-11-04 12:00:00")
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
             'track': [2],
             "people_swimming": 1}]
    assert Table_dict == Data


def test_Aviability_and_prices_set_next_day():
    available = Aviability_and_prices("2024-11-04 12:00:00", "2:00",
                                      "Maly")
    next_day = available.set_next_day("2024-11-04 12:00:00")
    assert next_day == ("2024-11-05 09:00:00", "2024-11-05 11:00:00")


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


def test_Aviability_and_prices_suggest_resevation_group_():
    available = Aviability_and_prices("2024-12-08 09:00:00", "3:00",
                                      "Maly", [0], 1)
    returned = available.suggest_resevation()
    assert returned == ("2024-12-08 09:00:00",
                        "2024-12-08 12:00:00", [2])


def test_Aviability_and_prices_suggest_resevation_group_1():
    available = Aviability_and_prices("2024-12-04 09:00:00", "3:00",
                                      "Maly", [0], 15)
    returned = available.suggest_resevation()
    assert returned == ("2024-12-04 09:00:00",
                        "2024-12-04 12:00:00", [1, 2, 3])


def test_Aviability_and_prices_suggest_resevation():
    available = Aviability_and_prices("2024-11-04 12:00:00", "2:00",
                                      "Maly")
    returned = available.suggest_resevation()
    assert returned == ("2024-11-04 12:00:00", "2024-11-04 14:00:00", [1])


def test_Price__init__():
    Price(500005, 1, "Maly")


def test_Price_get_price():
    prices = Price(500005, 1, "Maly")
    assert prices.get_price == 7500


def test_Price_get_swimming_time():
    prices = Price(500005, 1, "Maly")
    assert prices.get_swimming_time == 2.0


def test_Price_get_clients_age():
    prices = Price(500005, 1, "Maly")
    assert prices.get_clients_age == dt.timedelta(days=12970)


def test_Price_get_clients_age_type():
    prices = Price(500005, 1, "Maly")
    assert prices.get_clients_age_type == 'Adult'


def test_Price_price():
    prices = Price(500005, 1, "Maly")
    assert prices.price() == 7500


def test_Price_weekdays_():
    prices = Price(500005, 1, "Maly")
    assert prices.weekdays_(0) == "Monday"


def test_Price_weekday_():
    prices = Price(500005, 1, "Maly")
    assert prices.weekday_() == "Monday"


def test_Price_clients_age_type():
    prices = Price(500005, 1, "Maly")
    assert prices.clients_age_type() == "Adult"


def test_Price_find_reservation():
    prices = Price("500005", 1, "Maly")
    data = {
        "client's_id": {0: '500005'},
        'ending_hour': {0: '2024-11-04 13:00:00'},
        'reservation_num': {0: 1},
        'starting_hour': {0: '2024-11-04 11:00:00'},
        'track': {0: 2}, "people_swimming": {0: 1}
        }
    assert prices.find_reservation().to_dict() == data


def test_Price_clients_day():
    prices = Price(500005, 1, "Maly")
    assert prices.day() == dt.date(2024, 11, 4)


def test_Price_clients_swimming_time():
    prices = Price(500005, 1, "Maly")
    assert prices.swimming_time() == 2.0


def test_Price_clients_price():
    prices = Price(500005, 1, "Maly")
    assert prices.price() == 7500


def test_earnings_menagement_get_earnings():
    earnigs = earnings_meanagement("2024-11-04", "Maly")
    money = {
       "2024-11-04 18:00:00": {"Gross income": 7500, "Tax": 600},
       "2024-11-04 14:00:00": {"Gross income": 5000, "Tax": 400},
       "2024-11-04 11:35:17": {"Gross income": 2500, "Tax": 200},
       "2024-11-04 19:00:00": {"Gross income": 7500, "Tax": 600},
       "2024-11-04 21:35:17": {"Gross income": 7500, "Tax": 600},
       "2025-01-05 20:14:53": {"Gross income": 7500, "Tax": 600},
       "2025-01-07 19:38:05": {"Gross income": 7500, "Tax": 600},
       "2025-01-08 23:26:07": {"Gross income": 4500, "Tax": 360}
    }
    assert earnigs.get_earnings == money


def test_earnings_menagement_get_days_gross():
    earnigs = earnings_meanagement("2024-11-04", "Maly")
    assert earnigs.get_days_gross == 30000


def test_earnings_menagement_get_days_tax():
    earnigs = earnings_meanagement("2024-11-04", "Maly")
    assert earnigs.get_days_tax == 2400


def test_earnings_menagement_earnings_from_file():
    earnigs = earnings_meanagement("2024-11-04", "Maly")
    money = {
       "2024-11-04 18:00:00": {"Gross income": 7500, "Tax": 600},
       "2024-11-04 14:00:00": {"Gross income": 5000, "Tax": 400},
       "2024-11-04 11:35:17": {"Gross income": 2500, "Tax": 200},
       "2024-11-04 19:00:00": {"Gross income": 7500, "Tax": 600},
       "2024-11-04 21:35:17": {"Gross income": 7500, "Tax": 600},
       "2025-01-05 20:14:53": {"Gross income": 7500, "Tax": 600},
       "2025-01-07 19:38:05": {"Gross income": 7500, "Tax": 600},
       "2025-01-08 23:26:07": {"Gross income": 4500, "Tax": 360}
    }
    assert earnigs.earnings_from_file() == money


def test_earnings_menagement_find_all_day_earning():
    earnigs = earnings_meanagement("2024-11-04", "Maly")
    earnigs.find_all_day_earnings()
    assert earnigs._days_gross == 60000 and earnigs._days_tax == 4800


def test_earnings_menagement_day_earnings():
    earnigs = earnings_meanagement("2024-11-04", "Maly")
    money = {
       "2024-11-04 18:00:00": {"Gross income": 7500, "Tax": 600},
       "2024-11-04 14:00:00": {"Gross income": 5000, "Tax": 400},
       "2024-11-04 11:35:17": {"Gross income": 2500, "Tax": 200},
       "2024-11-04 19:00:00": {"Gross income": 7500, "Tax": 600},
       "2024-11-04 21:35:17": {"Gross income": 7500, "Tax": 600}
    }
    assert earnigs.day_earnings() == money


def test_earnings_menagement_add_earnings():
    earnigs = earnings_meanagement("2024-11-04 20:00:00", "Maly", 7500, 600)
    money = {
       "2024-11-04 18:00:00": {"Gross income": 7500, "Tax": 600},
       "2024-11-04 14:00:00": {"Gross income": 5000, "Tax": 400},
       "2024-11-04 11:35:17": {"Gross income": 2500, "Tax": 200},
       "2024-11-04 19:00:00": {"Gross income": 7500, "Tax": 600},
       "2024-11-04 21:35:17": {"Gross income": 7500, "Tax": 600},
       "2025-01-05 20:14:53": {"Gross income": 7500, "Tax": 600},
       "2025-01-07 19:38:05": {"Gross income": 7500, "Tax": 600},
       "2025-01-08 23:26:07": {"Gross income": 4500, "Tax": 360},
       '2024-11-04 20:00:00': {'Gross income': 7500, 'Tax': 600}
    }
    earnigs.add_earnings()
    assert earnigs._earnings == money
