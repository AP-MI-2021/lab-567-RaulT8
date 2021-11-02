from Domain.librarie import to_string
from Logic.CRUD import adaugacomanda,modificarecomanda,stergecomanda
from Logic.functionalitate import discount,cresc
from Logic.CRUD import adaugacomanda,stergecomanda,modificarecomanda
from Logic.functionalitate import minim_tip,discount,modifcomm,modif_gen
import re
def printmenu1():
    print("1)Add:")
    print("2)Showall: ")
    print("3)Delete: ")
    print("4)Exit: ")

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

def split_string(string,delimiters):
    pattern = r'|'.join(delimiters)
    return split_string(pattern, string)



def command_line_console(lista):
    lista = []
    printmenu1()
    while True:
        stringconsole= input()
        stringconsole = stringconsole.split(';')
        for comand in stringconsole:
            comand = comand.split(',')
            if comand[0] == "add":
                if len(comand) ==6:
                    id = comand[1]
                    titlu = comand[2]
                    pret = comand[3]
                    tip = comand[4]
                    reducere = comand[5]
                    lista = adaugacomanda(id,titlu,pret,tip,reducere,lista)
            elif comand[0] == "showall":
                print(lista)
            elif comand[0] == "delete":
                id = comand[1]
                lista = stergecomanda(id, lista)
            elif comand[0] == "exit":
                return 0
