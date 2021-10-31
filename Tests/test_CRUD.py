from Domain.librarie import getreducere,getpret,getID,gettitlu,gettip
from Logic.CRUD import adaugacomanda,getbyID,getbytitlu,getbypret,getbyreducere,getbytip,stergecomanda,modificarecomanda
from Logic.functionalitate import discount

def test_adaugacomanda(l):
    l=[]
    l=adaugacomanda("1","Pirati din Caraibe",45,"Explorare","Gold",l)
    assert getID(getbyID("1",l)) =="1"
    assert gettitlu(getbyID("1",l)) == "Pirati din Caraibe"
    assert getpret(getbyID("1",l)) ==45
    assert gettip(getbyID("1",l)) =="Explorare"
    assert getreducere(getbyID("1",l)) == "Gold"

def test_sterge():
    l=[]
    l=adaugacomanda("1","Piratii din Caraibe",45,"Explorare","Gold",l)
    l=adaugacomanda("2","Alba ca zapada",25,"Basm","Silver",l)
    l=adaugacomanda("3","Cenusareasa",30,"Nuvela","Gold",l)
    lista = stergecomanda("2",l)
    assert getbyID("1",lista) is not None
    assert getbyID("2",lista) is None
    assert getbyID("3",lista) is not None



def test_modif_comanda():
    l=[]
    l = adaugacomanda("1","Piratii din Caraibe",45,"Explorare","Gold",l)
    l = adaugacomanda("2", "Alba ca zapada", 25, "Basm", "Silver",l)
    l = modificarecomanda("2","Ana",10,"Nuvela","Gold",l)
    assert getID(getbyID("2", l)) == "2"
    assert gettitlu(getbyID("2", l)) == "Ana"
    assert getpret(getbyID("2", l)) == 10
    assert getreducere(getbyID("2", l)) == "Gold"
    assert gettip(getbyID("2",l)) == "Nuvela"

def test_getbyID():
    l= []
    l = adaugacomanda("1", "Piratii din Caraibe",  45, "Explorare","Gold")
    l = adaugacomanda("2", "Alba ca zapada",  25,"Basm", "Silver")
    l = modificarecomanda("2", "Alba ca zapada",  10,"Nuvela", "Gold")
    assert getID(getbyID("2", l)) == "2"
    assert getID(getbyID("1")) =="1"

def test_discount():
    l=[]
    l = adaugacomanda("1", "Piratii din Caraibe",  45,"Explorare", "Gold",l)
    l = adaugacomanda("2", "Alba ca zapada",  25,"Basm", "Silver",l)
    lnew = discount(l)
    assert getpret(getbyID("1",l)) == 40.5
    assert getpret(getbyID("2",l)) == 23.75


def test_modif_gen():
    l= []
    l = adaugacomanda("1", "Piratii din Caraibe",  45, "Explorare","Gold")
    l = adaugacomanda("2", "Alba ca zapada",  25,"Basm", "Silver")
    l = modificarecomanda("2", "Alba ca zapada",  10,"Nuvela", "Gold")
