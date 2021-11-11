from UI.command_line_console import command_line_console
from UI.console import menu
from Tests.testAll import runAlltests
from Logic.CRUD import adaugacomanda

def main():
    runAlltests()
    undoList =[]
    redoList =[]
    l=[]
    l = adaugacomanda("1", "Piratii din Caraibe", 45, "Explorare", "Gold",l)
    l = adaugacomanda("2", "Alba ca zapada", 25, "Basm", "Silver",l)
    l = adaugacomanda("3","Cenusareasa",10,"Basm","Gold",l)
    print("1)Old menu:")
    print("2)New menu:")
    optiune = input("Dati codul corespunzator pentru meniul dorit: ")
    if optiune =="1":
        menu(l)
    elif optiune =="2":
        command_line_console()
    else:
        print("Optiune incorecta!")

main()