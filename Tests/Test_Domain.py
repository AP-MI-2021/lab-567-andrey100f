from Domain.cheltuieli import creare_cheltuiala, get_id, get_numar_apartament, get_suma, get_tip, get_data


def test_creare_cheltuiala():
    cheltuiala = creare_cheltuiala(1010, 5, 100, "19.10.2021", "intretinere")
    assert get_id(cheltuiala) == 1010
    assert get_numar_apartament(cheltuiala) == 5
    assert get_suma(cheltuiala) == 100
    assert get_data(cheltuiala) == "19.10.2021"
    assert get_tip(cheltuiala) == "intretinere"
