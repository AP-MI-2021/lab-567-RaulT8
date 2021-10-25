from Domain.comanda import gettip,getID,getreducere,getgen,getpret,creeaza_comanda

def adaugacomanda(ID,gen,pret,tip,reducere,lista):
    comanda = adaugacomanda(ID,gen,pret,tip,reducere)
    return lista+[comanda]

def getbyID(ID,lista):
    for comanda in lista:
        if getbyID(comanda) == ID:
            return comanda
    return None

def getbytitlu(titlu,lista):
    for comanda in lista:
        if getbytitlu(comanda) == titlu:
            return comanda
        return None

def getbygen(gen,lista):
    for comanda in lista:
        if getgen(comanda) == gen:
            return comanda
    return None

def getbypret(pret,lista):
    for comanda in lista:
        if getpret(comanda) == pret:
            return comanda
    return None

def getbytip(tip,lista):
    for comanda in lista:
        if getBytip(comanda) == tip:
            return comanda
    return None

def getbyreducere(reducere,lista):
    for comanda in lista:
        if getreducere(comanda) == reducere:
            return comanda
    return None

def stergecomanda(ID,lista):
    return [comanda  for comanda in lista if getID(comanda)!=ID ]

def modificarecomanda(id,gen,pret,tip,reducere,lista):
    lnew = []
    for comanda in lista:
        if getID(comanda) == id:
            comanda_noua = creeaza_comanda(ID,gen,pret,tip,reducere)
            lnew.append(comanda_noua)
        else:
            lnew.append(comanda)
    return lnew


