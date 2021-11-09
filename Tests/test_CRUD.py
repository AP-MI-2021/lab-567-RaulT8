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
    l = adaugacomanda("1", "Piratii din Caraibe",  45, "Explorare","Gold",l)
    l = adaugacomanda("2", "Alba ca zapada",  25,"Basm", "Silver",l)
    l = modificarecomanda("2", "Alba ca zapada",  10,"Nuvela", "Gold",l)
    assert getID(getbyID("2", l)) == "2"
    assert getID(getbyID("1",l)) =="1"

def test_discount():
    l=[]
    l = adaugacomanda("1", "Piratii din Caraibe",  45,"Explorare", "Gold",l)
    l = adaugacomanda("2", "Alba ca zapada",  25,"Basm", "Silver",l)
    lnew = discount(l)
    assert getpret(getbyID("1",lnew)) == 20.25
    assert getpret(getbyID("2",lnew)) == 23.75


def test_modif_gen():
    l= []
    l = adaugacomanda("1", "Piratii din Caraibe",  45, "Explorare","Gold",l)
    l = adaugacomanda("2", "Alba ca zapada",  25,"Basm", "Silver",l)
    if getbytitlu("Piratii din Caraibe", l):
        gennou = "Basm"
        for comanda in l:
            if gettitlu(comanda) == "Piratii din Caraibe":
                comanda[3] = gennou
    assert gettip(l[0]) =="Basm"


def test_minim_tip():
    l = []
    l = adaugacomanda("1", "Piratii din Caraibe", 45, "Explorare", "Gold", l)
    l = adaugacomanda("2", "Alba ca zapada", 25, "Basm", "Silver", l)
    l = adaugacomanda("2", "Cenusareasa", 10, "Basm", "Silver", l)
    ltip = []
    pret = []
    for comanda in l:
        ok = 1
        for gen in ltip:
            if comanda[3] == gen:
                ok = 0
        if ok == 1:
            ltip.append(comanda[3])

    for gen in ltip:
        minim = 1000
        for comanda in l:
            if gettip(comanda) == gen and int(getpret(comanda)) <= minim:
                minim = getpret(comanda)
        pret.append(minim)

    assert ltip[0] == "Explorare"
    assert ltip[1] =="Basm"
    assert pret[0] ==45
    assert pret[1] == 10

def test_ordcresc():
    l = []
    l = adaugacomanda("1", "Piratii din Caraibe", 45, "Explorare", "Gold", l)
    l = adaugacomanda("2", "Alba ca zapada", 25, "Basm", "Silver", l)
    l = adaugacomanda("3", "Cenusareasa", 10, "Basm", "Silver", l)
    size = len(l)
    for i in range(size):
        min_index = i
        for j in range(i + 1, size):
            if l[min_index][2] > l[j][2]:
                min_index = j
                temp = l[i]
                l[i] = l[min_index]
                l[min_index] = temp

    assert getID(l[0]) == "3"
    assert getID(l[1]) == "2"
    assert getID(l[2]) == "1"

def titluri_dist():
    l = []
    l = adaugacomanda("1", "Piratii din Caraibe", 45, "Explorare", "Gold", l)
    l = adaugacomanda("2", "Alba ca zapada", 25, "Basm", "Silver", l)
    l = adaugacomanda("3", "Cenusareasa", 10, "Basm", "Silver", l)
    newgen1 = []
    contgen = []

    for i in l:
        ok = 1
        for gen in newgen1:
            if i[3] == gen:
                ok = 0
        if ok == 1:
            newgen1.append(i[3])

    for i in newgen1:
        c = 0
        for comanda in l:
            if comanda[3] == i:
                c = c + 1
        contgen.append(c)

    assert contgen[0] == 1
    assert contgen[1] == 2
