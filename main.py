from UI.console import menu
from Tests.testAll import runAlltests
from Logic.CRUD import adaugacomanda

def main():
    runAlltests()
    l=[]
    l = adaugacomanda("1", "Piratii din Caraibe", 45,"Explorare","Gold",l)
    l = adaugacomanda("2", "Alba ca zapada",  25,"Basm", "Silver",l)
    menu(l)

main()