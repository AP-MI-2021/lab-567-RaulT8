def creeaza_comanda(ID,titlu,gen,pret,tip,reducere):
    '''
        creaza un dictiionar ce reprezinta o comanda
        :param ID: int
        :param gen: string
        :param pret: float
        :param tipul: string
        :param reducere: string
        :return: Un dictionar al unei comenzi
    '''
    return {
            "ID":ID,
            "titlu":titlu,
            "gen": gen,
            "pret": pret,
            "tip":tip,
            "reducere": reducere
        }

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


def getgen(comanda):
    '''
        da genul cartii comandate
        :param comanda:dictionar care contine o comanda
        :return: gen (str)
    '''
    return comanda[2]



def getpret(comanda):
    '''
        da pretul
        :param comanda:dictionar care contine o comanda
        :return: pret (float)
    '''
    return comanda[3]



def gettip(comanda):
    '''
        da tipul
        :param comanda:dictionar care contine o comanda
        :return: tip (str)
    '''
    return comanda[4]



def getreducere(comanda):
    '''
        da reducerea
        :param comanda:dictionar care contine o comanda
        :return: reducere (str)
    '''
    return comanda[5]