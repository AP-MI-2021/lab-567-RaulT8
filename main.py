from UI.console import menu
from Tests.testAll import runAlltests

def main():
    runAlltests()
    l=[]
    l = adaugacomanda("1", "Piratii din Caraibe", 45,"Explorare","Gold")
    l = adaugacomanda("2", "Alba ca zapada",  25,"Basm", "Silver")
    menu()

main()