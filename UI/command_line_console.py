from Domain.librarie import to_string
from Logic.CRUD import adaugacomanda,modificarecomanda,stergecomanda
from Logic.functionalitate import discount,cresc
from Logic.CRUD import adaugacomanda,stergecomanda,modificarecomanda
from Logic.functionalitate import minim_tip,discount,modifcomm,modif_gen
def printmenu1():
    print("1)Add:")
    print("2)Showall: ")
    print("3)Delete: ")
    print("4)Stop: ")

def add_comanda(lista):
    pass

def sterg_comanda(lista):
    id = input("")
    return stergecomanda(id,lista)

def modif_comanda(lista):
    id = input("Dati ID ul comenzii de modificat: ")
    titlu = input("Titlu nou: ")
    pret = input("Pret nou: ")
    gen = input("Genul nou: ")
    reducere = input("Reducere noua (Silver/Gold): ")
    return modifcomm(id,titlu,gen,pret,reducere,lista)

def arata(lista):
    for comanda in lista:
        print(to_string(comanda))

def ord_cresc(lista):
    return cresc(lista)

def aplic_discount(lista):
    return discount(lista)


def command_line_console(lista):
    
    lista = []
    while True:
        printmenu1()
        stringconsole= input()
        stringconsole = stringconsole.split(',')
        if stringconsole[0] == "add":
            id = stringconsole[1]
            titlu = stringconsole[2]
            pret = stringconsole[3]
            tip = stringconsole[4]
            reducere = stringconsole[5]
            lista = adaugacomanda(id,titlu,pret,tip,reducere,lista)
            if stringconsole[6] == "showall":
                print(lista)
        elif stringconsole[0] == "showall":
            print(lista)
        elif stringconsole[0] == "exit":
            return 0
        elif stringconsole[0] == "delete":
            id = stringconsole[1]
            lista = stergecomanda(id, lista)
        else:
            print("Optiune gresita!")
