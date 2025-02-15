from DataStructures.List import array_list as sl


def new_queue():
    queue=sl.new_list()
    return queue

def enqueue(my_queue, element):
    queue=sl.add_last(my_queue, element)
    return queue

def dequeue(my_queue):
    try:
        element=sl.first_element(my_queue)
        queue=sl.remove_first(my_queue)
        return element
    except Exception as exp:
        print("EmptyStructureError: queue is empty")
        
def peek(my_queue):
    try:
        element=sl.first_element(my_queue)
        return element
    except Exception as exp:
        print("EmptyStructureError: queue is empty")

def is_empty(my_queue):
    return sl.size(my_queue)==0

def size(my_queue):
    return sl.size(my_queue)