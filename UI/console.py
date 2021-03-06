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
    print("r Redo")
    print("a. Afisarea comenzilor: ")
    print("x. Iesire")

def add_comanda(lista,undoList,redoList,obiect):
    try:
        if len(obiect) ==0:
            id = input("Dati un id: ")
            if getbyID(id,lista) is not None:
                raise ValueError("Id ul dat exista deja in lista!")
            titlu = input("Titlu: ")
            pret = float(input("Pret: "))
            gen = input("Genul: ")
            reducere = input("Reducere(Silver/Gold): ")
            if reducere !="Silver" and reducere !="Gold":
                raise ValueError("Reducerea data este incorecta!")
        else:
            id = obiect[0]
            titlu = obiect[1]
            pret = float(obiect[2])
            gen = obiect[3]
            reducere = obiect[4]
        cop_list = lista.copy()
        rezultat = adaugacomanda(id, titlu, pret, gen, reducere, lista)
        main_undo(undoList,redoList,cop_list)
        return rezultat
    except ValueError as ve:
        print("Eroare {}".format(ve))
        return lista




def sterg_comanda(lista,undoList,redoList,obiect):
    try:
        if len(obiect) ==0:
            id = input("Dati id ul unei comenzi: ")
        else:
            id = obiect[0]
        if getbyID(id,lista) is None:
            raise ValueError("Id ul dat nu exista in lista!")
        cop_list = lista.copy()
        rezultat= stergecomanda(id,lista)
        main_undo(undoList, redoList, cop_list)
        return rezultat
    except ValueError as ve:
        print("Eroare {}".format(ve))

def modif_comanda(lista,undoList,redoList,obiect):
    try:
        if len(obiect) ==0:
            id = input("Dati ID ul comenzii de modificat: ")
            if getbyID(id,lista) is None:
                raise ValueError("Id ul dat nu exista in lista!")
            titlu = input("Titlu nou: ")
            pret = float(input("Pret nou: "))
            gen = input("Genul nou: ")
            reducere = input("Reducere noua (Silver/Gold): ")
        else:
            id = obiect[0]
            titlu = obiect[1]
            pret = obiect[2]
            gen = obiect[3]
            reducere = obiect[4]
        cop_list = lista.copy()
        rezultat =  modifcomm(id,titlu,pret,gen,reducere,lista)
        main_undo(undoList, redoList, cop_list)
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

def modific_gen(lista):
    rezultat = modif_gen(lista)
    return rezultat

def undo(lista,undoList,redoList):
    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()
        return lista
    else:
        print("Nu se poate face undo!")

def redo(lista,undoList,redoList):
    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
        return lista
    else:
        print("Nu se poate face redo!")

def undo1(lista,undoList,redoList):
    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()
        print(lista)
    else:
        print("Nu se poate face undo!")

def redo1(lista,undoList,redoList):
    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
        print(lista)
    else:
        print("Nu se poate face redo!")

def main_undo(undoList,redoList,cop_list):
    undoList.append(cop_list)
    redoList.clear()

def menu(lista):
    undoList = []
    redoList = []
    obiect =[]

    while True:
        printmenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lista = add_comanda(lista,undoList,redoList,obiect)
        elif optiune =="2":
            lista = sterg_comanda(lista,undoList,redoList,obiect)
        elif optiune =="3":
            lista = modif_comanda(lista,undoList,redoList,obiect)
        elif optiune =="4":
            lista = aplic_discount(lista,undoList,redoList)
        elif optiune =="4.1":
            lista= modific_gen(lista)
        elif optiune =="4.4":
            minim_tip(lista)
        elif optiune == "4.5":
            lista = ord_cresc(lista)
        elif optiune =="4.6":
            afis_dist(lista)
        elif optiune =="a":
            print(lista)
        elif optiune =="u":
            undo1(lista,undoList,redoList)
        elif optiune =="r":
            redo1(lista,undoList,redoList)
        elif optiune == "x":
            break
        else:
            print("Optiune incorecta! Reincercati: ")