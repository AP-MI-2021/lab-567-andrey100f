from Domain.cheltuieli import get_id, get_numar_apartament, get_suma, get_data, get_tip
from Logic.CRUD import adaugare_cheltuiala, verificare_id, stergere_cheltuiala, modificare_cheltuiala


def test_adaugare_cheltuiala():
    lista = []
    lista = adaugare_cheltuiala(1010, 5, 100, "19.10.2021", "intretinere", lista)
    assert len(lista) == 1
    assert get_id(verificare_id(1010, lista)) == 1010
    assert get_numar_apartament(verificare_id(1010, lista)) == 5
    assert get_suma(verificare_id(1010, lista)) == 100
    assert get_data(verificare_id(1010, lista)) == "19.10.2021"
    assert get_tip(verificare_id(1010, lista)) == "intretinere"


def test_stergere_cheltuiala():
    lista = []
    lista = adaugare_cheltuiala(1010, 5, 100, "19.10.2021", "intretinere", lista)
    lista = adaugare_cheltuiala(2020, 1, 200, "29.10.2001", "alte cheltuieli", lista)
    lista = stergere_cheltuiala(2020, lista)
    assert get_id(verificare_id(1010, lista)) == 1010
    assert get_numar_apartament(verificare_id(1010, lista)) == 5
    assert get_suma(verificare_id(1010, lista)) == 100
    assert get_data(verificare_id(1010, lista)) == "19.10.2021"
    assert get_tip(verificare_id(1010, lista)) == "intretinere"


def test_modificare_cheltuiala():
    lista = []
    lista = adaugare_cheltuiala(1010, 5, 100, "19.10.2021", "intretinere", lista)
    lista = adaugare_cheltuiala(2020, 1, 200, "29.10.2001", "alte cheltuieli", lista)
    lista = modificare_cheltuiala(1010, 5, 50, "07.02.2004", "canal", lista)
    assert get_id(verificare_id(1010, lista)) == 1010
    assert get_numar_apartament(verificare_id(1010, lista)) == 5
    assert get_suma(verificare_id(1010, lista)) == 50
    assert get_data(verificare_id(1010, lista)) == "07.02.2004"
    assert get_tip(verificare_id(1010, lista)) == "canal"
