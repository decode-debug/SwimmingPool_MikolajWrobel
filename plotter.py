from swimming_pool_class import Swimming_pool
import json
# Type password without left CTRL press key
import maskpass # importing maskpass library


def get_from_file(file, need):
    with open(file, "r") as json_file:
        data = json.load(json_file)
    return data[need]


def input_value(values, mode):
    value = None
    if mode == 0:
        request = 'Podaj nazwę basenu:'
        not_a_str = 'Nazwa basenu jest typu string'
        not_found = f'Basen pod nazwą {value} nie istnieje, wpisz jeden z {values}'
    elif mode == 1:
        request = 'Podaj dzień tygodnia w, którym klient chce pływać:'
        not_a_str = 'Dzień jest typu string'
        not_found = f'Dzień {value} nie istnieje, wpisz jeden z {values}'
    elif mode == 2:
        request = 'Podaj datę i godzinę wejścia do basenu, proszoną przez klienta w formacie RRRR-MM-DD 00-00-00'
    while value is None:
        print(request)
        value = input()
        if type(value) is not str:
            value = None
            ValueError(not_a_str)
        if value not in values:
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
    print(Podaj dzień)
    week_day = input_value(day_list, 1)
    # pool = Swimming_pool(pool_name, day)


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
