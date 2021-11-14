from UI.console import undo,redo
from Logic.CRUD import adaugacomanda,stergecomanda,modificarecomanda,getbyID,gettip,getbytip,getID,gettitlu,getreducere,getpret,getbytitlu,getbypret,getbyreducere
from UI.console import add_comanda,sterg_comanda,modif_comanda
from Logic.functionalitate import minim_tip,discount,modifcomm,modif_gen
from Domain.librarie import gettip,getID,gettitlu,getreducere,getpret,to_string
def test_undored():
    l=[]
    undoList =[]
    redoList =[]

    obiect = ["1", "Piratii din Caraibe", 45, "Explorare", "Gold"]
    l = add_comanda(l,undoList,redoList,obiect)

    obiect = ["2", "Cenusareasa", 20, "Basm", "Gold"]
    l = add_comanda(l, undoList, redoList, obiect)

    obiect = ["3", "Alba ca Zapada", 45, "Nucela", "Silver"]
    l = add_comanda(l, undoList, redoList, obiect)

    assert len(l) ==3

    l = undo(l,undoList,redoList)

    assert len(l) ==2
    assert getbyID('1',l) is not None
    assert getbyID('2', l) is not None
    assert getbyID("3", l) is None

    l = undo(l,undoList,redoList)

    assert len(l) ==1
    assert getbyID("1", l) is not None
    assert getbyID("2", l) is None
    assert getbyID("3", l) is None

    l = undo(l, undoList, redoList)

    assert len(l) == 0
    assert getbyID("1", l) is None
    assert getbyID("2", l) is None
    assert getbyID("3", l) is None

    l=[]
    undoList = []
    redoList = []
    obiect = ["1", "Piratii din Caraibe", 45, "Explorare", "Gold"]
    l = add_comanda(l,undoList,redoList,obiect)
    obiect = ["2", "Cenusareasa", 20, "Basm", "Gold"]
    l = add_comanda(l, undoList, redoList, obiect)
    obiect = ["3", "Alba ca Zapada", 45, "Nucela", "Silver"]
    l = add_comanda(l, undoList, redoList, obiect)
    assert len(l) == 3

    assert getbyID('1', l) is not None
    assert getbyID("2", l) is not None
    assert getbyID("3", l) is not None

    l = undo(l, undoList, redoList)
    l = undo(l, undoList, redoList)

    assert len(l) == 1
    assert getbyID("1", l) is not None
    assert getbyID("2", l) is None
    assert getbyID("3", l) is None

    l = redo(l, undoList, redoList)

    assert len(l) == 2
    assert getbyID("1", l) is not None
    assert getbyID("2", l) is not None
    assert getbyID("3", l) is None

    l = redo(l, undoList, redoList)

    assert len(l) == 3
    assert getbyID("1", l) is not None
    assert getbyID("2", l) is not None
    assert getbyID("3", l) is not None

    l = undo(l, undoList, redoList)
    l = undo(l, undoList, redoList)

    assert len(l) == 1
    assert getbyID("1", l) is not None
    assert getbyID("2", l) is None
    assert getbyID("3", l) is None

    obiect = ["4", "Alba ca Zapada", 45, "Nucela", "Silver"]
    l=add_comanda(l,undoList,redoList,obiect)

    assert len(l) ==2
    assert getbyID("1", l) is not None
    assert getbyID("2", l) is None
    assert getbyID("3", l) is None
    assert getbyID("4",l) is not None

    if len(redoList)>0:
        l = redo(l, undoList, redoList)
        assert len(l) == 3
        assert getbyID("1", l) is not None
        assert getbyID("2", l) is None
        assert getbyID("3", l) is None
        assert getbyID("4", l) is not None

    l = undo(l, undoList, redoList)

    assert len(l) == 1
    assert getbyID("1", l) is not None
    assert getbyID("2", l) is None
    assert getbyID("3", l) is None
    assert getbyID("4", l) is None

    l = undo(l, undoList, redoList)

    assert len(l) == 0

    l = redo(l, undoList, redoList)
    l = redo(l, undoList, redoList)

    assert len(l) == 2
    assert getbyID("1", l) is not None
    assert getbyID("2", l) is None
    assert getbyID("3", l) is None
    assert getbyID("4", l) is not None

    if len(redoList)>0:
        l = redo(l, undoList, redoList)
        assert len(l) == 2
        assert getbyID("1", l) is not None
        assert getbyID("2", l) is None
        assert getbyID("3", l) is None
        assert getbyID("4", l) is not None

    l =[]
    obiect = ["1", "Piratii din Caraibe", 45, "Explorare", "Gold"]
    l = add_comanda(l, undoList, redoList, obiect)
    obiect = ["2", "Cenusareasa", 20, "Basm", "Gold"]
    l = add_comanda(l, undoList, redoList, obiect)
    obiect = ["3", "Alba ca Zapada", 45, "Nucela", "Silver"]
    l = add_comanda(l, undoList, redoList, obiect)

    obiect = ['2']
    l = sterg_comanda(l,undoList,redoList,obiect)

    assert len(l) ==2
    assert getbyID("1", l) is not None
    assert getbyID("2", l) is None
    assert getbyID("3", l) is not None

    l = undo(l, undoList, redoList)

    assert len(l) == 3
    assert getbyID("1", l) is not None
    assert getbyID("2", l) is not None
    assert getbyID("3", l) is not None

    l = redo(l,undoList,redoList)

    assert len(l) == 2
    assert getbyID("1", l) is not None
    assert getbyID("2", l) is None
    assert getbyID("3", l) is not None

    l=[]
    obiect = ["1", "Piratii din Caraibe", 45, "Explorare", "Gold"]
    l = add_comanda(l, undoList, redoList, obiect)
    obiect = ["2", "Cenusareasa", 20, "Basm", "Gold"]
    l = add_comanda(l, undoList, redoList, obiect)
    obiect = ["3", "Alba ca Zapada", 45, "Nuvela", "Silver"]
    l = add_comanda(l, undoList, redoList, obiect)

    obiect =['1','Piticii',35,'Basm','Silver']
    l=modif_comanda(l,undoList,redoList,obiect)

    for i in l:
        if getID(i)  ==1:
            assert gettitlu(i) =='Piticii'
            assert getpret(i) ==35
            assert gettip(i) == 'Basm'
            assert getreducere(i) == 'Silver'












