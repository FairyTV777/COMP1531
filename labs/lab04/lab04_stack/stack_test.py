from stack import Stack

def test_stack():
    stack = Stack()
    stack.push(1)
    assert stack.items == [1]
    stack.push(2)
    assert stack.items == [1,2]
    stack.push(1)
    assert stack.items == [1, 2 ,1]
    stack.push(3)
    assert stack.items == [1, 2, 1, 3] 
    stack.pop()
    assert stack.items == [1, 2, 1]
    stack.pop()
    assert stack.items == [1, 2]
    stack.push(4)
    assert stack.items == [1, 2, 4]
    stack.pop()
    assert stack.items == [1, 2]
    stack.push(4)
    assert stack.items == [1, 2, 4]
