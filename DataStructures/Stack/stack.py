from DataStructures.List import single_linked_list as sl

def new_stack():
    new_stack = sl.new_list()
    return new_stack

def push(stack, element):
    new_stack = sl.add_first(stack, element)
    return new_stack

def pop(stack):
    new_stack = sl.remove_first(stack)
    return new_stack

def is_empty(stack):
    rta = sl.is_empty(stack)
    return rta

def top(stack):
    top = sl.first_element(stack)
    return top

def size(stack):
    size = sl.size(stack)
    return size

    