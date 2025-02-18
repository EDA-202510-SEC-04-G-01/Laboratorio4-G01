def new_list():
    newlist = {
        'elements': [],
        'size': 0
    }
    return newlist
def get_element(my_list, index):
    return my_list["elements"][index]

def is_present(my_list, element, cmp_function):
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1

def size(my_list):
    return my_list["size"]

def first_element(my_list):
    return my_list["elements"][0]

def last_element(my_list):
    return my_list["elements"][size(my_list)]


def add_first(my_list, lmnt):
    my_list["elements"] = [lmnt] + my_list["elements"]
    my_list["size"] += 1
    
def add_last(my_list, lmnt):
    my_list["elements"] = my_list["elements"] + [lmnt]
    my_list["size"] += 1

def remove_last(my_list):
    """ Elimina el último elemento de la lista """
    if my_list["size"]== 0:
        return None
    my_list["elements"]=my_list["elements"][0:my_list["size"]]
    my_list["size"] -= 1
    
    return my_list["size"]

def remove_first(my_list):
    """ Elimina el último elemento de la lista """
    if my_list["size"]== 0:
        return None
    my_list["elements"]=my_list["elements"][1:my_list["size"]]
    my_list["size"] -= 1
    
    return my_list["size"]

def is_empty(my_list):
    return size(my_list)==0