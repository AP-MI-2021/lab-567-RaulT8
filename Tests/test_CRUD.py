from Domain.librarie import getreducere,getgen,gettip,getpret,getID,gettitlu
from Logic.CRUD import adaugacomanda,getbyID,getbygen,getbytitlu,getbypret,getbyreducere,getbytip,stergecomanda,modificarecomanda

def test_adaugacomanda():
    l=[]
    l=adaugacomanda("1","Pirati din Caraibe","Explorare",45,"Gold",lista)
    assert getID(getbyID("1",l)) =="1"
    assert gettitlu(getbyID("1",l)) == "Piratii din Caraibe"
    assert getgen(getbyID("1",l)) == "Explorare"
    assert getpret(getbyID("1",l)) == 45
    assert getreducere(getbyID("1",l)) == "Gold"

def test_sterge():
    l=[]
    l=adaugacomanda("1","Piratii din Caraibe","Explorare",45,"Gold")
    l=adaugacomanda("2","Alba ca zapada","Basm",25,"Silver")
    l=adaugacomanda("3","Cenusareasa","Basm",30,None)
    lista = stergecomanda("2",lista)
    assert getbyID("1",lista) is not None
    assert getbyID("2",lista) is None
    assert getbyID("3",lista) is not None

def test_modif_comanda():
    l=[]
    l = adaugacomanda("1","Piratii din Caraibe","Explorare",45,"Gold")
    l = adaugacomanda("2", "Alba ca zapada", "Basm", 25, "Silver")
    l = modificarecomanda("2","Alba ca zapada","Nuvela",10,"Gold")
    assert getID(getbyID("2", l)) == "2"
    assert gettitlu(getbyID("2", l)) == "Alba ca zapada"
    assert getgen(getbyID("2", l)) == "Nuvela"
    assert getpret(getbyID("2", l)) == 10
    assert getreducere(getbyID("2", l)) == "Gold"