from Domain.cheltuieli import get_to_string
from Logic.CRUD import adaugare_cheltuiala, stergere_cheltuiala, modificare_cheltuiala
from Logic.functionalitati import stergere_cheltuieli_apartament, adunare_valoare_cheltuieli, \
    cele_mai_mari_cheltuieli, ordonare_dupa_suma


def afisare_meniu():
    print("1. Adăugare cheltuială")
    print("2. Ștergere cheltuială")
    print("3. Modificare cheltuială")
    print("4. Ștergerea tuturor cheltuielilor pentru un apartament dat")
    print("5. Adunarea unei valori la toate cheltuielile dintr-o dată citită.")
    print("6. Determinarea celei mai mari cheltuieli pentru fiecare tip de cheltuială.")
    print("7. Ordonarea cheltuielilor descrescător după sumă.")
    print("a. Afisare cheltuieli")
    print("x. Iesire")


def adaugare_cheltuiala_ui(lista):
    try:
        id = int(input("Dati un ID: "))
        numar_apartament = int(input("Dati numarul apartamentului: "))
        suma = int(input("Dati suma: "))
        data = input("Precizati data: ")
        tip = input("Precizati tipul cheltuielii: ")
        return adaugare_cheltuiala(id, numar_apartament, suma, data, tip, lista)
    except ValueError as ve:
        print("Eroare: {}". format(ve))
        return lista


def stergere_cheltuiala_ui(lista):
    try:
        id = int(input("Dati ID-ul: "))
        return stergere_cheltuiala(id, lista)
    except ValueError as ve:
        print("Eroare: {}". format(ve))
        return lista


def modificare_cheltuiala_ui(lista):
    try:
        id = int(input("Dati ID-ul: "))
        numar_apartament = int(input("Dati numarul apartamentului: "))
        suma = int(input("Dati suma: "))
        data = input("Precizati data: ")
        tip = input("Precizati tipul: ")
        return modificare_cheltuiala(id, numar_apartament, suma, data, tip, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def cele_mai_mari_cheltuieli_ui(lista):
    lista_maxime = cele_mai_mari_cheltuieli(lista)
    print("Maximul pentru tipul << intretinere >> este: ")
    print(get_to_string(lista_maxime[0]))
    print("Maximul pentru tipul << canal >> este: ")
    print(get_to_string(lista_maxime[1]))
    print("Maximul pentru tipul << alte cheltuieli >> este: ")
    print(get_to_string(lista_maxime[2]))


def stergere_cheltuieli_apartament_ui(lista):
    numar_apartament = int(input("Dati numarul apartamentului: "))
    return stergere_cheltuieli_apartament(numar_apartament, lista)


def adunare_valoare_cheltuieli_ui(lista):
    data = input("Dati data: ")
    valoare = int(input("Dati valoarea: "))
    return adunare_valoare_cheltuieli(data, lista, valoare)


def ordonare_dupa_suma_ui(lista):
    lista_ordonata = ordonare_dupa_suma(lista)
    print("Ordinea este: ")
    for cheltuiala in lista_ordonata:
        print(get_to_string(cheltuiala))


def afisare_toate(lista):
    for cheltuiala in lista:
        print(get_to_string(cheltuiala))


def meniu():
    afisare_meniu()
    lista = []
    lista = adaugare_cheltuiala(1010, 5, 100, "19.10.2021", "intretinere", lista)
    lista = adaugare_cheltuiala(2020, 10, 300, "17.11.2021", "alte cheltuieli", lista)
    lista = adaugare_cheltuiala(3030, 20, 250, "14.02.2021", "canal", lista)
    merge = True
    while merge is True:
        optiune = input("Dati o optiune: ")
        if optiune == "1":
            lista = adaugare_cheltuiala_ui(lista)
        elif optiune == "2":
            lista = stergere_cheltuiala_ui(lista)
        elif optiune == "3":
            lista = modificare_cheltuiala_ui(lista)
        elif optiune == "4":
            lista = stergere_cheltuieli_apartament_ui(lista)
        elif optiune == "5":
            lista = adunare_valoare_cheltuieli_ui(lista)
        elif optiune == "6":
            cele_mai_mari_cheltuieli_ui(lista)
        elif optiune == "7":
            ordonare_dupa_suma_ui(lista)
        elif optiune == "a":
            afisare_toate(lista)
        elif optiune == "x":
            merge = False
        else:
            print("Optiune gresita! Reincercati!")
