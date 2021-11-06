from Domain.cheltuieli import get_to_string, get_tip, get_numar_apartament, get_suma, get_data, get_id
from Logic.CRUD import adaugare_cheltuiala, stergere_cheltuiala, modificare_cheltuiala, get_by_id
from Logic.functionalitati import stergere_cheltuieli_apartament, adunare_valoare_cheltuieli, \
    cele_mai_mari_cheltuieli, ordonare_dupa_suma, calculare_cheltuieli_lunare, determinare_luna, \
    adaugare_cheltuieli_apartament, scadere_valoare_cheltuieli


def afisare_meniu():
    print("1. Adăugare cheltuială")
    print("2. Ștergere cheltuială")
    print("3. Modificare cheltuială")
    print("4. Ștergerea tuturor cheltuielilor pentru un apartament dat")
    print("5. Adunarea unei valori la toate cheltuielile dintr-o dată citită.")
    print("6. Determinarea celei mai mari cheltuieli pentru fiecare tip de cheltuială.")
    print("7. Ordonarea cheltuielilor descrescător după sumă.")
    print("8. Afișarea sumelor lunare pentru fiecare apartament.")
    print("u. Undo")
    print("r. Redo")
    print("a. Afisare cheltuieli")
    print("x. Iesire")


def adaugare_cheltuiala_ui(lista, undo_operations, redo_operations):
    try:
        id = int(input("Dati un ID: "))
        numar_apartament = int(input("Dati numarul apartamentului: "))
        suma = int(input("Dati suma: "))
        data = input("Precizati data: ")
        tip = input("Precizati tipul cheltuielii: ")
        rezultat = adaugare_cheltuiala(id, numar_apartament, suma, data, tip, lista)
        undo_operations.append([
            lambda: stergere_cheltuiala(id, rezultat),
            lambda: adaugare_cheltuiala(id, numar_apartament, suma, data, tip, lista)
        ])
        redo_operations.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}". format(ve))
        return lista


def stergere_cheltuiala_ui(lista, undo_operations, redo_operations):
    try:
        id = int(input("Dati ID-ul: "))
        rezultat = stergere_cheltuiala(id, lista)
        cheltuiala_de_sters = get_by_id(id, lista)
        undo_operations.append([
            lambda: adaugare_cheltuiala(
                id,
                get_numar_apartament(cheltuiala_de_sters),
                get_suma(cheltuiala_de_sters),
                get_data(cheltuiala_de_sters),
                get_tip(cheltuiala_de_sters),
                rezultat),
            lambda: stergere_cheltuiala(id, lista)
        ])
        redo_operations.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}". format(ve))
        return lista


def modificare_cheltuiala_ui(lista, undo_operations, redo_operations):
    try:
        id = int(input("Dati ID-ul: "))
        numar_apartament = int(input("Dati numarul apartamentului: "))
        suma = int(input("Dati suma: "))
        data = input("Precizati data: ")
        tip = input("Precizati tipul: ")
        rezultat = modificare_cheltuiala(id, numar_apartament, suma, data, tip, lista)
        cheltuiala_veche = get_by_id(id, lista)
        undo_operations.append([
            lambda: modificare_cheltuiala(
                id,
                get_numar_apartament(cheltuiala_veche),
                get_suma(cheltuiala_veche),
                get_data(cheltuiala_veche),
                get_tip(cheltuiala_veche),
                rezultat),
            lambda: modificare_cheltuiala(id, numar_apartament, suma, data, tip, lista)
        ])
        redo_operations.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def cele_mai_mari_cheltuieli_ui(lista):
    lista_maxime = cele_mai_mari_cheltuieli(lista)
    for cheltuiala in lista_maxime:
        if cheltuiala != {}:
            print("Maximul pentru tipul << " + get_tip(cheltuiala) + " >> este: ")
            print(get_to_string(cheltuiala))


def stergere_cheltuieli_apartament_ui(lista, undo_operations, redo_operations):
    numar_apartament = int(input("Dati numarul apartamentului: "))
    rezultat = stergere_cheltuieli_apartament(numar_apartament, lista)
    lista_cheltuieli_vechi = adaugare_cheltuieli_apartament(numar_apartament, lista)
    for cheltuiala in lista_cheltuieli_vechi:
        undo_operations.append([
            lambda: adaugare_cheltuiala(
                get_id(cheltuiala),
                numar_apartament,
                get_suma(cheltuiala),
                get_data(cheltuiala),
                get_tip(cheltuiala),
                rezultat),
            lambda: stergere_cheltuieli_apartament(numar_apartament, lista)
            ])
    redo_operations.clear()
    return rezultat


def adunare_valoare_cheltuieli_ui(lista, undo_operations, redo_operations):
    data = input("Dati data: ")
    valoare = int(input("Dati valoarea: "))
    rezultat = adunare_valoare_cheltuieli(data, lista, valoare)
    undo_operations.append([
        lambda: scadere_valoare_cheltuieli(data, rezultat, valoare),
        lambda: adunare_valoare_cheltuieli(data, lista, valoare)
    ])
    redo_operations.clear()
    return rezultat


def ordonare_dupa_suma_ui(lista):
    lista_ordonata = ordonare_dupa_suma(lista)
    print("Ordinea este: ")
    for cheltuiala in lista_ordonata:
        print(get_to_string(cheltuiala))


def calculare_cheltuieli_lunare_ui(lista):
    numar_apartament = int(input("Dati numarul apartamentului: "))
    lista_cheltuieli = calculare_cheltuieli_lunare(numar_apartament, lista)
    for cheltuiala in lista_cheltuieli:
        cheltuiala[0] = determinare_luna(cheltuiala[0])
        print("Pentru luna: " + cheltuiala[0] + " cheltuielile sunt: " + str(cheltuiala[1]))


def afisare_toate(lista):
    if len(lista) > 0:
        for cheltuiala in lista:
            print(get_to_string(cheltuiala))
    else:
        print("Nu exista cheltuieli!")


def meniu():
    afisare_meniu()
    lista = []
    undo_operations = []
    redo_operations = []
    merge = True
    while merge is True:
        optiune = input("Dati o optiune: ")
        if optiune == "1":
            lista = adaugare_cheltuiala_ui(lista, undo_operations, redo_operations)
        elif optiune == "2":
            lista = stergere_cheltuiala_ui(lista, undo_operations, redo_operations)
        elif optiune == "3":
            lista = modificare_cheltuiala_ui(lista, undo_operations, redo_operations)
        elif optiune == "4":
            lista = stergere_cheltuieli_apartament_ui(lista, undo_operations, redo_operations)
        elif optiune == "5":
            lista = adunare_valoare_cheltuieli_ui(lista, undo_operations, redo_operations)
        elif optiune == "6":
            cele_mai_mari_cheltuieli_ui(lista)
        elif optiune == "7":
            ordonare_dupa_suma_ui(lista)
        elif optiune == "8":
            calculare_cheltuieli_lunare_ui(lista)
        elif optiune == "u":
            if len(undo_operations) > 0:
                operatie = undo_operations.pop()
                redo_operations.append(operatie)
                lista = operatie[0]()
            else:
                print("Nu se poate face undo!")
        elif optiune == "r":
            if len(redo_operations) > 0:
                operatie = redo_operations.pop()
                undo_operations.append(operatie)
                lista = operatie[1]()
            else:
                print("Nu se poate face redo!")
        elif optiune == "a":
            afisare_toate(lista)
        elif optiune == "x":
            merge = False
        else:
            print("Optiune gresita! Reincercati!")
