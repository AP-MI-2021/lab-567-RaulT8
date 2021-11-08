from Domain.librarie import gettip,getID,getreducere,getpret,creeaza_comanda,gettitlu

def adaugacomanda(ID,titlu,pret,tip,reducere,lista):
        comanda = creeaza_comanda(ID,titlu,pret,tip,reducere)
        return lista+[comanda]

def getbyID(id,lista):
    for comanda in lista:
        if getID(comanda) == id:
            return comanda
    return None

def getbytitlu(titlu,lista):
    for k in lista:
        if gettitlu(k) == titlu:
            return k
    return None

def getbypret(pret,lista):
    for k in lista:
        if getpret(k) == pret:
            return k
    return None

def getbytip(tip,lista):
    for comanda in lista:
        if gettip(comanda) == tip:
            return comanda
    return None

def getbyreducere(reducere,lista):
    for k in lista:
        if getreducere(k) == reducere:
            return k
    return None

def stergecomanda(id,lista):
    if getbyID(id, lista) is None:
        print("Id ul dat este incorect!")
    return [comanda for comanda in lista if getID(comanda) != id]


def modificarecomanda(id,gen,pret,tip,reducere,lista):
    lnew = []
    for comanda in lista:
        if getID(comanda) == id:
            comanda_noua = creeaza_comanda(id,gen,pret,tip,reducere)
            lnew.append(comanda_noua)
        else:
            lnew.append(comanda)
    return lnew