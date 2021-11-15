from Domain.cheltuieli import get_suma, get_id
from Logic.CRUD import adaugare_cheltuiala
from Logic.functionalitati import stergere_cheltuieli_apartament, adunare_valoare_cheltuieli, cele_mai_mari_cheltuieli, \
    ordonare_dupa_suma, calculare_cheltuieli_lunare, undo, redo, adaugare_cheltuiala_undo_redo


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


def test_ordonare_dupa_suma():
    lista = []
    lista = adaugare_cheltuiala(1010, 5, 100, "19.10.2021", "intretinere", lista)
    lista = adaugare_cheltuiala(2020, 10, 300, "17.11.2021", "alte cheltuieli", lista)
    lista = adaugare_cheltuiala(3030, 20, 250, "14.02.2021", "canal", lista)
    lista_ordonata = ordonare_dupa_suma(lista)
    assert get_id(lista_ordonata[0]) == 2020
    assert get_id(lista_ordonata[1]) == 3030
    assert get_id(lista_ordonata[2]) == 1010


def test_calculare_cheltuieli_lunare():
    lista = []
    lista = adaugare_cheltuiala(1010, 5, 100, "19.10.2021", "intretinere", lista)
    lista = adaugare_cheltuiala(2020, 5, 300, "17.10.2021", "alte cheltuieli", lista)
    lista = adaugare_cheltuiala(3030, 5, 250, "14.02.2021", "canal", lista)
    lista_cheltuieli = calculare_cheltuieli_lunare(5, lista)
    assert lista_cheltuieli[0] == ["10", 400]
    assert lista_cheltuieli[1] == ["02", 250]


def test_undo_redo():
    # 1
    lista = []
    lista_undo = []
    lista_redo = []

    # 2
    lista = adaugare_cheltuiala_undo_redo(7388, 1, 965, "24.06.2021", "alte cheltuieli", lista, lista_undo, lista_redo)
    assert get_id(lista[0]) == 7388
    assert len(lista) == 1

    # 3
    lista = adaugare_cheltuiala_undo_redo(4513, 15, 91, "26.10.2021", "canal", lista, lista_undo, lista_redo)
    assert get_id(lista[0]) == 7388
    assert get_id(lista[1]) == 4513
    assert len(lista) == 2

    # 4
    lista = adaugare_cheltuiala_undo_redo(7155, 3, 810, "06.08.2021", "intretinere", lista, lista_undo, lista_redo)
    assert get_id(lista[0]) == 7388
    assert get_id(lista[1]) == 4513
    assert get_id(lista[2]) == 7155
    assert len(lista) == 3

    # 5
    lista = undo(lista, lista_undo, lista_redo)
    assert get_id(lista[0]) == 7388
    assert get_id(lista[1]) == 4513
    assert len(lista) == 2

    # 6
    lista = undo(lista, lista_undo, lista_redo)
    assert get_id(lista[0]) == 7388
    assert len(lista) == 1

    # 7
    lista = undo(lista, lista_undo, lista_redo)
    assert len(lista) == 0

    # 8
    lista = undo(lista, lista_undo, lista_redo)
    assert lista is None

    # 9
    lista = []
    lista_undo = []
    lista_redo = []
    lista = adaugare_cheltuiala_undo_redo(7388, 1, 965, "24.06.2021", "alte cheltuieli", lista, lista_undo, lista_redo)
    lista = adaugare_cheltuiala_undo_redo(4513, 15, 91, "26.10.2021", "canal", lista, lista_undo, lista_redo)
    lista = adaugare_cheltuiala_undo_redo(7155, 3, 810, "06.08.2021", "intretinere", lista, lista_undo, lista_redo)
    assert get_id(lista[0]) == 7388
    assert get_id(lista[1]) == 4513
    assert get_id(lista[2]) == 7155
    assert len(lista) == 3

    # 10
    lista = redo(lista, lista_undo, lista_redo)
    assert len(lista) == 3
    assert get_id(lista[0]) == 7388
    assert get_id(lista[1]) == 4513
    assert get_id(lista[2]) == 7155

    # 11
    lista = undo(lista, lista_undo, lista_redo)
    lista = undo(lista, lista_undo, lista_redo)
    assert get_id(lista[0]) == 7388
    assert len(lista) == 1

    # 12
    lista = redo(lista, lista_undo, lista_redo)
    assert len(lista) == 2
    assert get_id(lista[1]) == 4513
    assert get_id(lista[0]) == 7388

    # 13
    lista = redo(lista, lista_undo, lista_redo)
    assert len(lista) == 3
    assert get_id(lista[2]) == 7155
    assert get_id(lista[1]) == 4513
    assert get_id(lista[0]) == 7388

    # 14
    lista = undo(lista, lista_undo, lista_redo)
    lista = undo(lista, lista_undo, lista_redo)
    assert get_id(lista[0]) == 7388
    assert len(lista) == 1

    # 15
    lista = adaugare_cheltuiala_undo_redo(6404, 18, 754, "30.09.2021", "intretinere", lista, lista_undo, lista_redo)
    assert len(lista) == 2
    assert get_id(lista[0]) == 7388
    assert get_id(lista[1]) == 6404

    # 16
    lista = redo(lista, lista_undo, lista_redo)
    assert len(lista) == 2
    assert get_id(lista[0]) == 7388
    assert get_id(lista[1]) == 6404

    # 17
    lista = undo(lista, lista_undo, lista_redo)
    assert len(lista) == 1
    assert get_id(lista[0]) == 7388

    # 18
    lista = undo(lista, lista_undo, lista_redo)
    assert len(lista) == 0

    # 19
    lista = redo(lista, lista_undo, lista_redo)
    lista = redo(lista, lista_undo, lista_redo)
    assert len(lista) == 2
    assert get_id(lista[0]) == 7388
    assert get_id(lista[1]) == 6404

    # 20
    lista = redo(lista, lista_undo, lista_redo)
    assert len(lista) == 2
    assert get_id(lista[0]) == 7388
    assert get_id(lista[1]) == 6404
