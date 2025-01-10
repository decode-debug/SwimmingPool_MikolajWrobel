# from typing import List
import json
from pandas import DataFrame, concat
from datetime import datetime as dt
from datetime import date
from datetime import timedelta


class Swimming_pool:
    def __init__(self, name):
        """
        defining Swimming_pool class
        self :: str
        name :: str
        working_hours :: typle
        """
        self._pool_name = name
        self._tracks = self.load_tracks()

    @property
    def get_name(self):
        "returns pool name"
        return self._pool_name

    @property
    def get_tracks(self):
        "returns ammount of swimming tracks"
        return self._tracks  # ??????????????

    def load_tracks(self):
        '''asking for ammount of tracks in Swimming_pool'''
        file = "Pools/Pools.json"
        with (open(file, 'r')) as json_file:
            data = json.load(json_file)
        return data["Pools"][f'{self._pool_name}']

    # def set_tracks(self, new_tracks):
    #     '''setting ammount of tracks in Swimming_pool'''
    #     file = "Pools.json"
    #     with (open(file, 'r')) as json_file:
    #         data = json.load(json_file)
    #     tracks = data["Pools"]
    #     tracks[f'{self._name}'] = new_tracks
    #     open.safe_to_file_dict(file, tracks, "w", '"Pools"')


class File_menagement(Swimming_pool):
    def __init__(self, pool_name):
        super().__init__(pool_name)

    @property
    def get_tracks(self):
        return super().get_tracks

    def file_path(self, file):
        if file != "passwords.json" and file != "Pools.json":
            file_path = f"Pools/{self._pool_name}_Pool_Data/{file}"
        else:
            file_path = f"Pools/{file}"
        return file_path

    def import_file(self, file):
        file_path = self.file_path(file)
        with open(file_path, 'r') as json_file:
            return json.load(json_file)

    def import_from_file(self, file, request):
        file_path = self.file_path(file)
        with (open(file_path, 'r')) as json_file:
            data = json.load(json_file)
        return data[request]

    # def safe_to_file_list(self, file, Data, name=0):
    #     with open(file, 'w') as json_file:
    #         json_file.write("{")
    #         json_file.write("\n")
    #         json_file.write("   ")
    #         if name != 0:
    #             json_file.write(f'{name}:')
    #             json_file.write("[")
    #             json_file.write("\n")
    #         for element in Data:
    #             json_file.write("       ")
    #             json_file.write(json.dumps(element))
    #             if element != Data[-1]:
    #                 json_file.write(",")
    #             json_file.write("\n")
    #         json_file.write("    ")
    #         json_file.write("]")
    #         json_file.write("\n")
    #         json_file.write("}")

    def safe_to_file_dict(self, file, Data, work, name=0):
        file_path = self.file_path(file)
        with open(file_path, f'{work}') as json_file:
            json_file.write("{")
            json_file.write("\n")
            json_file.write("   ")
            if name != 0:
                json_file.write(f'{name}:')
                json_file.write("{")
                json_file.write("\n")
            iter = 1
            for element in Data:
                json_file.write("       ")
                json_file.write(json.dumps(element))
                json_file.write(":")
                json_file.write(json.dumps(Data[element]))
                if iter < len(Data):
                    iter += 1
                    json_file.write(",")
                json_file.write("\n")
            json_file.write("    ")
            json_file.write("}")
            json_file.write("\n")
            json_file.write("}")


class Client(File_menagement):
    def __init__(self, id, pool_name):
        super().__init__(pool_name)
        """
        defining Client class
        self :: str
        name :: str
        maturity :: str
        group_size :: int
        class_or_cust :: bool
        """
        self._id = id
        self._name = self.name()
        self._birthday = self.birthday()
        self._maturity = self.maturity()
        self._group_size = self.group_size()
        self._class_or_cust = self.class_or_cust()

    @property
    def get_name(self) -> str:
        """returning client's name"""
        return self._name

    @property
    def get_maturity(self) -> str:
        return self._maturity

    @property
    def get_class_or_cust(self) -> str:
        return self._class_or_cust

    @property
    def get_group_size(self) -> str:
        return self._group_size

    def name(self):
        return self.import_client()[0]

    def birthday(self):
        return self.import_client()[1]

    def maturity(self):
        return self.import_client()[2]

    def group_size(self):
        return self.import_client()[4]

    def class_or_cust(self):
        return self.import_client()[3]

    def import_client(self):
        file = "Clients.json"
        clients = self.import_from_file(file, "Clients")
        return clients[f"{self._id}".zfill(6)]

    def __str__(self):
        group_size = ''
        if self._class_or_cust == 0:
            class_or_cust = f"{self._name} jest kleintem/ką. "
        else:
            class_or_cust = f"{self._name} jest szkółką. "

        if self._class_or_cust == 0:
            if self._maturity == 1:
                maturity = f"Klient/tka {self._name} jest dorosły/a. "
            else:
                maturity = f"Klient/tka {self._name} nie jest dorosły/a. "
        else:
            str = "dorosłych pływaków/czek."
            maturity = f"Szkółka {self._name} ma {self._maturity} {str} "
            str = f"pływa dziś {self._group_size} pływaków/czek."
            group_size = f"W szkółce {self._name} {str}"
        return class_or_cust + maturity + group_size

    def client_from_file(self, id):
        Dict_of_clients.find_client(id)

    def add_client_to_file(self):
        add = Dict_of_clients()
        add.Add_client()


class Dict_of_clients(File_menagement):
    def __init__(self, pool_name):
        super().__init__(pool_name)
        self._dict = {}

    @property
    def get_dict(self):
        self._dict = self.import_from_file("clients.json", "Clients")
        return self._dict

    def find_client(self, id):
        """Check's if client is on list"""
        if len(self._dict) == 0:
            self.get_dict
        return id, self._dict[f"{id}"]

    def Add_client(self, id, Data):
        self.get_dict
        self._dict[f"{id}"] = Data
        self.safe_to_file_dict("Clients.json", self._dict, "w", '"Clients"')

    def remove_client(self, id):
        self.get_dict
        del self._dict[f"{id}"]
        self.safe_to_file_dict("Clients.json", self._dict, "w", '"Clients"')


# class Reservation:
#     def __init__(self, client_id, track, water_entry, booked_hours):
#         """
#         client_id :: int
#         track :: int
#         water_entry :: int
#         booked_hours :: int
#         """
#         self._client_id = client_id
#         self._track = track
#         self._water_entry = water_entry
#         self._booked_hours = booked_hours

#     def tracks(self) -> str:
#         """Printing track occupied by client"""
#         if self._group_size == 1:
#             return f"{self._name} occupies track {self._track[0]}"
#         if self._class_or_cust == 0:
#             a = f"{self._name} occupies track {self._track[0]} "
#             b = f"with {self._group_size - 1} other customers"
#             return a+b
#         else:
#             a = ""
#             for i in self._track:
#                 a = a + f" {i}"
#             str = "{self._name} occupies tracks{a}"
#             return f"group of {self._group_size} named {str}"


class Tickets:
    pass


class TimeTable(File_menagement):
    def __init__(self, pool_name):
        """stores datatable about reservations"""
        super().__init__(pool_name)
        self._Data = self.import_Data_from_Reservations()
        self._Table = self.table()

    @property
    def get_Data(self):
        return self._Data

    @property
    def get_Table(self):
        return self._Table

    def import_Data_from_Reservations(self):
        return self.import_from_file("Reservations.json", "Data")

    def table(self):
        """Sorts and decrypts Data"""
        Table = DataFrame(self._Data,
                          columns=["reservation_num", "client's_id",
                                   "starting_hour", "ending_hour", "track"])
        return Table

    def check_if_reservations_not_same(self, id, strating_hour,
                                       eding_hour, track):
        if len(self._Table[((self._Table["client's_id"] == id) &
                            (self._Table[
                                "starting_hour"] == strating_hour) &
                            (self._Table[
                                "ending_hour"] == eding_hour) &
                            (self._Table["track"] == track))]) != 0:
            return True
        else:
            return False

    def Table_filtered(self, filter, row_key):
        return self._Table[self._Table[row_key] == filter]

    def book(self, id, strating_hour, eding_hour, track):
        """Booking track for client"""
        number = self.new_reservation_number(id)
        new_row = {"reservation_num": number,
                   "client's_id": id, "starting_hour": strating_hour,
                   "ending_hour": eding_hour, "track": track}
        self._Table = concat([self._Table, DataFrame([new_row])],
                             ignore_index=True)
        self._Data = self._Table.to_dict(orient='list')
        self.safe_Data_to_Reservations()

    def new_reservation_number(self, id):
        Table = self._Table[self._Table["client's_id"] == id]
        numbers = Table.to_dict(orient='list')["reservation_num"]
        try:
            return numbers[-1] + 1
        except:
            return 1

    def remove_booking(self, id, strating_hour, eding_hour, track):
        """Removes clients reservation"""
        self._Table = self._Table[~((self._Table["client's_id"] == id) &
                                    (self._Table[
                                        "starting_hour"] == strating_hour) &
                                    (self._Table[
                                        "ending_hour"] == eding_hour) &
                                    (self._Table["track"] == track))]
        self._Data = self._Table.to_dict(orient='list')
        self.safe_Data_to_Reservations()

    def safe_Data_to_Reservations(self):
        file = "Reservations.json"
        self.safe_to_file_dict(file, self._Data, "w", '"Data"')


class Aviability_and_prices(File_menagement):
    def __init__(self, starting_hour, swimming_time, pool_name, track=0):
        """
        defining Aviability_and_prices class
        self :: str
        starting_hour :: int
        ending_hour :: int
        track :: int
        """
        super().__init__(pool_name)
        # TimeTable.__init__(self)
        day = dt.fromisoformat(starting_hour).date()
        self._day = day
        self._starting_hour = starting_hour
        self._swimming_time = swimming_time
        self._weekday = self.weekday_()
        self._working_hours = self.load_working_hours()
        self._track = int(track)
        self._ending_hour = self.ending_hour()

    @property
    def get_working_hours(self):
        "returns working_hours"
        return self._working_hours

    @property
    def get_swimming_time(self):
        return self._swimming_time

    @property
    def get_tracks(self):
        return super().get_tracks

    @property
    def get_track(self):
        return self._track

    @property
    def get_ending_hour(self):
        return self._ending_hour

    def load_working_hours(self):
        '''asking for workinghours of Swimming_pool'''
        file = "Working_hours_weekly.json"
        return self.import_from_file(file, "Week")[f'{self._weekday}']

    def set_working_hours(self, weekday, new_working_hours):
        '''setting workinghours of Swimming_pool'''
        file = "Working_hours_weekly.json"
        Day = self.import_from_file(file, "Week")
        Day[f'{weekday}'] = new_working_hours
        self.safe_to_file_dict(file, Day, "w", '"Week"')

    def weekdays_(self, day):
        days = ["Monday", "Tuesday", "Wednesday",
                "Thrusday", "Friday", "Saturday", "Sunday"]
        return days[day]

    def weekday_(self):
        return self.weekdays_(self._day.weekday())

    def ending_hour(self):
        return self.add_time(self._starting_hour, self._swimming_time, 0)

    def add_time(self, starting_hour, time, days):
        hours,  minutes = time.split(":")
        add_time = timedelta(days, 0, 0, 0, int(minutes), int(hours))
        return dt.isoformat(dt.fromisoformat(starting_hour)
                            + add_time).replace('T', ' ')

    def find_available_track(self, Hazards):
        if self._track == 0 and self.any_track_available(Hazards) is True:
            track = 1
            while track <= self._tracks:
                if self.track_available(self._track, Hazards) is True:
                    return track
        if self.track_available(self._track, Hazards) is True:
            return self._track

    def track_available(self, track, Hazards) -> bool or int:  # type: ignore
        """checks if track is free at asked hour"""
        Hazards_track = Hazards[Hazards["track"] == track]
        if len(Hazards_track) < 5:
            return True
        return False

    def any_track_available(self, Hazards):
        """checks if any track is free at asked hour"""
        if len(Hazards) < self._tracks * 5:
            return True

    def risky_reservations(self, starting_hour, ending_hour):
        get = TimeTable("Maly")
        Table = get.table()
        new_Table = Table[~((Table['starting_hour'] >= ending_hour) |
                            (Table['ending_hour'] <= starting_hour))]
        return new_Table

    def set_next_day(self, starting_hour):
        hours,  minutes = self._working_hours[0].split(":")
        starting_hour = dt.fromisoformat(starting_hour)
        starting_hour = starting_hour.replace(hour=int(hours),
                                              minute=int(minutes))
        starting_hour = self.add_time(dt.isoformat(starting_hour), "00:00", 1)
        ending_hour = self.add_time(starting_hour, self._swimming_time, 0)
        return starting_hour, ending_hour

    def hour_in_working_hours(self, starting_hour, ending_hour):
        starting_hour = self.datetime_to_time(starting_hour)
        ending_hour = self.datetime_to_time(ending_hour)
        if self._working_hours[0] < starting_hour:
            if self._working_hours[1] > ending_hour:
                return True
        return False

    def datetime_to_time(self, datetime):
        time = dt.strptime(datetime, "%Y-%m-%d %H:%M:%S")
        return time.strftime("%H:%M:%S")

    def potential_reser_hour(self, starting_hour, ending_hour):
        if self._working_hours != [None, None]:
            if self.hour_in_working_hours(starting_hour, ending_hour) is True:
                starting_hour = self.add_time(starting_hour, "00:15", 0)
                    # psoobily should implement timestamp changer
                ending_hour = self.add_time(ending_hour, "00:15", 0)
            else:
                """zresetuj do ranka następnego dnia"""
                self.set_next_day(starting_hour)
        return starting_hour, ending_hour

    def suggest_resevation(self):
        starting_hour = self._starting_hour
        ending_hour = self._ending_hour
        while False is False:
            Hazards = self.risky_reservations(starting_hour, ending_hour)
            if type(self.find_available_track(Hazards)) is int:
                track = self.find_available_track(Hazards)
                break
            starting_hour, ending_hour = self.potential_reser_hour(
                                        starting_hour, ending_hour)
        return starting_hour, ending_hour, track


class Price(Client):
    def __init__(self, id, res_numer, pool_name):
        super().__init__(id, pool_name)

        self._res_numer = res_numer

        self._clients_age = self.client_age()
        self._clients_age_type = self.clients_age_type()
        self._swimming_time = self.swimming_time()
        self._reservation = self.find_reservation()
        self._day = self.day()
        self._weekday = self.weekday_()
        self._price = self.price()

    @property
    def get_price(self):
        return self._price

    @property
    def get_swimming_time(self):
        return self._swimming_time

    @property
    def get_clients_age(self):
        return self._clients_age

    @property
    def get_clients_age_type(self):
        return self._clients_age_type

    def import_prices(self):
        file = "Prices.json"
        fees = self.import_from_file(file, "Prices")["Hourly_fee"]
        discounts = self.import_from_file(file, "Prices")["Discounts"]
        return fees, discounts

    def weekdays_(self, day):
        days = ["Monday", "Tuesday", "Wednesday",
                "Thrusday", "Friday", "Saturday", "Sunday"]
        return days[day]

    def weekday_(self):
        return self.weekdays_(self._day.weekday())

    def client_age(self):
        return dt.today().date() - date.fromisoformat(self._birthday)

    def swimming_time(self):
        get = TimeTable(self._pool_name)
        get.get_Table

    def clients_age_type(self):
        if self._clients_age >= timedelta(12*365):
            return "Adult"
        elif timedelta(3*365) <= self._clients_age < timedelta(12*365):
            # possibly should implemtent age changer
            return "Kid_up_to_12"
        elif timedelta(0*365) <= self._clients_age < timedelta(3*365):
            return "Kid_up_to_3"

    def find_reservation(self):
        get = TimeTable(self._pool_name)
        Table = get.get_Table
        row = Table[(Table["reservation_num"] == self._res_numer) &
                    (Table["client's_id"] == str(self._id))]
        return row

    def day(self):
        reservation = self.find_reservation()
        return dt.fromisoformat(reservation["starting_hour"][0]).date()

    def swimming_time(self):
        reservation = self.find_reservation()
        starting_hour = dt.fromisoformat(reservation["starting_hour"][0])
        ending_hour = dt.fromisoformat(reservation["ending_hour"][0])
        return (ending_hour - starting_hour).total_seconds() // 3600

    def price(self):
        fees, discounts = self.import_prices()
        fee = fees[self._clients_age_type]
        discount = (1-(discounts[self._weekday])/100)
        hours = self._swimming_time
        return int(int(fee*discount)*hours)


class earnings_meanagement(File_menagement):
    def __init__(self, day: dt,pool_name,  income: int = 0, tax: int = 0):
        super().__init__(pool_name)
        self._earnings = self.earnings_from_file()
        self._day = day
        self._income = income
        self._tax = tax
        self._day_earnings = self.day_earnings()
        self._days_gross = 0
        self._days_tax = 0
        self.find_all_day_earnings()

    @property
    def get_earnings(self):
        return self._earnings

    @property
    def get_days_gross(self):
        return self._days_gross

    @property
    def get_days_tax(self):
        return self._days_tax

    def earnings_from_file(self):
        return self.import_from_file("Made_money.json", "Money")

    def find_all_day_earnings(self):
        for key in self._day_earnings.keys():
            self._days_gross += self._day_earnings[key]["Gross imcome"]
            self._days_tax += self._day_earnings[key]["Tax"]

    def day_earnings(self):
        day_earnings = {}
        for key in self._earnings.keys():
            if dt.fromisoformat(key).date() == dt.fromisoformat(self._day).date():
                day_earnings[key] = self._earnings[key]
        return day_earnings

    def add_earnings(self):
        self._earnings[self._day] = {
                "Gross imcome": self._income,
                "Tax": self._tax
        }

    def save_new_eranings(self):
        self.add_earnings()
        self.safe_to_file_dict("Made_money.json", self._earnings,
                               "w", '"Money"')
