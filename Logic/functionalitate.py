from Domain.librarie import creeaza_comanda,getgen,gettip,getpret,getreducere,getID,gettitlu
def modificgen(gennou,id,lista):
    lnoua = []
    for comanda in lista:
        if id == getID(lista):
            comanda

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
                get_reducere(comanda)

            )
            lnew.append(comanda_new)
        elif getreducere(comanda) =="gold":
            comanda_new = creeaza_comanda(
                getID(comanda),
                gettitlu(comanda),
                getgen(comanda),
                getpret(comanda) * 0.9,
                gettip(comanda),
                get_reducere(comanda)

            )
            lnew.append(comanda_new)
        else:
            lnew.append(comanda)
        return lnew

    def ord_cresc(lista):
        lnew = sorted(lista,key = lambda i:getpret(i))
        return lnew
