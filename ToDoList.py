_list = []
_listDel = []

def add(obj):
    _list.append(obj)

def show():
    print("The list contains:")
    for val in _list:
        print(val)

def remove(index):
    try:
        obj = _list[index]
        _list.pop(index)
        _listDel.append(obj)
        print(f"{obj} has been successfully removed!")
    except Exception:
        print('There is no such object')

def removedObj():
    print("Deleted objects:")
    for val in _listDel:
        print(val)

def control(opt):
    if opt == 1:
        obj = input("Enter element: ")
        add(obj)

    if opt == 2:
        show()

    if opt == 3:
        print(_list)
        obj = int(input("Type the objects' id to be deleted"))
        remove(obj)
    if opt == 4:
        print(f"List containing done tasks: {_listDel}")

    if opt == 5:
        ex



print("To DO List")

while(1):
    try:
        option = int(input("1.Add 2.List 3.Consider Done 4.Done list 5.Exit \nSelect option: "))
        control(option)

    except ValueError:
        print("Oops! This is not a number! Try again.")




