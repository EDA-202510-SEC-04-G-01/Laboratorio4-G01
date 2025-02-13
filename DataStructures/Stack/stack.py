from DataStructures.Stack import stack as st

def new_stack():
    stack = st.new_stack()
    return stack

def push(stack, element):
    stack = st.push(stack, element)
    return stack

def pop(stack):
    stack = st.pop(stack)
    return stack

def is_empty(stack):
    rta = st.is_empty(stack)
    return rta

def top(stack):
    top = st.top(stack)
    return top

def size(stack):
    size = st.size(stack)
    return size

    