from Tests.test_CRUD import test_discount,test_sterge,test_adaugacomanda,test_getbyID,test_modif_comanda
from Tests.testDomain import testComanda


def runAlltests() -> object:
    l=[]
    testComanda()
    test_adaugacomanda(l)
    test_sterge()
    test_modif_comanda()
    test_discount()
