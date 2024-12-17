import swimming_pool_class

class user_friendly_interface:
    def __init__(self):
        pass


def bootapp():
    pass

def run_in_terminal():
    print('Podaj nazwę basenu:')
    while():
        try:
            pool_name = input()
            if type(pool_name) != str:
                pass
        except ValueError:
            print((""))

def main():
    print('Gdzie chcesz odpalić program')
    print("W aplikacji czy Terminalu:")
    a = input()
    if a.lower() == ("terminal" or 't'):
        run_in_terminal()
    elif a.lower() == ("aplikacja" or 'a'):
        bootapp()
    else:
        ValueError("Oczekiwana odpowiedź: terminal, t, aplikacja lub a")


if __name__ == "__main__":
    main()




    print('What do you want to do')