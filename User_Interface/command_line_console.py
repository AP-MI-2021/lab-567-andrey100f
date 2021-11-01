from Domain.cheltuieli import get_to_string
from Logic.CRUD import adaugare_cheltuiala, modificare_cheltuiala


def adaugare(id, numar_apartament, suma, data, tip, lista):
    try:
        return adaugare_cheltuiala(id, numar_apartament, suma, data, tip, lista)
    except ValueError as ve:
        print("Eroare: {}". format(ve))
        return lista


def modificare(id, numar_apartament, suma, data, tip, lista):
    try:
        return modificare_cheltuiala(id, numar_apartament, suma, data, tip, lista)
    except ValueError as ve:
        print("Eroare: {}". format(ve))
        return lista


def afisare_toate(lista):
    for cheltuiala in lista:
        print(get_to_string(cheltuiala))


def ajutor():
    print("Legenda comenzilor:")
    print("add -> adaugare cheltuiala")
    print("update -> modificare cheltuiala")
    print("show_all -> afisarea tuturor cheltuielilor")
    print("stop -> oprirea programului")


def meniu():
    lista = []
    lista = adaugare_cheltuiala(1010, 5, 100, "19.10.2021", "intretinere", lista)
    lista = adaugare_cheltuiala(2020, 10, 300, "19.10.2021", "alte cheltuieli", lista)
    merge = True
    while merge is True:
        text = input("Intorduceti comenzile: ")
        lista_comenzi = text.split("-")
        for comanda in lista_comenzi:
            optiune = comanda.split(" ")
            if optiune[0] == "add":
                lista = adaugare(int(optiune[1]), int(optiune[2]), int(optiune[3]), optiune[4], optiune[5], lista)
            elif optiune[0] == "update":
                lista = modificare(int(optiune[1]), int(optiune[2]), int(optiune[3]), optiune[4], optiune[5], lista)
            elif optiune[0] == "show_all":
                afisare_toate(lista)
            elif optiune[0] == "help":
                ajutor()
            elif optiune[0] == "stop":
                merge = False
            else:
                print("Comanda gresita! Incercati din nou!")


meniu()
