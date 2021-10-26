from Domain.librarie import creeaza_comanda,getpret,getID,gettitlu,getreducere,to_string,gettip
def testComanda():
    comanda  =creeaza_comanda("1","Piratii din Caraibe",45,"Explorare","Gold")
    assert getID(comanda) =="1"
    assert gettitlu(comanda) == "Piratii din Caraibe"
    assert getpret(comanda) ==45
    assert gettip(comanda) == "Explorare"
    assert getreducere(comanda) =="Gold"
