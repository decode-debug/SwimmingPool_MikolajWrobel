from swimming_pool_class import Swimming_pool, Client
from swimming_pool_class import File_menagement, Dict_of_clients
import json
import maskpass
from datetime import datetime, timedelta, time
import re
# from InquirerPy import inquirer
from PyInquirer import prompt

class Create_client():
    def __init__(self):
        pass

    def input_class_or_cust(self):
        string = "podaj 1 w przeciwnym razie 0: "
        question = {
            'type': 'input',
            'name': 'data',
            'message': f"Jeśli klient-/ka to szółka pływcka {string}",
            'validate': lambda data: True if data == '1' or data == '0'
            else "Źle podałeś wartość - podaj 1 lub 0"
        },
        self._class_or_cust = int(prompt(question)['data'])

    def input_name(self):
        if self._class_or_cust == 0:
            string2 = "(Nie wpisuj znaków polskich)"
            string = f"Podaj imię i nazwisko klienta/ki{string2}"
        elif self._class_or_cust == 1:
            string = "Podaj nazwę szkółki pływackiej"
        question = {
            'type': 'input',
            'name': 'name',
            'message': f"{string}: ",
        },
        self._name = prompt(question)['name']

    def input_group_size(self):
        question = {
            'type': 'input',
            'name': 'data',
            'message': "Podaj liczbę osób zamierzających pływać w szkółce: ",
            'validate': lambda data: True if int(data) > 0
            else "Źle podałeś wartość - podaj 1 lub 0"
        }
        if self._class_or_cust == 1:
            self._group_size = int(prompt(question)['data'])
        elif self._class_or_cust == 0:
            self._group_size = 1

    def input_marurity(self):
        if self._group_size == 1:
            string = "(jeśli tak podaj 1 w przeciwnym razie 0)"
            maturity = f"Czy pływak/czka jest dorosły {string}: "
            wrong = "Źle podałeś/aś wartość - podaj liczbę całkowitą od 0 do 1"
        elif self._group_size > 1:
            maturity = "Podaj liczbę dorosłych pływaków: "
            wrong = f"Źle podałeś/aś wartość - podaj liczbę całkowitą od 0 do {self._group_size}"

        question = {
            'type': 'input',
            'name': 'mature',
            'message': f"{maturity}",
            'validate': lambda mature: True
            if (self._group_size == 1) and (mature == '1' or mature == '0') or
            (self._group_size > 1) and (int(mature) <= self._group_size)
            else f"{wrong}"
        }
        self._maturity = int(prompt(question)['mature'])

    def create_clients_number(self):
        number = 0
        if self._class_or_cust == 0:
            name, surname = self._name.split(" ")
            number += 100000 * (ord(name[0]) % 10)
            number += 10000 * (ord(surname[0]) % 10)
        elif self._class_or_cust == 1:
            number += 100000 * (ord(self._name[0]) % 10)
            number += 10000 * (ord(self._name[1]) % 10)
        file = "Clients.json"
        with (open(file, 'r')) as json_file:
            data = json.load(json_file)
        other_clients = data["Clients"]
        other_nums = other_clients.keys()
        danger_nums = [num for num in other_nums if number <= int(num) <= (number+9999)]
        for ii in range(0, len(danger_nums)):
            danger_nums[ii] = int((int(danger_nums[ii])/10))
        id = number
        while id < number+9999:
            if id/10 in danger_nums:
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
        new_client = Dict_of_clients()
        Data = [self._name, self._maturity,
                self._class_or_cust, self._group_size]
        new_client.Add_client(self._id, Data)
        if self._class_or_cust == 1:
            print("Szkółka pływacka dodana")
        elif self._class_or_cust == 0:
            print("Klient dodany")


# new_client = Create_client()
# new_client.create_client()


def choose_whats_next():
    # choices = ["zamknąć terminal", "dodać nową rezerwację"]
    # selected_option = inquirer.select(
    #     message="Co chcesz dalej robić:",
    #     choices=choices
    # ).execute()
    # print(f"You selected: {selected_option}")
    choices = "zamknąć terminal(1), dodać nową rezerwację(0)"
    selected_option = input(f"Co chcesz dalej robić: {choices}")
    return selected_option


def week_days(day):
    days = ["Poniedzialek", "Wtorek", "sroda",
            "Czwartek", "Piatek", "Sobota", "Niedziela"]
    return days[day]


def get_password(pool_name):
    get = File_menagement()
    password = maskpass.advpass()
    if password != get.import_from_file("passwords.json", pool_name):
        exit()


def import_data(selection , geter):
    get = File_menagement()
    pools = get.import_from_file("Pools.json", 'Pools').keys()
    not_found1 = f'Basen nie istnieje, wpisz jeden z {pools}'

    string = "(Jeśli klient jescze nie ma id wpisz 0)"
    stri = "poinformuj że go nie ma pisząc 0"
    incorrect1 = f"Podaj poprawenie id [w formacie 0000000] lub {stri}"

    request = 'Podaj datę i godzinę wejścia do basenu, '
    request_ending1 = "proszoną przez klienta w formacie RRRR-MM-DD 00-00-00"
    incorrect2 = ' np. 2077-07-07 07:07:07'
    incorrect3 = 'np. 03:30 oznacza 3 godziny i 30 min'

    questions = [

        {
            'type': 'input',
            'name': 'pool',
            'message': 'Podaj nazwę basenu:',
            'validate': lambda pool: True if pool in pools
            else f'{not_found1}'
        },
        {
            'type': 'input',
            'name': 'id',
            'message': f"Podaj numer karty klienta {string}",
            'validate': lambda id: True if
            re.match(r'^\d{6}$', id) or re.match(r'^\d{1}$', id)
            else f'{incorrect1}'
        },
        {
            'type': 'input',
            'name': 'date',
            'message': f'{request}{request_ending1}',
            'validate': lambda date: True if
            re.match(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$', date)
            else f'Podaj datę w formacie iso RRRR-MM-DD 00-00-00{incorrect2}'
        },
        {
            'type': 'input',
            'name': 'time',
            'message': "Jak długo klient zamierza pływać(podaj w formacie HH:MM)",
            'validate': lambda id: True if
            re.match(r'^\d{2}:\d{2}$', id) and
            (time().fromisoformat(id) >= time.fromisoformat("01:00"))
            else f"Podaj poprawnie czas - w formacie HH:MM {incorrect3}"
        }

    ]
    ans = prompt(questions[selection])
    return ans[geter]


def input_value(values, mode):

    value = None
    if mode == 0:
        request = 'Podaj nazwę basenu:'
        not_found = f'Basen pod nazwą {value} nie istnieje, wpisz jeden z {values}'
    elif mode == 1:
        request = 'Podaj dzień tygodnia w, którym klient chce pływać:'
        not_found = f'Dzień {value} nie istnieje, wpisz jeden z {values}'
    elif mode == 2:
        # str2 = ' 2077-07-07 07:07:07'
        not_found = ''

    while value is None:
        print(request)
        value = input()
        if value not in values and mode != 2:
            value = None
            ValueError(not_found)
    return value


def bootapp():
    pass


def run_in_terminal():
    pool_name = import_data(0, "pool")
    get_password(pool_name)
    terminal = 0
    while terminal == 0:
        card_id = import_data(1, "id")
        if card_id == "0":
            new_client = Create_client()
            new_client.create_client()
        reserved_from = datetime.fromisoformat(import_data(2, "date"))
        reserved_time = import_data(3, "time")
        hours, minutes = reserved_time.split(":")
        reserved_to = reserved_from + timedelta(int(hours), int(minutes))
        week_day = week_days(reserved_from.weekday())  # day_list would be better but it is for future me
        pool = Swimming_pool(pool_name, week_day)
        terminal = choose_whats_next()


def main():
    print('Gdzie chcesz odpalić program')
    print("W aplikacji czy Terminalu:")
    a = input()
    if a.lower() == "terminal" or a.lower() == 't':
        run_in_terminal()
    elif a.lower() == "aplikacja" or 'a':
        bootapp()
    else:
        ValueError("Oczekiwana odpowiedź: terminal, t, aplikacja lub a")


if __name__ == "__main__":
    main()
    print('What do you want to do')
