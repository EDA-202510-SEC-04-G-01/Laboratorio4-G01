from DataStructures.List import list_node as ln

def new_list():
    newlist = {
        'first': None,
        'last': None,
        'size': 0
    }
    return newlist

def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node[next]
        searchpos += 1
    return node["info"]

def is_present(my_list, element, cmp_function):
    is_in_array = False 
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1
    
    if not is_in_array:
        count = -1
    return count

def add_first(my_list, lmnt):
    node = ln.new_single_node(lmnt)
    node['next'] = my_list['first']
    my_list['first'] = node
    if (my_list['size'] == 0):
        my_list['last'] = my_list['first']
    my_list['size'] += 1
    return my_list

def add_last(my_list, lmnt):
    node = ln.new_single_node(lmnt)
    if my_list["size"] == 0:
        my_list["first"] = node
    else:
        my_list["last"]["next"] = node
    my_list['last'] = node
    my_list['size'] += 1
    return my_list

def size(my_list):
    return my_list["size"]

def is_empty(my_list):
    if size(my_list) == 0:
        return True
    else:
        return False

def first_element(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        return my_list["first"]
    
def last_element(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        return my_list["last"]
    
def remove_first(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        first = my_list["first"]["info"]
        second = my_list["first"]["next"]
        my_list["first"] = second
        my_list["size"] -= 1
        return first

def remove_last(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        last = my_list["last"]["info"]
        temp = my_list["first"]
        for _ in range(size(my_list)-1):
            temp = temp["next"]
        temp["next"] = None
        my_list["last"] = temp
        return last
    
def insert_element(my_list, lmnt, pos):
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        node = ln.new_single_node(lmnt)
        if pos == 0:
            node["next"] = my_list["first"]
            my_list["first"] = node
            my_list["size"] += 1
        elif pos == size(my_list):
            my_list["last"]["next"] = node
            my_list["last"] = node
            my_list["size"] += 1
        else:
            temp = my_list["first"]
            for _ in range(pos-1):
                temp = temp["next"]
            node["next"] = temp["next"]
            temp["next"] = node
            my_list["size"] += 1
    return my_list

def delete_element(my_list, pos):
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
    elif pos == 0:
        my_list["first"] = my_list["first"]["next"]
        my_list["size"] -= 1
    else:
        temp = my_list["first"]
        for _ in range(pos-1):
            temp = temp["next"]
        if temp["next"]["next"] == None:
            temp["next"] = temp["next"]["next"]
            my_list["size"] -= 1
            my_list["last"] = temp["next"]
        else:
            temp["next"] = temp["next"]["next"]
            my_list["size"] -= 1
    return my_list

def change_info(my_list, pos, new_info):
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
    elif pos == 0:
        my_list["first"]["info"] = new_info
    else:
        temp = my_list["first"]
        for _ in range(pos):
            temp = temp["next"]
        temp["info"] = new_info
    return my_list

def exchange(my_list, pos_1, pos_2):
    if pos_1 < 0 or pos_1 >= size(my_list) or pos_2 < 0 or pos_2 >= size(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        temp_1 = my_list["first"]
        for _ in range(pos_1):
            temp_1 = temp_1["next"]
        info_1 = temp_1["info"]
        temp_2 = my_list["first"]
        for _ in range(pos_2):
            temp_2 = temp_2["next"]
        info_2 = temp_2["info"]
        temp_1["info"] = info_2
        temp_2["info"] = info_1
    return my_list

def sub_list(my_list,pos, num_elements):
    if pos < 0 or pos + num_elements >= size(my_list):
        raise Exception('IndexError: list index out of range')
    new = new_list()
    temp = my_list["first"]
    for _ in range(pos):
        temp = temp["next"]
    for _ in range(num_elements + 1): #el +1 va porque estoy leyendo el de atras, pero sin un buen sistema de tests no estoy 100% seguro que así sea -Miguel
        add_last(new, temp["info"])
        temp = temp["next"]
    return new