from UI.command_line_console import command_line_console
from Tests.testAll import runAlltests
from Logic.CRUD import adaugacomanda

def main():
    runAlltests()
    l=[]
    l = adaugacomanda("1", "Piratii din Caraibe", 45, "Explorare", "Gold",l)
    l = adaugacomanda("2", "Alba ca zapada", 25, "Basm", "Silver",l)
    l = adaugacomanda("3","Cenusareasa",10,"Basm","Gold",l)
    print("1)Interfata clasica:")

    optiune =input("Dati codul de interfata pe care doriti sa o accesati: ")
    command_line_console(l)

main()