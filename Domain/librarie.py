def creeaza_comanda(ID,titlu,pret,tip,reducere):
    '''
        creaza un dictiionar ce reprezinta o comanda
        :param ID: int
        :param titlu:string
        :param pret: float
        :param tip: string
        :param reducere: string
        :return: Un dictionar al unei comenzi
    '''
    return [ID,titlu,pret,tip,reducere]
        #Touple

def getID(comanda):
    '''
    da ID ul unei vanzari
    :param comanda:dictionar care contine o comanda
    :return: ID (int)
    '''
    return comanda[0]

def gettitlu(comanda):
    '''
    da titlul unei carti
    :param comanda: dictionar care contine o comanda
    :return: titlu(str)
    '''
    return comanda[1]

def getpret(comanda):
    '''
        da pretul
        :param comanda:dictionar care contine o comanda
        :return: pret (float)
    '''
    return comanda[2]



def gettip(comanda):
    '''
        da tipul
        :param comanda:dictionar care contine o comanda
        :return: tip (str)
    '''
    return comanda[3]



def getreducere(comanda):
    '''
        da reducerea
        :param comanda:dictionar care contine o comanda
        :return: reducere (str)
    '''
    return comanda[4]

def to_string(comanda):
    return "Id:, Titlu: , Pret: ,Tip:, Reducere:"(
    getID(comanda),
    gettitlu(comanda),
    getpret(comanda),
    gettip(comanda),
    getreducere(comanda)
    )