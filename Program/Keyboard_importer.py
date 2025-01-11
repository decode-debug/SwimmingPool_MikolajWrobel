from PyInquirer import prompt
import re
from swimming_pool_class import File_menagement, Dict_of_clients, Swimming_pool
import json
import maskpass
import math
from datetime import time


class Create_client():
    def __init__(self, pool_name):
        self._pool_name = pool_name

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
            'message': "Podaj dzień urodzin: ",
            'validate': lambda day: True if
            re.match(r'^\d{4}:\d{2}:\d{2}$', day)
            else "Źle podałeś wartość - podaj 0000:00:00"
        }
        if self._class_or_cust == 0:
            self._birthday = prompt(question)['day']
        elif self._class_or_cust == 1:
            self._birthday = "Not a person"

    def input_marurity(self):
        if self._group_size == 1:
            string = "(jeśli tak podaj 1 w przeciwnym razie 0)"
            maturity = f"Czy pływak/czka jest dorosły {string}: "
            wrong = "Źle podałeś/aś wartość - podaj liczbę całkowitą od 0 do 1"
        elif self._group_size > 1:
            maturity = "Podaj liczbę dorosłych pływaków: "
            wrong = f" - podaj liczbę całkowitą od 0 do {self._group_size}"

        question = [{
            'type': 'input',
            'name': 'mature',
            'message': f"{maturity}",
            'validate': lambda mature: True
            if (self._group_size == 1) and (mature == '1' or mature == '0') or
            (self._group_size > 1) and (int(mature) <= self._group_size)
            else f"Źle podałeś/aś wartość{wrong}"
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
        open = File_menagement(self._pool_name)
        other_clients = open.import_from_file("Clients.json", "Clients")
        # with (open(file, 'r')) as json_file:
        #     data = json.load(json_file)
        # other_clients = data["Clients"]
        other_nums = other_clients.keys()
        danger_nums = [num for num in other_nums
                       if number <= int(num) <= (number+9999)]
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
        new_client = Dict_of_clients(self._pool_name)
        Data = [self._name, self._birthday, self._maturity,
                self._class_or_cust, self._group_size]
        new_client.Add_client(self._id, Data)
        if self._class_or_cust == 1:
            print("Szkółka pływacka dodana")
        elif self._class_or_cust == 0:
            print(f"Klient dodany, jego id to {self._id}")


def choose_whats_next():
    questions = [{
        'type': 'list',
        'name': 'choice',
        'message': 'Wybierz opcję:',
        'choices': ["Zamknięcie programu", "Rezerwacja",
                    "Płatność", "Raport Finansowy",
                    "Ustawienia"],
    }]
    answers = prompt(questions)
    print(f"Wybrałeś: {answers['choice']}")
    return answers['choice']


class Get_from_keyboard():
    def __init__(self):
        pass

    def get_password(self, pool_name):
        get = File_menagement(pool_name)
        password = maskpass.advpass()
        if password != get.import_from_file("passwords.json",
                                            "passwords")[pool_name]:
            exit()

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
            'name': 'data',
            'message': 'Wybierz opcję:',
            'choices': ["Tak", "Nie"],
        }]
        return prompt(questions)["data"]

    def import_pool(self, pools=0):
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

    def import_new_pool(self):
        questions = [{
                'type': 'input',
                'name': 'data',
                'message': 'Podaj nazwę basenu:'
            }]
        ans = prompt(questions[0])
        return ans["data"]

    def import_id(self):

        def check_id(id):
            if (re.match(r'^\d{6}$', id) or re.match(r'^\d{1}$', id)) is False:
                return False
            sum = 0
            if len(id) == 6:
                for num in id:
                    sum += int(num)
                sum -= int(id[-1])
                if sum % 10 == int(id[-1]):
                    return True
            elif int(id) == 0:
                return True
            return False

        string = "(Jeśli klient jescze nie ma id wpisz 0)"
        stri = "poinformuj że go nie ma pisząc 0"
        incorrect = f"Podaj poprawenie id [w formacie 0000000] lub {stri}"

        questions = [{
                'type': 'input',
                'name': 'data',
                'message': f"Podaj numer karty klienta {string}:",
                'validate': lambda id: True if check_id(id) is True
                else f'{incorrect}'
            }]
        ans = prompt(questions[0])
        return ans["data"]

    def import_swimming_start(self):
        request = 'Podaj datę i godzinę wejścia do basenu, '
        request_ending = "proszoną przez klienta w formacie "
        incorrect = 'RRRR-MM-DD 00:00:00 np. 2077-07-07 07:07:07'
        questions = [{
                'type': 'input',
                'name': 'data',
                'message': f'{request}{request_ending}RRRR-MM-DD 00:00:00:',
                'validate': lambda date: True if
                re.match(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$', date)
                else f'Podaj datę w formacie iso {incorrect}'
            }]
        ans = prompt(questions[0])
        return ans["data"]

    def import_swimming_time(self):
        incorrect = 'np. 03:30 oznacza 3 godziny i 30 min'
        string = "(podaj w formacie HH:MM)"
        questions = [{
            'type': 'input',
            'name': 'data',
            'message': f"Jak długo klient zamierza pływać{string}:",
            'validate': lambda id: True if
            re.match(r'^\d{2}:\d{2}$', id) and
            (time().fromisoformat(id) >= time.fromisoformat("01:00"))
            else f"Podaj poprawnie czas - w formacie HH:MM {incorrect}"
        }]
        ans = prompt(questions[0])
        return ans["data"]

    def import_track(self, pool_name, tracks):
        request = "klient zamierza pływać(podaj liczbę z przedziału [1,"
        if pool_name != '':
            request_ending2 = f"{tracks}], jeśli klientowi wszystko jedno "
        questions = [{
            'type': 'input',
            'name': 'data',
            'message': f"Na jakim torze {request}{request_ending2}wpisz 0):",
            'validate': lambda track: True  if 0 <= int(track) <= tracks
            else f"Podaj poprawnie tor jako liczbę z przedziału [0,{tracks}]"
        }]
        return [int(prompt(questions[0])["data"])]

    def import_res_data(self):
        string = ' jeśli klient już podał już swoje wszystkie rezrwacje, '
        string2 = 'wpisz 0, jeśli klient nie pamięta wpisz "Nie"'
        questions = [{
            'type': 'input',
            'name': 'data',
            'message': f"Podaj numer rezerwacji klienta,{string}{string2}:",
            'validate': lambda track: True if (track.isdigit() or track == '0' or track == "Nie")
            else "Podaj liczbę w formacie 000000, wpisz 0 lub napisz Nie"
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
        return prompt(questions[0])["data"]

    def choose_settings(self):
        questions = [{
            'type': 'list',
            'name': 'choice',
            'message': 'Wybierz opcję:',
            'choices': ["Zmień godziny pracy", "Zmień hasło",
                        "Zmień przeceny", "Zmień opłatę godzinową",
                        "Zmień liczbę torów", "Stwórz nowy basen"],
        }]
        answers = prompt(questions)
        print(f"Wybrałeś: {answers['choice']}")
        return answers['choice']

    def import_password(self):
        questions = [{
            'type': 'input',
            'name': 'data',
            'message': "Podaj nowe hasło(bez znaków polskich):",
        }]
        return prompt(questions[0])["data"]

    def import_price(self, ii):
        def age_type_pol(ii):
            ages = {
                1: "Dorosły",
                2: "Dziecko do 12 lat",
                3: "Dziecko do 3 lat"
            }
            return ages[ii]

        questions = [{
            'type': 'input',
            'name': 'data',
            'message': f"Podaj nową cenę w groszach dla {age_type_pol(ii)}:",
            "validate": lambda price: True if price.isdigit() else "Podaj liczbę!"

        }]
        return prompt(questions[0])["data"]

    def import_week_day(self):

        questions = [{
            'type': 'input',
            'name': 'data',
            'message': "Podaj dzień tygodnia:",
            "validate": lambda day: True if day in days.keys()
            else f'Podaj poprawnie dzień tydnia(jeden z listy {days.keys()})'
        }]
        days = {
            "Poniedzialek": "Monday",
            "Wtorek": "Tuesday",
            "Sroda": "Wednesday",
            "Czwartek": "Thrusday",
            "Piatek": "Friday",
            "Sobota": "Saturday",
            "Niedziela": "Sunday"
        }
        return days[prompt(questions[0])["data"]]

    def import_dicount(self, eng_day):
        days = {
            "Monday": "Poniedzialek",
            "Tuesday": "Wtorek",
            "Wednesday": "Sroda",
            "Thrusday": "Czwartek",
            "Friday": "Piatek",
            "Saturday": "Sobota",
            "Sunday": "Niedziela"
        }
        day = days[eng_day]

        questions = [{
            'type': 'input',
            'name': 'data',
            'message': f"Podaj nową przecenę w dniu {day}(w procentach):",
            'validate': lambda date: True if re.match(r'^\d{2}$', date)
            else 'Podaj w formacie 00'
            }]
        return prompt(questions[0])["data"]

    def import_working_hours(self, eng_day):
        days = {
            "Monday": "Poniedzialek",
            "Tuesday": "Wtorek",
            "Wednesday": "Sroda",
            "Thursday": "Czwartek",
            "Friday": "Piatek",
            "Saturday": "Sobota",
            "Sunday": "Niedziela"
        }
        day = days[eng_day]
        stri = "(Jeśli basen w tym dniu jest zamknięty wpisz 0)"
        incorrect = ' np. 2077-07-07 07:07:07'
        questions = [{
            'type': 'input',
            'name': 'data',
            'message': f"Podaj godzinę otwarcia basenu w dniu {day} {stri}:",
            'validate': lambda hour: True if
            re.match(r'^\d{2}:\d{2}$', hour) or hour == "0"
            else f'Podaj datę w formacie iso RRRR-MM-DD{incorrect} lub wpisz 0'
        },
         {
            'type': 'input',
            'name': 'data',
            'message': f"Podaj godziny zamknięcia basenu w dniu {day} {stri}:",
            'validate': lambda hour: True if
            re.match(r'^\d{2}:\d{2}$', hour)
            else f'Podaj datę w formacie iso RRRR-MM-DD{incorrect} lub wpisz 0'
        }
        ]
        open = prompt(questions[0])["data"]
        if open == '0':
            return [None, None]
        close = prompt(questions[1])["data"]
        return [open, close]

    def import_tracks(self):
        questions = [{
            'type': 'input',
            'name': 'data',
            'message': "Podaj liczbę towrów:",
            'validate': lambda tracks: True if
            int(tracks) else 'Podaj liczbę całkowitą!'
        }]
        return prompt(questions[0])["data"]

    def import_people_swimming(self, tracks):
        limit = int(math.floor((tracks*0.35)))
        questions = [{
            'type': 'input',
            'name': 'data',
            'message': "Podaj liczbę osób chcących pływać w basenie:",
            'validate': lambda swimmers: True if int(math.ceil(
                (swimmers)/5)) <= limit
            else f'Podaj liczbę całkowitą mniejszą niż {limit * 5}!'
        }]
        return int(math.ceil((prompt(questions[0])["data"])/5)) * 5
