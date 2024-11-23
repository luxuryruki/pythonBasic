from data_structures.clist import CList

def test_clist():
    clist = CList()
    clist.add(10)
    clist.add(20)
    clist.add(30)
    clist.add(40)
    clist.add(50)
    clist.add(60)
    print("Initial list:")
    clist.display()

    clist.remove(20)
    print("Modified list:")
    clist.display()

    clist.remove(60)
    clist.add(65)
    print("Modified list:")
    clist.display()
test_clist()
