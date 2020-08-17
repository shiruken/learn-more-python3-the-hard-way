from stack import *

def test_push():
    colors = Stack()
    colors.push("Red")
    assert colors.count() == 1
    colors.push("Green")
    assert colors.count() == 2
    colors.push("Blue")
    assert colors.count() == 3

def test_pop():
    colors = Stack()
    colors.push("Red")
    colors.push("Green")
    colors.push("Blue")
    assert colors.pop() == "Blue"
    assert colors.pop() == "Green"
    assert colors.pop() == "Red"
    assert colors.pop() == None

def test_first():
    colors = Stack()
    colors.push("Red")
    assert colors.first() == "Red"
    colors.push("Blue")
    assert colors.first() == "Blue"
    colors.push("Green")
    assert colors.first() == "Green"
