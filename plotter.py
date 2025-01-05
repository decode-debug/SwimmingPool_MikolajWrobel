from swimming_pool_class import Aviability_and_prices, Swimming_pool
from swimming_pool_class import File_menagement, Dict_of_clients
from swimming_pool_class import TimeTable, Price, earnings_meanagement
import json
import maskpass
from datetime import datetime as dt
from datetime import time
import re
from colorama import Fore, Back, Style, init
# from InquirerPy import inquirer
# from prompt_toolkit import prompt
from PyInquirer import prompt
from datetime import date
import math


class change_prices():
    pass


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

    def input_bithday(self):
        question = {
            'type': 'input',
            'name': 'day',
            'message': "Podaj liczbę osób zamierzających pływać w szkółce: ",
            'validate': lambda day: True if
            re.match(r'^\d{4}:\d{2}:\d{2}$', day)
            else "Źle podałeś wartość - podaj 1 lub 0"
        }
        if self._class_or_cust == 0:
            self._birthday = int(prompt(question)['day'])
        elif self._class_or_cust == 1:
            self._birthday = "Not a person"

    def input_marurity(self):
        if self._group_size == 1:
            string = "(jeśli tak podaj 1 w przeciwnym razie 0)"
            maturity = f"Czy pływak/czka jest dorosły {string}: "
            wrong = "Źle podałeś/aś wartość - podaj liczbę całkowitą od 0 do 1"
        elif self._group_size > 1:
            maturity = "Podaj liczbę dorosłych pływaków: "
            wrong = f"Źle podałeś/aś wartość - podaj liczbę całkowitą od 0 do {self._group_size}"

        question = [{
            'type': 'input',
            'name': 'mature',
            'message': f"{maturity}",
            'validate': lambda mature: True
            if (self._group_size == 1) and (mature == '1' or mature == '0') or
            (self._group_size > 1) and (int(mature) <= self._group_size)
            else f"{wrong}"
        }]
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
        self.input_bithday()
        self.input_marurity()
        self.create_clients_number()
        new_client = Dict_of_clients()
        Data = [self._name, self._birthday, self._maturity,
                self._class_or_cust, self._group_size]
        new_client.Add_client(self._id, Data)
        if self._class_or_cust == 1:
            print("Szkółka pływacka dodana")
        elif self._class_or_cust == 0:
            print("Klient dodany")


# new_client = Create_client()
# new_client.create_client()


def choose_whats_next():
    questions = [{
        'type': 'list',
        'name': 'choice',
        'message': 'Choose an option:',
        'choices': ["Zamknięcie programu", "Rezerwacja",
                    "Płatność", "Raport Finansowy"],
    }]
    answers = prompt(questions)
    print(f"Wybrałeś: {answers['choice']}")
    return answers['choice']


class Get_from_keyboard():
    def __init__(self):
        pass

    def get_password(self, pool_name):
        get = File_menagement()
        password = maskpass.advpass()
        if password != get.import_from_file("passwords.json", pool_name):
            exit()

    def get_tracks(self, pool_name):
        pool = Swimming_pool(pool_name)
        tracks = pool.get_tracks
        return tracks

    def import_decision(self):
        str = "godzinę(wpisz Tak lub Nie)"
        inncorrect = "tak wpisz Tak jeśli nie Nie"
        question = [
            {
                'type': 'input',
                'name': 'data',
                'message': f'Czy klient chce zarezreowawać na tę {str}',
                'validate': lambda data: True if data in ["Tak", "Nie"]
                else f"Podaj decyzję klienta jeśli {inncorrect}"
            }
         ]
        return prompt(question[0])["data"]

    def yes_no(self):
        questions = [{
            'type': 'list',
            'name': 'choice',
            'message': 'Choose an option:',
            'choices': ["Tak", "Nie"],
        }]
        return prompt(questions)

    def import_pool(self):
        get = File_menagement()
        pools = get.import_from_file("Pools.json", 'Pools').keys()
        not_found = f'Basen nie istnieje, wpisz jeden z {pools}'

        questions = [{
                'type': 'input',
                'name': 'data',
                'message': 'Podaj nazwę basenu:',
                'validate': lambda pool: True if pool in pools
                else f'{not_found}'
            }]
        ans = prompt(questions[0])
        return ans["data"]

    def import_id(self):
        string = "(Jeśli klient jescze nie ma id wpisz 0)"
        stri = "poinformuj że go nie ma pisząc 0"
        incorrect = f"Podaj poprawenie id [w formacie 0000000] lub {stri}"

        questions = [{
                'type': 'input',
                'name': 'data',
                'message': f"Podaj numer karty klienta {string}:",
                'validate': lambda id: True if
                re.match(r'^\d{6}$', id) or re.match(r'^\d{1}$', id)
                else f'{incorrect}'
            }]
        ans = prompt(questions[0])
        return ans["data"]

    def import_swimming_start(self):
        request = 'Podaj datę i godzinę wejścia do basenu, '
        request_ending = "proszoną przez klienta w formacie RRRR-MM-DD 00-00-00"
        incorrect = 'RRRR-MM-DD 00:00:00 np. 2077-07-07 07:07:07'
        questions = [{
                'type': 'input',
                'name': 'data',
                'message': f'{request}{request_ending}:',
                'validate': lambda date: True if
                re.match(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$', date)
                else f'Podaj datę w formacie iso {incorrect}'
            }]
        ans = prompt(questions[0])
        return ans["data"]

    def import_swimming_time(self):
        incorrect = 'np. 03:30 oznacza 3 godziny i 30 min'
        questions = [{
            'type': 'input',
            'name': 'data',
            'message': "Jak długo klient zamierza pływać(podaj w formacie HH:MM):",
            'validate': lambda id: True if
            re.match(r'^\d{2}:\d{2}$', id) and
            (time().fromisoformat(id) >= time.fromisoformat("01:00"))
            else f"Podaj poprawnie czas - w formacie HH:MM {incorrect}"
        }]
        ans = prompt(questions[0])
        return ans["data"]

    def import_track(self, pool_name):
        request = "klient zamierza pływać(podaj liczbę z przedziału [1,"
        request_ending = ''
        if pool_name != '':
            tracks = self.get_tracks(pool_name)
            request_ending2 = f"{tracks}], jeśli klientowi wszystko jedno wpisz 0)"
        questions = [{
            'type': 'input',
            'name': 'data',
            'message': f"Na jakim torze {request}{request_ending}:",
            'validate': lambda track: True if 0 <= int(track) <= tracks
            else f"Podaj poprawnie tor jako liczbę z przedziału [0,{tracks}]"
        }]
        ans = prompt(questions[0])
        return ans["data"]

    def import_res_data(self):
        questions = [{
            'type': 'input',
            'name': 'data',
            'message': "Podaj numer rezerwacji klienta, jeśli klient już wpisał swoje wszystkie, wpisz 0:",
            # 'validate': lambda track:
            # else f"Podaj poprawnie liczbę"
        }]
        ans = prompt(questions[0])
        return ans["data"]

    def import_assert_paynment(self):
        questions = [{
            'type': 'input',
            'name': 'data',
            'message': "Czy klient zapłacił",
            'validate': lambda pay: True if pay in ['Tak', 'Nie']
            else "Podaj poprawnie daną (Tak/Nie)"
        }]
        ans = prompt(questions[0])
        return ans["data"]

    def import_day(self):
        incorrect = ' np. 2077-07-07 07:07:07'
        questions = [{
            'type': 'input',
            'name': 'data',
            'message': "Który dzień cię intersuje:",
            'validate': lambda date: True if
            re.match(r'^\d{4}-\d{2}-\d{2}$', date)
            else f'Podaj datę w formacie iso RRRR-MM-DD{incorrect}'
        }]
        ans = prompt(questions[0])
        return ans["data"]


class Reservation_suggestion_handler():
    def __init__(self, reserved_from, reserved_time, pool_name, track, id):
        self._reserved_from = reserved_from
        self._reserved_time = reserved_time
        self._pool_name = pool_name
        self._track = int(track)
        self._id = id
        self._sugg_starting = None
        self._sugg_ending = None
        self._sugg_track = None

    def check_reservation_aviablity(self):
        available = Aviability_and_prices(self._reserved_from,
                                          self._reserved_time,
                                          self._pool_name, self._track)
        suggestion = available.suggest_resevation()
        self._sugg_starting, self._sugg_ending, self._sugg_track = suggestion

    def plot_reservation(self):
        print("Sugestia rezerwacji:")
        print(f"> godzina wejścia do wody: {self._sugg_starting}")
        print(f"> godzina wyjścia z wody: {self._sugg_ending}")
        print(f"> tor : {self._sugg_track}")

    def decision(self):
        decide = Get_from_keyboard()
        decision = decide.import_decision()
        if decision == "Tak":
            book = TimeTable()
            book.book(self._id, self._sugg_starting,
                      self._sugg_ending, self._track)
            self.report_and_save()

    def report_and_save(self):
        print(f"{Style.BRIGHT}{Fore.GREEN}Rezerwacja przyjęta")
        print(f"{Fore.RED}Czy chcesz cofnąć akcję?")
        yes_no = Get_from_keyboard()
        if yes_no.yes_no() == "Tak":
            removebook = TimeTable()
            removebook.remove_booking(self._id, self._sugg_starting,
                                      self._sugg_ending, self._track)
        print(f"{Fore.CYAN}", end="")

    def reservation_suggestion(self):
        self.check_reservation_aviablity()
        self.plot_reservation()
        self.decision()


class Payment_handler(Get_from_keyboard):
    def __init__(self):
        super().__init__()

    def get_single_payment(self, id, resevation):
        """It can not be parted since I can pay fro more thean one swimming"""
        bill = Price(id, resevation)
        price = bill.get_price
        swimming_time = bill.get_swimming_time
        age_type = bill.get_clients_age_type
        return price, swimming_time, age_type

    def get_payment_data(self):
        data = []
        id = int(self.import_id())
        while id != 0:
            res = int(self.import_res_data())
            while res != 0:
                one_payment = self.get_single_payment(id, res), id, res
                data.append(one_payment)
                res = int(self.import_res_data())
            id = int(self.import_id())
        return data

    def print_date_and_time(self):
        self._today = date.today()
        self._datetime = dt.today().strftime("%Y-%m-%d %H:%M:%S")
        now = dt.now()
        self._current_time = now.strftime("%H:%M:%S")
        print("DATE:", self._today, self._current_time)

    def age_type_pol(self, age):
        ages = {
            "Adult": "Dorosły",
            "Kid_up_to_12": "Dziecko do 12 lat",
            "Kid_up_to_3": "Dziecko do 3 lat"
        }
        return ages[age]

    def print_billing_data(self, reservation, position):
        age = self.age_type_pol(reservation[0][2])
        print(f'{position:3}. Wiek: {age}, Czas: {reservation[0][1]:5}', end='')
        print(f', Cena:{reservation[0][0]//100:3}.{reservation[0][0]%100:2}')

    def print_payments(self):
        self._total_price = 0
        ii = 0
        data = self.get_payment_data()
        print('--------------------------------------------')
        self.print_date_and_time()
        print('--------------------------------------------')
        for reservation in data:
            ii += 1
            self.print_billing_data(reservation, ii)
            self._total_price += reservation[0][0]
        self._total_price = self._total_price

    def tax(self):
        tax_to_round = (self._total_price * 0.08)
        self._tax = math.ceil(tax_to_round)

    def assert_paynment(self):
        pay = self.import_assert_paynment()
        if pay == "Tak":
            return True
        elif pay == "Nie":
            return False

    def save_earned_money(self):
        save = earnings_meanagement(self._datetime, self._total_price, self._tax)
        if self.assert_paynment() is True:
            save.save_new_eranings()

    def print_bill(self):
        self.print_payments()
        self.tax()
        print('--------------------------------------------')
        print(f'Płatność: {self._total_price//100:>31}.{self._total_price%100:2}')
        print(f'Podatek: {self._tax//100:>32}.{self._tax%100:2}')
        print('--------------------------------------------')
        self.save_earned_money()


class Finance_raport_handler(Get_from_keyboard):
    def __init__(self):
        super().__init__()
        self._day = self.import_days_earnigs()

    def import_days_earnigs(self):
        return self.import_day()

    def print_all_day_transactions(self):
        money = earnings_meanagement(self._day)
        earnings = money.get_day_earnings
        ii = 0
        for earning in earnings:
            ii += 1
            hour = earning.key()
            gross = earning[hour]["Gross imcome"]
            tax = earning[hour]["Tax"]
            print(f"{ii}.{hour} Brutto: {gross//100:>5}.", end='')
            print(f"{gross%100:2} Podatek: {tax//100:>5}.{tax%100:2}", end='')
            print(f" Netto: {(gross - tax)//100:>5}.{(gross - tax)%100:2}")

    def print_all_day_income(self):
        money = earnings_meanagement(self._day)
        gross = money.get_days_gross
        tax = money.get_days_tax
        print(f"Brutto: {gross//100:>5}.", end='')
        print(f"{gross%100:2} Podatek: {tax//100:>5}.{tax%100:2}", end='')
        print(f" Netto: {(gross - tax)//100:>5}.{(gross - tax)%100:2}")

    def print_report(self):
        print('--------------------------------------------')
        self.print_all_day_transactions()
        print('--------------------------------------------')
        self.print_all_day_income()

    def report(self):
        self.import_days_earnigs()
        self.print_report()


class decision_handlers(Get_from_keyboard):
    def __init__(self, pool_name):
        super().__init__()
        self._pool_name = pool_name

    def reservation_handler(self):
        id = self.import_id()
        if id == "0":
            new_client = Create_client()
            new_client.create_client()
        reserved_from = self.import_swimming_start()
        reserved_time = self.import_swimming_time()
        track = self.import_track(self._pool_name)
        suggest = Reservation_suggestion_handler(reserved_from, reserved_time,
                                                 self._pool_name, track, id)
        suggest.reservation_suggestion()

    def payment_handler(self):
        pay = Payment_handler()
        pay.print_bill()

    def finance_raport(self):
        report = Finance_raport_handler()
        report.report()



def bootapp():
    pass


def run_in_terminal():
    get = Get_from_keyboard()
    pool_name = get.import_pool()
    decision = decision_handlers(pool_name)
    get.get_password(pool_name)
    terminal = choose_whats_next()
    while terminal != "Zamknięcie programu":
        if terminal == "Rezerwacja":
            decision.reservation_handler()
        elif terminal == "Płatność":
            decision.payment_handler()
        elif terminal == "Raport Finansowy":
            decision.finance_raport()
        terminal = choose_whats_next()


def main():
    print(f'{Style.BRIGHT}{Fore.CYAN}Gdzie chcesz odpalić program')
    print(f"W aplikacji czy Terminalu:{Style.NORMAL}{Fore.YELLOW}")
    a = input()
    if a.lower() == "terminal" or a.lower() == 't':
        print(f"{Fore.CYAN}", end="")
        run_in_terminal()
    elif a.lower() == "aplikacja" or 'a':
        bootapp()
    else:
        ValueError("Oczekiwana odpowiedź: terminal, t, aplikacja lub a")


if __name__ == "__main__":
    main()
