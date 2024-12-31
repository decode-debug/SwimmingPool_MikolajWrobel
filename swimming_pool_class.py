# from typing import List
import json
from pandas import DataFrame
from datetime import datetime as dt


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

    def safe_to_file_dict(self, file, Data, name=0):
        with open(file, 'w') as json_file:
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
    def __init__(self, name, day, tracks=1):
        """
        defining Swimming_pool class
        self :: str
        name :: str
        working_hours :: typle
        """
        self._name = name
        self._tracks = self.load_tracks()
        self._day = day
        self._working_hours = self.load_working_hours()
        pass

    @property
    def get_working_hours(self):
        "returns working_hours"
        return self._working_hours

    @property
    def get_name(self):
        "returns pool name"
        return self._name

    @property
    def get_day(self):
        "returns day of the week"
        return self._day

    @property
    def get_tracks(self):
        "returns ammount of swimming tracks"
        return self._tracks  # ??????????????

    def load_tracks(self):
        '''asking for ammount of tracks in Swimming_pool'''
        file = "Pools.json"
        load = File_menagement()
        return load.import_from_file(file, "Pools")[f'{self._name}']

    def load_working_hours(self):
        '''asking for workinghours of Swimming_pool'''
        file = "Working_hours_weekly.json"
        load = File_menagement()
        return load.import_from_file(file, "Week")[f'{self._day}']

    def set_tracks(self, new_tracks):
        '''setting ammount of tracks in Swimming_pool'''
        file = "Pools.json"
        open = File_menagement()
        tracks = open.import_from_file(file, "Pools")
        tracks[f'{self._name}'] = new_tracks
        open.safe_to_file_dict(file, tracks, '"Pools"')

    def set_working_hours(self, new_working_hours):
        '''setting workinghours of Swimming_pool'''
        file = "Working_hours_weekly.json"
        open = File_menagement()
        Day = open.import_from_file(file, "Week")
        Day[f'{self._day}'] = new_working_hours
        open.safe_to_file_dict(file, Day, '"Week"')


class Client:
    def __init__(self, id, name, maturity, class_or_cust, group_size=1):
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
        self._id = id

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

    def Create_client_from_clientsFile():
        return Create_client.create_client()  # ???????????????????

    def client_from_file(self, id):
        Dict_of_clients.find_client(id)

    def add_client_to_file(self):
        add = Dict_of_clients()
        add.Add_client()


class Create_client(Client):
    def __init__(self):
        pass

    def input_class_or_cust(self):
        print("Jeśli klient to szółka pływcka podaj 1 w przeciwnym razie 0")
        self._class_or_cust = bool(input())
        if self._class_or_cust is not True or False:
            print("Źle podałeś wartość - podaj 0 lub 1")
            self.input_class_or_cust()

    def input_name(self):
        if self._class_or_cust == 0:
            name = input("Podaj imię i nazwisko klienta")
            if (len(name.split(" ")) == 2):
                self._name = name
            else:
                self.input_name
        elif self._class_or_cust == 1:
            self._name = input("Podaj nazwę szkółki pływackiej")

    def input_group_size(self):
        if self._class_or_cust == 1:
            print("Podaj liczbę osób zamierzających pływać w szkółce")
            self._group_size = input()
        if self._group_size < 0:
            print("Źle podałeś wartość - podaj liczbę od 1 do nieksończoności")
            self.input_group_size()

    def input_marurity(self):
        if self._group_size == 1:
            string = "(jeśli tak podaj 1 w przeciwnym razie 0)"
            maturity = int(input(f"Czy pływak jest dorosły {string}"))
        elif self._group_size > 1:
            maturity = int(input("Podaj liczbę dorosłych pływaków"))
        if maturity <= 0:
            self.input_marurity()

    def create_clients_number(self):
        number = 0
        name, surname = self._name.split(" ")
        number += 100000 * (ord(name[0]) % 10)
        number += 10000 * (ord(surname[0]) % 10)
        file = File_menagement()
        other_clients = file.import_from_file("Clients.json", "Clients")
        other_nums = other_clients.keys()
        danger_nums = [num for num in other_nums if number <= int(num) <= (number+9999)]
        id = number
        while id < number+9999:
            if id in danger_nums:
                id += 10
            else:
                break
        id_str = str(id)
        last_digit = 0
        for digit in id_str:
            last_digit += int(digit)
        id += last_digit % 10
        self._id = id

    def create_client(self):
        self.input_class_or_cust()
        self.input_name()
        self.input_group_size()
        self.input_marurity()
        self.create_clients_number()
        check = False
        check = Dict_of_clients.Add_client()
        if check is False:
            SystemError("Something went seriously wrong")


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
        save.safe_to_file_dict("Clients.json", self._dict, '"Clients"')

    def remove_client(self, id):
        save = File_menagement()
        self.get_dict
        del self._dict[f"{id}"]
        save.safe_to_file_dict("Clients.json", self._dict, '"Clients"')


class Reservation:
    def __init__(self, client_id, track, water_entry, booked_hours):
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
            b = f"with {self._group_size - 1} other customers"
            return a+b
        else:
            a = ""
            for i in self._track:
                a = a + f" {i}"
            str = "{self._name} occupies tracks{a}"
            return f"group of {self._group_size} named {str}"


class Tickets:
    pass


class Aviability_and_prices(Swimming_pool):
    def __init__(self, starting_hour, ending_hour, name,
                 day, track=(-1), tracks=1):
        """
        defining Aviability_and_prices class
        self :: str
        starting_hour :: int
        ending_hour :: int
        track :: int
        """
        super().__init__(name, day, tracks)
        self._starting_hour = starting_hour
        self._ending_hour = ending_hour
        self._track = track
        self._swimming_time = self.swimming_time()
        self._Table = None
        self._num_rows = None

    @property
    def get_swimming_time(self):
        return self._swimming_time

    @property
    def get_tracks(self):
        return super().get_tracks

    def swimming_time(self):
        return self.strptime_double(self._ending_hour, self._starting_hour)

    def strptime_double(self, first, second):
        format = "%Y-%m-%d %H:%M:%S"
        return dt.strptime(first, format) - dt.strptime(second, format)

    def find_aviable_track(self):
        if self.track_aviable(self._track) is True:
            return self._track
        for track in range(1, self._track+1):
            if self.track_aviable(track) is True:
                return track

    def track_aviable(self, track) -> bool or int:  # type: ignore
        """checks if track is free at asked hour"""
        Hazards = self.risky_reservations()
        Hazards_track = Hazards[Hazards["track"] == track]
        if len(Hazards_track) < 5:
            return True
        return False

    def risky_reservations(self):
        get = TimeTable()
        Table = get.table()
        new_Table = Table[~((Table['starting_hour'] >= self._ending_hour) |
                            (Table['ending_hour'] <= self._starting_hour))]
        return new_Table

    def suggest_hour(self):
        pass

    def book_hour(self):
        return TimeTable.book(self._)  # ???????????????????


class TimeTable():
    def __init__(self):
        """stores datatable about reservations"""
        self._Data = {}

    @property
    def get_Data(self):
        return self._Data

    def import_Data_from_Reservations(self):
        get = File_menagement()
        self._Data = get.import_from_file("Reservations.json", "Data")

    def table(self):
        """Sorts and decrypts Data"""
        if len(self._Data) == 0:
            self.import_Data_from_Reservations()
        Table = DataFrame(self._Data,
                          columns=["client's_number", "starting_hour",
                                   "ending_hour", "track"])
        return Table

    def book(self, number, strating_hour, eding_hour, track):
        """Booking track for client"""
        self._Data["client's_number"].append(number)
        self._Data["starting_hour"].append(strating_hour)
        self._Data["ending_hour"].append(eding_hour)
        self._Data["track"].append(track)
        self.safe_Data_to_Reservations()

    def remove_booking(self, number, strating_hour, eding_hour, track):
        """Removes clients reservation"""
        self._Data["client's_number"].remove(number)
        self._Data["starting_hour"].remove(strating_hour)
        self._Data["ending_hour"].remove(eding_hour)
        self._Data["track"].remove(track)
        self.safe_Data_to_Reservations()

    def safe_Data_to_Reservations(self):
        file = "Reservations.json"
        save = File_menagement()
        save.safe_to_file_dict(file, self._Data, '"Data"')
