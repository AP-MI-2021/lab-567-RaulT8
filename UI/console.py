from Domain.librarie import to_string
from Logic.CRUD import adaugacomanda,modificarecomanda,stergecomanda
from Logic.functionalitate import discount,modificgen,cresc

def printmenu():
    print("1. Adaugare comanda: ")
    print("2. Stergere comanda: ")
    print("3. Modifica comanda: ")
    print("4. Fa discount dupa reducerea comenzii: ")
    print("5. Ordoneaza crescator dupa pret: ")
    print("a. Afisare comenzi: ")
    print("x. Iesire")

def add_comanda(lista):
    id = input("Dati ID: ")
    titlu = input("Titlu: ")
    gen = input("Genul: ")
    pret = input("Pret: ")
    reducere = input("Reducere(Silver/Gold): ")
    return adaugacomanda(id,titlu,gen,pret,reducere,lista)

def sterg_comanda(lista):
    id = input("Dati id ul unei comenzi: ")
    return stergecomanda(id,lista)

def modif_comanda(lista):
    id = input("Dati noul ID: ")
    titlu = input("Titlu nou: ")
    gen = input("Genul nou: ")
    pret = input("Pret nou: ")
    reducere = input("Reducere noua (Silver/Gold): ")
    return modificgen(id,titlu,gen,pret,reducere,lista)

def arata(lista):
    for comanda in lista:
        print(to_string(comanda))

def ord_cresc(lista):
    return cresc(lista)

def aplic_discount(lista):
    return discount(lista)

def menu(lista):
    while True:
        printmenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lista = add_comanda(lista)
        elif optiune =="2":
            lista = stergecomanda(lista)
        elif optiune =="3":
            lista = modif_comanda(lista)
        elif optiune =="4":
            lista = aplic_discount(lista)
        elif optiune ="afisare":
            arata(lista)
        elif optiune ="x":
            break
        else:
            print("Optiune incorecta! Reincercati: ")
