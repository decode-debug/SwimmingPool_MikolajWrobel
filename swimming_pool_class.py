# from typing import List
import json
from pandas import DataFrame
from datetime import datetime as dt
from datetime import date
from datetime import timedelta


class File_menagement():
    def __init__(self):
        pass

    def import_file(self, file):
        with (open(file, 'r')) as json_file:
            return json.load(json_file)

    def import_from_file(self, file, request):
        with (open(file, 'r')) as json_file:
            data = json.load(json_file)
        return data[request]

    def safe_to_file_list(self, file, Data, name=0):
        with open(file, 'w') as json_file:
            json_file.write("{")
            json_file.write("\n")
            json_file.write("   ")
            if name != 0:
                json_file.write(f'{name}:')
                json_file.write("[")
                json_file.write("\n")
            for element in Data:
                json_file.write("       ")
                json_file.write(json.dumps(element))
                if element != Data[-1]:
                    json_file.write(",")
                json_file.write("\n")
            json_file.write("    ")
            json_file.write("]")
            json_file.write("\n")
            json_file.write("}")

    def safe_to_file_dict(self, file, Data, work, name=0):
        with open(file, f'{work}') as json_file:
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


class Swimming_pool:
    def __init__(self, name, day=dt.today().date(), tracks=1):
        """
        defining Swimming_pool class
        self :: str
        name :: str
        working_hours :: typle
        """
        self._name = name
        self._tracks = self.load_tracks()
        self._day = day
        self._weekday = self.weekday_()
        self._working_hours = self.load_working_hours()

    @property
    def get_working_hours(self):
        "returns working_hours"
        return self._working_hours

    @property
    def get_name(self):
        "returns pool name"
        return self._name

    @property
    def get_tracks(self):
        "returns ammount of swimming tracks"
        return self._tracks  # ??????????????

    def weekdays_(self, day):
        days = ["Monday", "Tuesday", "Wednesday",
                "Thrusday", "Friday", "Saturday", "Sunday"]
        return days[day]

    def weekday_(self):
        return self.weekdays_(self._day.weekday())

    def load_tracks(self):
        '''asking for ammount of tracks in Swimming_pool'''
        file = "Pools.json"
        load = File_menagement()
        return load.import_from_file(file, "Pools")[f'{self._name}']

    def load_working_hours(self):
        '''asking for workinghours of Swimming_pool'''
        file = "Working_hours_weekly.json"
        load = File_menagement()
        return load.import_from_file(file, "Week")[f'{self._weekday}']

    def set_tracks(self, new_tracks):
        '''setting ammount of tracks in Swimming_pool'''
        file = "Pools.json"
        open = File_menagement()
        tracks = open.import_from_file(file, "Pools")
        tracks[f'{self._name}'] = new_tracks
        open.safe_to_file_dict(file, tracks, "w", '"Pools"')

    def set_working_hours(self, new_working_hours):
        '''setting workinghours of Swimming_pool'''
        file = "Working_hours_weekly.json"
        open = File_menagement()
        Day = open.import_from_file(file, "Week")
        Day[f'{self._weekday}'] = new_working_hours
        open.safe_to_file_dict(file, Day, "w", '"Week"')


class Client:
    def __init__(self, id):
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
        get = File_menagement()
        file = "Clients.json"
        clients = get.import_from_file(file, "Clients")
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


class Dict_of_clients():
    def __init__(self):
        self._dict = {}

    @property
    def get_dict(self):
        open = File_menagement()
        self._dict = open.import_from_file("clients.json", "Clients")
        return self._dict

    def find_client(self, id):
        """Check's if client is on list"""
        if len(self._dict) == 0:
            self.get_dict
        return id, self._dict[f"{id}"]

    def Add_client(self, id, Data):
        save = File_menagement()
        self.get_dict
        self._dict[f"{id}"] = Data
        save.safe_to_file_dict("Clients.json", self._dict, "w", '"Clients"')

    def remove_client(self, id):
        save = File_menagement()
        self.get_dict
        del self._dict[f"{id}"]
        save.safe_to_file_dict("Clients.json", self._dict, "w", '"Clients"')


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


class Aviability_and_prices(Swimming_pool):
    def __init__(self, starting_hour, swimming_time, name,
                 track=0, tracks=1):
        """
        defining Aviability_and_prices class
        self :: str
        starting_hour :: int
        ending_hour :: int
        track :: int
        """
        day = dt.fromisoformat(starting_hour).date()
        super().__init__(name, day, tracks)
        self._starting_hour = starting_hour
        self._swimming_time = swimming_time
        self._track = track
        self._ending_hour = self.ending_hour()

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

    def ending_hour(self):
        return self.add_time(self._starting_hour, self._swimming_time, 0)

    def add_time(self, starting_hour, time, days):
        hours,  minutes = time.split(":")
        add_time = timedelta(days, 0, 0, 0, int(minutes), int(hours))
        return dt.isoformat(dt.fromisoformat(starting_hour)
                            + add_time).replace('T', ' ')

    def find_available_track(self, Hazards):
        if self._track == 0 and self.any_track_available(Hazards) is True:
            return self._track
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
        get = TimeTable()
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
            starting_hour, ending_hour = self.potential_reser_hour(starting_hour, ending_hour)
        return starting_hour, ending_hour, track


class TimeTable():
    def __init__(self):
        """stores datatable about reservations"""
        self._Data = {}

    @property
    def get_Data(self):
        return self._Data

    @property
    def get_Table(self):
        return self.table()

    def import_Data_from_Reservations(self):
        get = File_menagement()
        self._Data = get.import_from_file("Reservations.json", "Data")

    def table(self):
        """Sorts and decrypts Data"""
        if len(self._Data) == 0:
            self.import_Data_from_Reservations()
        Table = DataFrame(self._Data,
                          columns=["client's_id", "starting_hour",
                                   "ending_hour", "track"])
        return Table

    def book(self, id, strating_hour, eding_hour, track):
        """Booking track for client"""
        self._Data["client's_id"].append(id)
        self._Data["starting_hour"].append(strating_hour)
        self._Data["ending_hour"].append(eding_hour)
        self._Data["track"].append(track)
        self.safe_Data_to_Reservations()

    def remove_booking(self, id, strating_hour, eding_hour, track):
        """Removes clients reservation"""
        self._Data["client's_id"].remove(id)
        self._Data["starting_hour"].remove(strating_hour)
        self._Data["ending_hour"].remove(eding_hour)
        self._Data["track"].remove(track)
        self.safe_Data_to_Reservations()

    def safe_Data_to_Reservations(self):
        file = "Reservations.json"
        save = File_menagement()
        save.safe_to_file_dict(file, self._Data, "w", '"Data"')


class Payment():
    def __init__(self):
        pass


class Price(Client):
    def __init__(self, id, day=dt.today().date()):
        super().__init__(id)
        self._day = day
        self._weekday = self.weekday_()
        self._clients_age = self.client_age()
        self._price = self.price()
        self._swimming_time = self.swimming_time()

    def import_prices(self):
        get = File_menagement()
        file = "Prices.json"
        fees = get.import_from_file(file, "Hourly_fee")
        discounts = get.import_from_file(file, "Discounts")
        return fees, discounts

    def weekdays_(self, day):
        days = ["Monday", "Tuesday", "Wednesday",
                "Thrusday", "Friday", "Saturday", "Sunday"]
        return days[day]

    def weekday_(self):
        return self.weekdays_(self._day.weekday())

    def client_age(self):
        return dt.today().date() - date.fromisoformat(self._birthday)

    def swimming_time():
        get = TimeTable()
        get.get_Table

    def cleints_age_type(self):
        if self._clients_age >= timedelta(12*365):
            return "Adult"
        elif timedelta(3*365) <= self._clients_age < timedelta(12*365):
            # possibly should implemtent age changer
            return "Kid_up_to_12"
        elif timedelta(0*365) <= self._clients_age < timedelta(3*365):
            return "Kid_up_to_3"

    def price(self):
        fees, discounts = self.import_prices()
        fee = fees[self.cleints_age_type()]
        discount = (1-(discounts[self._weekday])/100)
        return int(fee*discount)*self._swimming_time
