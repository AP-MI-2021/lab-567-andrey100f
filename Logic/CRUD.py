from Domain.cheltuieli import creare_cheltuiala, get_id, get_numar_apartament, get_data, get_tip


def verificare_id(id, lista):
    """
    Verifica daca un id este deja intr-o lista de cheltuieli
    :param id: o valoare intreaga
    :param lista: o lista de dictionare
    :return: un dictionar in caz afirmativ, reprezentand cheltuiala, "None" in caz contrar
    """
    for cheltuiala in lista:
        if get_id(cheltuiala) == id:
            return cheltuiala
    return None


def verificare_numar_apartament(numar_apartament, lista):
    """
    Verifica daca un apartament este deja intr-o lista de cheltuieli
    :param numar_apartament: o valoare intreaga
    :param lista: o lista de dictionare
    :return: un dictionar in caz afirmativ, reprezentand cheltuiala, "None" in caz contrar
    """
    for cheltuiala in lista:
        if get_numar_apartament(cheltuiala) == numar_apartament:
            return cheltuiala
    return None


def verificare_data(data, lista):
    """
    Verifica daca o data este deja intr-o lista de cheltuieli
    :param data: un sir de caractere
    :param lista: o lista de dictionare
    :return: un dictionar in caz afirmativ, reprezentand cheltuiala, "None" in caz contrar
    """
    for cheltuiala in lista:
        if get_data(cheltuiala) == data:
            return cheltuiala
    return None


def verificare_tip(tip, lista):
    """
    Verifica daca un tip de cheltuiala este deja intr-o lista
    :param tip: un sir de caractere
    :param lista: o lista de dictionare
    :return: un dictionar in caz afirmativ, reprezentand cheltuiala, "None" in caz contrar
    """
    for cheltuiala in lista:
        if get_tip(cheltuiala) == tip:
            return cheltuiala
    return None


def adaugare_cheltuiala(id, numar_apartament, suma, data, tip, lista):
    """
    Adauga o cheltuiala noua intr-o lista de cheltuieli
    :param id: o valoare intreaga
    :param numar_apartament: o valoare intreaga
    :param suma: o valoare intreaga
    :param data: un sir de caractere
    :param tip: un sir de caractere
    :param lista: o lista de dictionare
    :return: o noua lista, ce va contine atat elementele noi, cat si cel nou adaugat
    """
    if verificare_id(id, lista) is not None:
        raise ValueError("Acest id exista deja! Introduceti alt id!")
    cheltuiala = creare_cheltuiala(id, numar_apartament, suma, data, tip)
    return lista + [cheltuiala]


def stergere_cheltuiala(id, lista):
    """
    Sterge o cheltuiala dintr-o lista
    :param id: o valoare intreaga
    :param lista: o lista de dictionare
    :return: o noua lista de dictionare
    """
    if verificare_id(id, lista) is None:
        raise ValueError("Nu exista acest id!")
    lista_noua = []
    for cheltuiala in lista:
        if get_id(cheltuiala) != id:
            lista_noua.append(cheltuiala)
    return lista_noua


def modificare_cheltuiala(id, numar_apartament, suma, data, tip, lista):
    """
    Editeaza o cheltuiala dintr-o lista
    :param id: o valoare intreaga
    :param numar_apartament: o valoare intreaga
    :param suma: o valoare intreaga
    :param data: un sir de caractere
    :param tip: un sir de caractere
    :param lista: o lista de dictionare
    :return: o noua lista de dictionare
    """
    if verificare_id(id, lista) is None:
        raise ValueError("Acest id nu exista!")
    lista_noua = []
    for cheltuiala in lista:
        if get_id(cheltuiala) == id:
            element_nou = creare_cheltuiala(id, numar_apartament, suma, data, tip)
            lista_noua.append(element_nou)
        else:
            lista_noua.append(cheltuiala)
    return lista_noua
