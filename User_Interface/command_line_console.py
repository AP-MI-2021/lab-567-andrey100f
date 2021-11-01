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
    merge = True
    while merge is True:
        text = input("Intorduceti comanda: ")
        comanda = text.split(" ")
        if comanda[0] == "add":
            lista = adaugare(int(comanda[1]), int(comanda[2]), int(comanda[3]), comanda[4], comanda[5], lista)
        elif comanda[0] == "update":
            lista = modificare(int(comanda[1]), int(comanda[2]), int(comanda[3]), comanda[4], comanda[5], lista)
        elif comanda[0] == "show_all":
            afisare_toate(lista)
        elif comanda[0] == "help":
            ajutor()
        elif comanda[0] == "stop":
            merge = False
        else:
            print("Comanda gresita! Incercati din nou!")


meniu()
