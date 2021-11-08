from Domain.librarie import to_string
from Logic.CRUD import adaugacomanda,modificarecomanda,stergecomanda
from Logic.functionalitate import discount,cresc
from Logic.CRUD import adaugacomanda,stergecomanda,modificarecomanda,getbyID,gettip,getbytip,getID
from Logic.functionalitate import minim_tip,discount,modifcomm,modif_gen
def printmenu():
    print("1. Adaugare comanda: ")
    print("2. Stergere comanda: ")
    print("3. Modifica comanda: ")
    print("4. Fa discount dupa reducerea comenzii: ")
    print("4.1 Modifica gen dupa titlul cartii: ")
    print("4.4 Pretul minim pe fiecare gen: ")
    print("4.5 Ordoneaza crescator dupa pret: ")
    print("4.6 Afisarea numărului de titluri distincte pentru fiecare gen.")
    print("u Undo")
    print("a. Afisarea comenzilor: ")
    print("x. Iesire")

def add_comanda(lista,undoList,redoList):
    try:
        id = input("Dati un id: ")
        if getbyID(id,lista) is not None:
            raise ValueError("Id ul dat exista deja in lista!")
        titlu = input("Titlu: ")
        pret = input("Pret: ")
        gen = input("Genul: ")
        reducere = input("Reducere(Silver/Gold): ")
        if reducere !="Silver" and reducere !="Gold":
            raise ValueError("Reducerea data este incorecta!")
        rezultat = adaugacomanda(id, titlu, gen, pret, reducere, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare {}".format(ve))
        return lista




def sterg_comanda(lista,undoList,redoList):
    try:
        id = input("Dati id ul unei comenzi: ")
        if getbyID(id,lista) is None:
            raise ValueError("Id ul dat nu exista in lista!")
        rezultat= stergecomanda(id,lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare {}".format(ve))

def modif_comanda(lista,undoList,redoList):
    try:
        id = input("Dati ID ul comenzii de modificat: ")
        if getbyID(id,lista) is None:
            raise ValueError("Id ul dat nu exista in lista!")
        titlu = input("Titlu nou: ")
        pret = input("Pret nou: ")
        gen = input("Genul nou: ")
        reducere = input("Reducere noua (Silver/Gold): ")
        rezultat =  modifcomm(id,titlu,gen,pret,reducere,lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare {}".format(ve))



def arata(lista):
    for comanda in lista:
        print(to_string(comanda))

def ord_cresc(lista):
    return cresc(lista)

def aplic_discount(lista,undoList,redoList):
    undoList.append(lista)
    redoList.clear()
    return discount(lista)

def afis_dist(lista):
    newgen1 =[]
    contgen=[]

    for i in lista:
        ok=1
        for gen in newgen1:
            if i[3]==gen:
                ok=0
        if ok ==1:
            newgen1.append(i[3])

    for i in newgen1:
        c=0
        for comanda in lista:
            if comanda[3] == i:
                c=c+1
        contgen.append(c)


    for i in range(len(newgen1)):
        print(newgen1[i]," ",contgen[i])


def menu(lista):
    undoList = []
    redoList = []
    while True:
        printmenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lista = add_comanda(lista,undoList,redoList)
        elif optiune =="2":
            lista = sterg_comanda(lista,undoList,redoList)
        elif optiune =="3":
            lista = modif_comanda(lista,undoList,redoList)
        elif optiune =="4":
            lista = aplic_discount(lista,undoList,redoList)
        elif optiune =="4.1":
            modif_gen(lista)
        elif optiune =="4.4":
            minim_tip(lista)
        elif optiune == "4.5":
            lista = ord_cresc(lista,undoList,redoList)
        elif optiune =="4.6":
            afis_dist(lista)
        elif optiune =="a":
            print(lista)
        elif optiune == "x":
            break
        elif optiune =="u":
            if len(undoList)>0:
                lista = undoList.pop()
                print(lista)
                redoList.append(lista)
            else:
                print("Nu se poate face undo!")
        else:
            print("Optiune incorecta! Reincercati: ")

