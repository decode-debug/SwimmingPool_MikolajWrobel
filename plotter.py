from swimming_pool_class import Swimming_pool, Client, Get_client
import json
import maskpass
from datetime import datetime


def end_program():
    print("Do you want to continue")


def week_days(day):
    days = ["Poniedziałek", "Wtorek", "środa",
            "Czwartek", "Piątek", "Sobota", "Niedziela"]
    return days(day)


def get_from_file(file, need):
    with open(file, "r") as json_file:
        data = json.load(json_file)
    return data[need]


def input_value(values, mode):
    value = None
    if mode == 0:
        request = 'Podaj nazwę basenu:'
        not_a_type = 'Nazwa basenu jest typu string'
        not_found = f'Basen pod nazwą {value} nie istnieje, wpisz jeden z {values}'
        types = str
    elif mode == 1:
        request = 'Podaj dzień tygodnia w, którym klient chce pływać:'
        not_a_type = 'Dzień jest typu string'
        not_found = f'Dzień {value} nie istnieje, wpisz jeden z {values}'
        types = str
    elif mode == 2:
        request = 'Podaj datę i godzinę wejścia do basenu, proszoną przez klienta w formacie RRRR-MM-DD 00-00-00'
        not_a_type = 'Podaj datę w formacie iso RRRR-MM-DD 00-00-00 np. 2077-07-07 07:07:07'
        not_found = ''
        types = datetime

    while value is None:
        print(request)
        value = input()
        if type(value) is not types:
            value = None
            ValueError(not_a_type)
        if value not in values and mode != 2:
            value = None
            ValueError(not_found)
    return value

def bootapp():
    pass


def run_in_terminal():
    pool_list = get_from_file("Pools.json", 'Pools')
    day_list = get_from_file("Working_hours_weekly.json", 'Week').keys()
    pool_name = input_value(pool_list, 0)
    password = maskpass.advpass()
    if password != get_from_file("passwords.json", pool_name):
        exit()
    kill_terminal = 0
    while kill_terminal == 0:
        string = "(Jeśli klient jescze nie ma numeru wpisz 0)"
        print(f"Podaj numer karty klienta {string}")
        card_num = input()
        if card_num == 0:
            Get_client.create_client()
            card_num = Swimming_pool.genrate_client_number()
            print(f"Client card number is {card_num}")
        reservation_hour = datetime.fromisoformat(input_value(None, 2))
        reservation_time = input("Jak długo klient zamierza pływać")
        week_day = week_days(reservation_hour.weekday())
        pool = Swimming_pool(pool_name, week_day)

        kill_terminal = end_program()


def main():
    print('Gdzie chcesz odpalić program')
    print("W aplikacji czy Terminalu:")
    a = input()
    if a.lower() == "terminal" or 't':
        run_in_terminal()
    elif a.lower() == "aplikacja" or 'a':
        bootapp()
    else:
        ValueError("Oczekiwana odpowiedź: terminal, t, aplikacja lub a")


if __name__ == "__main__":
    main()
    print('What do you want to do')
