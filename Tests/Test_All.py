from Tests.Test_CRUD import test_adaugare_cheltuiala, test_stergere_cheltuiala, test_modificare_cheltuiala
from Tests.Test_Domain import test_creare_cheltuiala
from Tests.test_functionalitati import test_stergere_cheltuieli_apartament, test_adunare_valoare_cheltuieli, \
    test_cele_mai_mari_cheltuieli, test_ordonare_dupa_suma


def run_all_tests():
    test_creare_cheltuiala()
    test_adaugare_cheltuiala()
    test_stergere_cheltuiala()
    test_modificare_cheltuiala()
    test_stergere_cheltuieli_apartament()
    test_adunare_valoare_cheltuieli()
    test_cele_mai_mari_cheltuieli()
    test_ordonare_dupa_suma()
