from DataStructures.List import array_list as sl


def new_queue():
    queue=sl.new_list()
    return queue

def enqueue(my_queue, element):
    queue=sl.add_last(my_queue, element)
    return queue

def dequeue(my_queue):
    if size(my_queue)==0:
        raise Exception('EmptyStructureError: queue is empty')
    else:
        element=sl.first_element(my_queue)
        my_queue=sl.remove_first(my_queue)
        return element
        
def peek(my_queue):
    if size(my_queue)==0:
        raise Exception('EmptyStructureError: queue is empty')
    else:
        element=sl.first_element(my_queue)
        return element

def is_empty(my_queue):
    return sl.size(my_queue)==0

def size(my_queue):
    return sl.size(my_queue)