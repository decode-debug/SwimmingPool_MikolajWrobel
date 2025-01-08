from swimming_pool_class import Aviability_and_prices, File_menagement
from Keyboard_importer import Create_client, Get_from_keyboard
from Keyboard_importer import choose_whats_next
from swimming_pool_class import TimeTable, Price, earnings_meanagement
from datetime import datetime as dt
from colorama import Fore, Back, Style, init
# from InquirerPy import prompt # this library is uggested
# instead of InquirerPy in case of you using python 3.9 (Better looking)
from datetime import date
import math
# flake8:


class change_prices():
    pass


class Reservation_suggestion_handler(TimeTable):
    def __init__(self, reserved_from, reserved_time, pool_name, track, id):
        super().__init__()
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
            if self.check_if_reservations_not_same(self._id,
                                                   self._sugg_starting,
                                                   self._sugg_ending,
                                                   self._sugg_track) is True:
                print(f"{Fore.RED}Już taka rezerwacja istnieje")
            else:
                self.book(self._id, self._sugg_starting,
                          self._sugg_ending, self._track)
                self.report_and_save()

    def report_and_save(self):
        print(f"{Style.BRIGHT}{Fore.GREEN}Rezerwacja przyjęta")
        print(f"{Fore.RED}Czy chcesz cofnąć akcję?")
        yes_no = Get_from_keyboard()
        answer = yes_no.yes_no()
        if answer == "Tak":
            removebook = TimeTable()
            removebook.remove_booking(self._id, self._sugg_starting,
                                      self._sugg_ending, self._track)
        print(f"{Fore.CYAN}", end="")

    def reservation_suggestion(self):
        self.check_reservation_aviablity()
        self.plot_reservation()
        self.decision()


class Payment_handler(Get_from_keyboard, TimeTable):
    def __init__(self):
        super(Get_from_keyboard, self).__init__()
        super(TimeTable, self).__init__()

    def get_single_payment(self, id, resevation):
        """It can not be parted since I can pay fro more thean one swimming"""
        bill = Price(id, resevation)
        price = bill.get_price
        swimming_time = bill.get_swimming_time
        age_type = bill.get_clients_age_type
        return price, swimming_time, age_type

    def import_res(self):
        res = self.import_res_data()
        while res == "Nie":
            Table = self.Table_filtered(id, "client's_id")
            if len(Table) != 0:
                print(Table)
            else:
                print("Nie ma rezerwacji")
            res = self.import_res_data()
        return int(res)

    def get_payment_data(self):
        data = []
        id = int(self.import_id())
        while id != 0:
            res = self.import_res()
            while res != 0:
                one_payment = self.get_single_payment(id, res), id, res
                data.append(one_payment)
                res = self.import_res()
            id = int(self.import_id())
            res = int(res)
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

    def print_day(self, pool_name):
        print(f'W dniu: {self._day}. Basen "{pool_name}" zarorobił:')

    def print_all_day_transactions(self):
        money = earnings_meanagement(self._day)
        earnings = money.get_earnings
        ii = 0
        for earning in earnings:
            ii += 1
            gross = earnings[earning]["Gross imcome"]
            tax = earnings[earning]["Tax"]
            print(f"{ii}.{earning} Brutto: {gross//100:>5}.", end='')
            print(f"{gross%100:2} Podatek: {tax//100:>5}.{tax%100:2}", end='')
            print(f" Netto: {(gross - tax)//100:>5}.{(gross - tax)%100:2}")

    def print_all_day_income(self):
        money = earnings_meanagement(self._day)
        gross = money.get_days_gross
        tax = money.get_days_tax
        print(f"Zarobki z całego dnia Brutto: {gross//100:>5}.", end='')
        print(f"{gross%100:2} Podatek: {tax//100:>5}.{tax%100:2}", end='')
        print(f" Netto: {(gross - tax)//100:>5}.{(gross - tax)%100:2}")

    def print_report(self, pool_name):
        string = "----------------------------"
        print(f'--------------------------------------------{string}')
        print(f'--------------------------------------------{string}')
        self.print_day(pool_name)
        print(f'--------------------------------------------{string}')
        self.print_all_day_transactions()
        print(f'--------------------------------------------{string}')
        self.print_all_day_income()
        print(f'--------------------------------------------{string}')
        print(f'--------------------------------------------{string}')

    def report(self, pool_name):
        self.print_report(pool_name)


class settings_handler(Get_from_keyboard, File_menagement):
    def __init__(self, choice, pool_name):
        super(Get_from_keyboard, self).__init__()
        super(File_menagement, self).__init__()
        self._choice = choice
        self._pool_name = pool_name

    def change_working_hours(self):
        """Fix"""
        weekday = self.import_week_day()
        working_hours = self.import_from_file("Working_hours_weekly.json",
                                              "Week")
        new_hours = self.import_working_hours(weekday)
        working_hours[weekday] = new_hours
        self.safe_to_file_dict("Working_hours_weekly.json",
                               working_hours, "w", '"Week"')

    def change_password(self):
        passwords = self.import_from_file("passwords.json", "passwords")
        new_password = self.import_password()
        passwords[self._pool_name] = new_password
        self.safe_to_file_dict("passwords.json", passwords, "w", '"passwords"')

    def change_discounts(self):
        prices = self.import_from_file("Prices.json", "Prices")
        discounts = prices["Discounts"]
        for day in discounts:
            print(f"dicount: {discounts[day]}")
            discounts[day] = int(self.import_dicount(day))
            self.safe_to_file_dict("Prices.json", prices,
                                   "w", '"Prices"')

    def change_hourly_payment(self):
        """Fix"""
        prices = self.import_from_file("Prices.json", "Prices")
        fees = prices["Hourly_fee"]
        for fee in fees:
            print(f'fee: {fees[fee]}')
            fees[fee] = int(self.import_price())
            self.safe_to_file_dict("Prices.json", prices, "w", '"Prices"')

    def change_tracks(self):
        all_tracks = self.import_from_file("Pools.json", "Pools")
        tracks = self.import_tracks()
        all_tracks[self._pool_name] = int(tracks)
        self.safe_to_file_dict("Pools.json", all_tracks,
                               "w", '"Pools"')

    def add_new_swimming_pool():



    def change(self):
        if self._choice == "Zmień godziny pracy":
            self.change_working_hours()
        elif self._choice == "Zmień hasło":
            self.change_password()
        elif self._choice == "Zmień przeceny":
            self.change_discounts()
        elif self._choice == "Zmień opłatę godzinową":
            self.change_hourly_payment()
        elif self._choice == "Zmień liczbę torów":
            self.change_tracks()


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
        report.report(self._pool_name)

    def settings(self):
        choice = self.choose_settings()
        set = settings_handler(choice, self._pool_name)
        set.change()


    def seperate_next_task(self):
        print("\n\n\n\n")


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
        elif terminal == "Ustawienia":
            decision.settings()
        decision.seperate_next_task()
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
