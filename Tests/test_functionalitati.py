from Domain.cheltuieli import get_suma, get_id
from Logic.CRUD import adaugare_cheltuiala
from Logic.functionalitati import stergere_cheltuieli_apartament, adunare_valoare_cheltuieli, cele_mai_mari_cheltuieli


def test_stergere_cheltuieli_apartament():
    lista = []
    lista = adaugare_cheltuiala(1010, 5, 100, "19.10.2021", "intretinere", lista)
    lista = adaugare_cheltuiala(2020, 5, 200, "29.10.2001", "alte cheltuieli", lista)
    lista = stergere_cheltuieli_apartament(5, lista)
    assert len(lista) == 0


def test_adunare_valoare_cheltuieli():
    lista = []
    lista = adaugare_cheltuiala(1010, 5, 100, "19.10.2021", "intretinere", lista)
    lista = adaugare_cheltuiala(2020, 10, 300, "19.10.2021", "alte cheltuieli", lista)
    lista = adunare_valoare_cheltuieli("19.10.2021", lista, 200)
    assert get_suma(lista[0]) == 300
    assert get_suma(lista[1]) == 500


def test_cele_mai_mari_cheltuieli():
    lista = []
    lista = adaugare_cheltuiala(1010, 5, 100, "19.10.2021", "intretinere", lista)
    lista = adaugare_cheltuiala(2020, 10, 300, "17.11.2021", "alte cheltuieli", lista)
    lista = adaugare_cheltuiala(3030, 20, 250, "14.02.2021", "canal", lista)
    lista_maxime = cele_mai_mari_cheltuieli(lista)
    assert get_id(lista_maxime[0]) == 1010
    assert get_id(lista_maxime[1]) == 3030
    assert get_id(lista_maxime[2]) == 2020
