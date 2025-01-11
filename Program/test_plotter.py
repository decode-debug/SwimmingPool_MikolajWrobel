from Program.plotter import get_pools, Reservation_suggestion_handler
from Program.plotter import Payment_handler, swimming_pool_creator


def test_get_pools():
    assert get_pools() == ['Maly', 'Obrotny']


def test_Reservation_suggestion_handler_check_reservation_aviablity():
    suggestion = Reservation_suggestion_handler("2024-11-04 11:00:00",
                                                "02:00", "Maly", 1,
                                                "500005", 1)
    suggestion.check_reservation_aviablity()
    assert suggestion.get_syggestion == ('2024-11-04 11:00:00',
                                         '2024-11-04 13:00:00', [1])


def test_Payment_handler_get_single_payment():
    get = Payment_handler("Maly")
    data = get.get_single_payment("500005", 1)
    assert data == (7500, 2.0, 'Adult')


def test_Payment_handler_age_type_pol():
    get = Payment_handler("Maly")
    data = get.age_type_pol("Adult")
    assert data == "Dorosły"


def test_swimming_pool_creator_open_file():
    get = swimming_pool_creator("Maly")
    Data = {
           "Clients": {
            "570002": ["Ala Makota", "2010-12-09", 0, 0, 1],
            "500005": ["Alice Police", "1989-07-09", 1, 0, 1],
            "580003": ["Arthur Davidson", "1978-09-07", 1, 0, 1],
            "670003": ["Bob Marley", "1978-09-07", 1, 0, 1],
            "720009": ["Charlie Hudson", "1978-09-07", 0, 0, 1],
            "080008": ["Pletewka", "Not a person", 5, 1, 10],
            "570013": ["Ania Mapsa", "2024-09-07", 0, 0, 1]
            }
    }
    data = get.open_file("Pools/Maly_Pool_Data/Clients.json")
    assert data == Data


def test_swimming_pool_creator_pools_and_passwords():
    get = swimming_pool_creator("Maly")
    Data = ({"Pools": {"Maly": 6, "Obrotny": 8}},
            {"passwords": {"Maly": "pipr", "Obrotny": "pipr"}})
    data = get.pools_and_passwords()
    assert data == Data
