from queue import *

def test_shift():
    colors = Queue()
    colors.shift("Red")
    assert colors.count() == 1
    colors.shift("Green")
    assert colors.count() == 2
    colors.shift("Blue")
    assert colors.count() == 3

def test_unshift():
    colors = Queue()
    colors.shift("Red")
    colors.shift("Green")
    colors.shift("Blue")
    assert colors.unshift() == "Red"
    assert colors.unshift() == "Green"
    assert colors.unshift() == "Blue"
    assert colors.unshift() == None

def test_head():
    colors = Queue()
    colors.shift("Red")
    assert colors.first() == "Red"
    colors.shift("Blue")
    assert colors.first() == "Red"
    colors.shift("Green")
    assert colors.first() == "Red"
