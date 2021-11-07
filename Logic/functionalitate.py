from Domain.librarie import creeaza_comanda,gettip,getpret,getreducere,getID,gettitlu
from Logic.CRUD import getbyID,getbytitlu,getbypret,getbyreducere,getbytip
def modifcomm(id,titlu,pret,gen,reducere,lista):
    '''
    :param id:
    :param titlu:
    :param pret:
    :param gen:
    :param reducere:
    :param lista:
    :return: modificarea obiectului din lista
    '''
    try:
        lnew =[]
        if getbyID(id,lista) is not None:
            for comanda in lista:
                if getID(comanda) == id:
                    comandanoua = creeaza_comanda(id,titlu,pret,gen,reducere)
                    lnew.append(comandanoua)
                else:
                    lnew.append(comanda)
        return lnew
    except ValueError as ve:
        print("Eroare {}".format(ve))

def modif_gen(lista):
    '''
    :param lista:
    :return:lista noua cu obiectul modificat in functie de titlul dat
    '''
    try:
        titlul = input("Dati un titlu:")
        if getbytitlu(titlul,lista) is None:
            raise ValueError("Titlul dat nu exista in lista!")
        else:
            gennou = input("Dati noul gen: ")
            for comanda in lista:
                if gettitlu(comanda) == titlul:
                    comanda[3] = gennou
    except ValueError as ve:
        print("Eroare {}".format(ve))




def discount(lista):
    '''
    :param lista:
    :return: Lista noua in care se va aplica la preturile tuturor obiectelor discount ul corespunzator
    '''
    lnew = []
    for i in lista:
        if getreducere(i) =="Silver":
            comanda_new = creeaza_comanda(
                getID(i),
                gettitlu(i),
                int(getpret(i))*19/20,
                gettip(i),
                getreducere(i)

            )
            lnew.append(comanda_new)
        elif getreducere(i) =="Gold":
            comanda_new = creeaza_comanda(
                getID(i),
                gettitlu(i),
                int(getpret(i))*9/20,
                gettip(i),
                getreducere(i)

            )
            lnew.append(comanda_new)
        else:
            lnew.append(i)
    lista = []
    for comanda in lnew:
        lista.append(comanda)
    return lista


def cresc(lista):
    '''
    :param lista:
    :return: Lista initiala ordonata crescator in fucntie de pretul fiecarei comenzi
    '''
    size = len(lista)
    for i in range(size):
        min_index = i
        for j in range(i+1,size):
            if lista[min_index][2] > lista[j][2]:
                min_index = j
                temp = lista[i]
                lista[i] = lista[min_index]
                lista[min_index] = temp

def minim_tip(lista):
    '''
    Determinam pretul minim pe fiecare categorie
    :param lista: lista comenzilor
    :return: pretul minim pentru fiecare functie
    '''
    ltip =[]
    pret = []
    for comanda in lista:
        ok=1
        for gen in ltip:
            if comanda[3]==gen:
                ok=0
        if ok ==1:
            ltip.append(comanda[3])

    for gen in ltip:
        minim=1000
        for comanda in lista:
            if gettip(comanda) == gen and getpret(comanda)<=minim:
                minim=getpret(comanda)
        pret.append(minim)

    for i in range(len(pret)):
        print(ltip[i]," ",pret[i])
