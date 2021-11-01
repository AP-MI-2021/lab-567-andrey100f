from Domain.cheltuieli import get_numar_apartament, get_id, get_data, get_suma, get_tip, creare_cheltuiala
from Logic.CRUD import verificare_numar_apartament, verificare_data, verificare_tip


def stergere_cheltuieli_apartament(numar_apartament, lista):
    """
    Sterge toate cheltuielile unui apartament dintr-o lista
    :param numar_apartament: o valoare intreaga
    :param lista: o lista de dictionare
    :return: o lista de dictionare
    """
    if verificare_numar_apartament(numar_apartament, lista) is None:
        raise ValueError("Acest apartament nu exista!")
    lista_noua = []
    for cheltuiala in lista:
        if get_numar_apartament(cheltuiala) != numar_apartament:
            lista_noua.append(cheltuiala)
    return lista_noua


def adunare_valoare_cheltuieli(data, lista, valoare):
    """
    Aduna o valoare la toate cheltuielile dintr-o anumita data
    :param data: un sir de caractere
    :param lista: o lista de dictionare
    :param valoare: o valoare intreaga
    :return: o noua lista ce contine noile cheltuieli
    """
    if verificare_data(data, lista) is None:
        raise ValueError("Aceasta data nu exista!")
    lista_noua = []
    for cheltuiala in lista:
        if get_data(cheltuiala) == data:
            id_nou = get_id(cheltuiala)
            numar_apartament_nou = get_numar_apartament(cheltuiala)
            suma_noua = get_suma(cheltuiala) + valoare
            tip_nou = get_tip(cheltuiala)
            element_nou = creare_cheltuiala(id_nou, numar_apartament_nou, suma_noua, data, tip_nou)
            lista_noua.append(element_nou)
        else:
            lista_noua.append(cheltuiala)
    return lista_noua


def cea_mai_mare_cheltuiala_intretinere(lista):
    """
    Determina cea mai mare cheltuiala de tipul "intretinere"
    :param lista: o lista de dictionare
    :return: un dictionar, ce reprezinta cheltuiala cea mai mare de tipul "intretinere
    """
    maxim_intretinere = {}
    if verificare_tip("intretinere", lista) is None:
        return maxim_intretinere
    maxim_suma = 0
    for cheltuiala in lista:
        if get_tip(cheltuiala) == "intretinere" and get_suma(cheltuiala) > maxim_suma:
            maxim_suma = get_suma(cheltuiala)
            maxim_intretinere = cheltuiala
    return maxim_intretinere


def cea_mai_mare_cheltuiala_canal(lista):
    """
    Determina cea mai mare cheltuiala de tipul "canal"
    :param lista: o lista de dictionare
    :return: un dictionar, ce reprezinta cheltuiala cea mai mare de tipul "canal"
    """
    maxim_canal = {}
    if verificare_tip("canal", lista) is None:
        return maxim_canal
    maxim_suma = 0
    for cheltuiala in lista:
        if get_tip(cheltuiala) == "canal" and get_suma(cheltuiala) > maxim_suma:
            maxim_suma = get_suma(cheltuiala)
            maxim_canal = cheltuiala
    return maxim_canal


def cea_mai_nare_cheltuiala_altele(lista):
    """
    Determina cea mai mare cheltuiala de tipul "alte cheltuieli"
    :param lista: o lista de dictionare
    :return: un dictionar, ce reprezinta cheltuiala cea mai mare de tipul "alte cheltuieli"
    """
    maxim_altele = {}
    if verificare_tip("alte cheltuieli", lista) is None:
        return maxim_altele
    maxim_suma = 0
    for cheltuiala in lista:
        if get_tip(cheltuiala) == "alte cheltuieli" and get_suma(cheltuiala) > maxim_suma:
            maxim_suma = get_suma(cheltuiala)
            maxim_altele = cheltuiala
    return maxim_altele


def cele_mai_mari_cheltuieli(lista):
    """
    Determina cele mai mari cheltuieli de fiecare tip dintr-o lista
    :param lista: o lista de dictionare
    :return: o noua lista de dictionare, ce contine valorile maxime
    """
    lista_maxime = []
    maxim_intretinere = cea_mai_mare_cheltuiala_intretinere(lista)
    maxim_canal = cea_mai_mare_cheltuiala_canal(lista)
    maxim_altele = cea_mai_nare_cheltuiala_altele(lista)
    lista_maxime.append(maxim_intretinere)
    lista_maxime.append(maxim_canal)
    lista_maxime.append(maxim_altele)
    return lista_maxime


def ordonare_dupa_suma(lista):
    """
    Ordoneaza o lista de cheltuieli descrescator dupa valoarea sumei
    :param lista: o lista de dictionare
    :return: lista de dictionare ordonata conform cerintei
    """
    return sorted(lista, key=lambda cheltuiala: get_suma(cheltuiala), reverse=True)
