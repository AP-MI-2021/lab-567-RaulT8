from Tests.test_CRUD import test_sterge,test_adaugacomanda,test_getbyID,test_modif_comanda,test_modif_gen,test_discount,test_minim_tip,test_ordcresc,titluri_dist
from Tests.testDomain import testComanda


def runAlltests() -> object:
    l=[]
    test_adaugacomanda(l)
    test_sterge()
    test_modif_comanda()
    test_discount()
    test_modif_gen()
    test_getbyID()
    testComanda()
    test_minim_tip()
    test_ordcresc()
    titluri_dist()

    #test_discount()
