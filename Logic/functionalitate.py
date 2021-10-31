from Domain.librarie import creeaza_comanda,gettip,getpret,getreducere,getID,gettitlu
from Logic.CRUD import getbyID,getbytitlu,getbypret,getbyreducere,getbytip
def modifcomm(id,titlu,pret,gen,reducere,lista):
    if getbyID(id,lista) is None:
        raise ValueError("Id-ul dat este incorect! ")
    lnew = []
    for comanda in lista:
        if getID(comanda) == id:
            comandanoua = creeaza_comanda(id,titlu,pret,gen,reducere)
            lnew.append(comandanoua)
        else:
            lnew.append(comanda)
    return lnew

def modif_gen(lista):
    titlul = input("Dati un titlu:")
    ok=1
    for comanda in lista:
        if getbytitlu(titlul,lista):
            comanda[1] = input("Introduceti noul titlu: ")



def discount(lista):
    lnew = []
    for comanda in lista:
        if getreducere(comanda) =="Silver":
            comanda_new = creeaza_comanda(
                getID(comanda),
                gettitlu(comanda),
                getpret(comanda) - 1 / 20 * getpret(comanda),
                gettip(comanda),
                getreducere(comanda)

            )
            lnew.append(comanda_new)
        elif getreducere(comanda) =="Gold":
            comanda_new = creeaza_comanda(
                getID(comanda),
                gettitlu(comanda),
                getpret(comanda) - 1 / 10 * getpret(comanda),
                gettip(comanda),
                getreducere(comanda)

            )
            lnew.append(comanda_new)
        else:
            lnew.append(comanda)
    lista = []
    for comanda in lnew:
        lista.append(comanda)
    return lista


def cresc(lista):
    lnew = sorted(lista,key = lambda comanda:getpret(comanda))
    return lnew

def minim_tip(lista):
    '''
    Determinam pretul minim pe fiecare categorie
    :param lista: lista comenzilor
    :return: pretul minim pentru fiecare functie
    '''
    lnew ={}
    for comanda in lista:
        tip = gettip(comanda)
        pret = getpret(comanda)
        if tip in lnew:
            if pret<lnew[tip]:
                lnew[tip] = pret
            else:
                lnew[tip]
    return lnew