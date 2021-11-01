def creare_cheltuiala(id, numar_apartament, suma, data, tip):
    """
    Creaza un dictionar ce reprezinta o cheltuiala
    :param id: o valoare intreaga
    :param numar_apartament: o valoare intreaga
    :param suma: o valoare intreaga
    :param data: un sir de caractere
    :param tip: un sir de caractere
    :return: un dictionar ce reprezinta o cheltuiala
    """
    return {
        "id": id,
        "numar_apartament": numar_apartament,
        "suma": suma,
        "data": data,
        "tip": tip
    }


def get_id(cheltuiala):
    """
    Getter pentru id-ul unei cheltuieli
    :param cheltuiala: un dictionar
    :return: o valoare intreaga
    """
    return cheltuiala["id"]


def get_numar_apartament(cheltuiala):
    """
    Getter pentru numarul de apartament al unei cheltuieli
    :param cheltuiala: un dictionar
    :return: o valoare intreaga
    """
    return cheltuiala['numar_apartament']


def get_suma(cheltuiala):
    """
    Getter pentru suma unei cheltuieli
    :param cheltuiala: un dictionar
    :return: o valoare intreaga
    """
    return cheltuiala["suma"]


def get_data(cheltuiala):
    """
    Getter pentru data unei cheltuieli
    :param cheltuiala: un dictionar
    :return: un sir de caractere
    """
    return cheltuiala["data"]


def get_tip(cheltuiala):
    """
    Getter pentru tipul unei cheltuieli
    :param cheltuiala: un dictionar
    :return: un sir de caractere
    """
    return cheltuiala["tip"]


def get_to_string(cheltuiala):
    """
    Converteste dictionarul "cheltuiala" intr-un sir de caractere
    :param cheltuiala: un dictionar
    :return: un sir de caractere
    """
    return "ID: {}, Numar apartament: {}, Suma: {}, Data: {}, Tip: {}".format(
        get_id(cheltuiala),
        get_numar_apartament(cheltuiala),
        get_suma(cheltuiala),
        get_data(cheltuiala),
        get_tip(cheltuiala)
    )
