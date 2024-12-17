from typing import List


class Swimming_pool:
    def __init__(self, name, working_hours):
        """
        defining Swimming_pool class
        self :: str
        name :: str
        working_hours :: typle
        """
        self._name = name
        self._working_hours = working_hours


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

    def trackaviable(self) -> bool or int:
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
    def __init__(self, strating_hour, eding_hour, track, name, working_hours):
        """
        self :: str
        strating_hour :: int
        eding_hour :: int
        track :: int
        name :: str
        working_hours :: tuple
        """
        super(Aviability_and_prices).__init__(strating_hour, eding_hour, track)
        super(Swimming_pool).__init__(name, working_hours)

    def table_storage(self) -> List[List[str,int,int,int]]:
        """stores datatable about reservations"""
        Data = [
            ['Alice Police', 1200, 1400, 2],
            ['Bob Marley', 1800, 2000, 3],
            ['Charlie Hudson', 1730, 2030, 1],
            [' Arthur Davidson', 1300, 1445, 6],
            ['Płetewka', 1600, 2000, 5]
        ]
        return Data

    def table(self) -> List[str], List[int], List[int], List[int]:
        """Sorts and decrips Data"""
        list_name, list_starting_hour, list_ending_hour, list_track = list(map(list, zip(*sorted(TimeTable.table_storage()))))
        return list_name, list_starting_hour, list_ending_hour, list_track

    def book(self):
        """Booking track for client"""
        Table = TimeTable.table_storage()


class Finance_raport:
    pass
