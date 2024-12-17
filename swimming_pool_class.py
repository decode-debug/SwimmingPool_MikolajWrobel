from typing import List
import json


class Swimming_pool:
    def __init__(self, name, day):
        """
        defining Swimming_pool class
        self :: str
        name :: str
        working_hours :: typle
        """
        self._name = name
        self._day = day
        self._working_hours = Swimming_pool.get_working_hours()

    def get_working_hours(self):
        file = "Working_hours_weekly.json"
        with open(file, "r") as json_file:
            Data = json.load(json_file)
        return Data['Week'][f'{self._day}']

    def set_working_hours(self, new_working_hours):
        file = "Working_hours_weekly.json"
        with open(file, 'r') as json_file:
            Day = json.load(json_file)
            Day['Week'][f'{self._day}'] = list(new_working_hours)
        with open(file, 'w') as json_file:
            json_file.write(json.dumps(Day))


class Client:
    def __init__(self, name, maturity, track, water_entry,
                 booked_hours, group_size=1):
        """
        defining Client class
        self :: str
        name :: str
        maturity :: str
        track :: int
        water_entry :: int
        booked_hours :: int
        group_size :: int
        """
        self._name = name
        self._maturity = maturity
        self._track = track
        self._water_entry = water_entry
        self._booked_hours = booked_hours
        self._group_size = group_size

    def name(self) -> str:
        """returning client's name"""
        return self._name

    def tracks(self) -> str:
        """Printing track occupied by client"""
        if self._group_size == 1:
            return f"{self._name} occupies track {self._track[0]}"
        else:
            a = ""
            for i in self._track:
                a = a + f" {i}"
            return f"group of {self._group_size} named {self._name} occupies tracks{a}"

    def maturity(self) -> str:
        return f"{self._name} is {self._maturity}"


class Tickets:
    pass


class Aviability_and_prices(Swimming_pool):
    def __init__(self, starting_hour, ending_hour, working_hours, track=(-1)):
        """
        defining Aviability_and_prices class
        self :: str
        starting_hour :: int
        ending_hour :: int
        track :: int
        """
        super().__init__(working_hours)
        self._starting_hour = starting_hour
        self._ending_hour = ending_hour
        self._track = track
        self._swimming_time = ending_hour - starting_hour
        self._Table = None
        self._num_rows = None

    def track_aviable(self) -> bool or int:
        """checks if track is free at asked hour"""
        Table = TimeTable.table(self)
        self._Table = Table
        self._num_rows = Table.shape[0]
        for i in range(0, self._num_rows):
            for j in range(1, 3):
                start = self._starting_hour
                if start > Table.iloc[i, j] and start < Table.iloc[i, 2]:
                    return self.suggest_hour(i, j)
        return True

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
        with open(file, "r") as json_file:
            Data = json.load(json_file)
        self._Data = Data["Data"]
        return

    def table(self) -> List[str], List[int], List[int], List[int]:
        """Sorts and decrypts Data"""
        if len(self._Data) == 0:
            TimeTable.import_Data_from_Reservations()
        else:
            list_name, list_starting_hour, list_ending_hour, list_track = list(map(list, zip(*sorted(self._Data))))
        return list_name, list_starting_hour, list_ending_hour, list_track

    def book(self, other, name, strating_hour, eding_hour, track):
        """Booking track for client"""
        self._Data.append([name, strating_hour, eding_hour, track]) #  ????????????????????????????????


class Finance_raport:
    pass
