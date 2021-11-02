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
    id = input("Dati ID: ")
    titlu = input("Titlu: ")
    pret = input("Pret: ")
    gen = input("Genul: ")
    reducere = input("Reducere(Silver/Gold): ")
    return adaugacomanda(id,titlu,gen,pret,reducere,lista)

def sterg_comanda(lista):
    id = input("Dati id ul unei comenzi: ")
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
    while True:
        printmenu1()
        optiune = input("Introduceti optiunea: ")
        if optiune == "1":
            lista = add_comanda(lista)
        elif optiune =="2":
            print(lista)
        elif optiune =="3":
            lista = sterg_comanda(lista)
        elif optiune =="4":
            break

        else:
            print("Optiune incorecta! Reincercati: ")
