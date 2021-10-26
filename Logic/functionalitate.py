from Domain.librarie import creeaza_comanda,gettip,getpret,getreducere,getID,gettitlu
from Logic.CRUD import getbyID
def modifcomm(id,titlu,pret,gen,reducere,lista):
    lista[int(id)][1] = titlu
    lista[int(id)][2] =pret
    lista[int(id)][3] = gen
    lista[int(id)][4] = reducere


def discount(lista):
    lnew = []
    for comanda in lista:
        if getreducere(comanda) =="silver":
            comanda_new = creeaza_comanda(
                getID(comanda),
                gettitlu(comanda),
                getgen(comanda),
                getpret(comanda) * 0.95,
                gettip(comanda),
                getreducere(comanda)

            )
            lnew.append(comanda_new)
        elif getreducere(comanda) =="gold":
            comanda_new = creeaza_comanda(
                getID(comanda),
                gettitlu(comanda),
                getgen(comanda),
                getpret(comanda) * 0.9,
                gettip(comanda),
                getreducere(comanda)

            )
            lnew.append(comanda_new)
        else:
            lnew.append(comanda)
        return lnew

def cresc(lista):
        lnew = sorted(lista,key = lambda i:getpret(i))
        return lnew
