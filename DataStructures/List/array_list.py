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

def insert_element(my_list, lmnt, pos):
    my_list["elements"].insert(pos, lmnt)
    my_list["size"] += 1
    return my_list

def delete_element(my_list, pos):
    if not( 0 <= pos  and pos< size(my_list)):
        raise IndexError('list index out of range')
    else:
        my_list["elements"].pop(pos)
        my_list["size"] -= 1
        return my_list

def change_info(my_list, pos, new_info):
    if not( 0 <= pos  and pos< size(my_list)):
        raise IndexError('list index out of range')
    else:
        my_list["elements"][pos] = new_info
        return my_list
    
def exchange(my_list, pos_1, pos_2):
    if not((0 <= pos_1  and pos_1< size(my_list)) and (0 <= pos_2  and pos_2< size(my_list))):
        raise IndexError('list index out of range')
    else:
        info1 = my_list["elements"][pos_1]
        info2 = my_list["elements"][pos_2]
        my_list["elements"][pos_1] = info1
        my_list["elements"][pos_2] = info2
        return my_list
    
def sub_list(my_list, pos_i, num_elements):
    if not 0 < pos_i  or not pos_i< size(my_list):
        raise IndexError('list index out of range')
    else:
        ansList = new_list()
        for i in range(num_elements):
            add_last(ansList, my_list["elements"][pos_i + i])
        return ansList