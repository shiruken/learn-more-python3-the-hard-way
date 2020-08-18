def bubble_sort(numbers):
    """Sorts a double linked list of numbers using bubble sort."""
    while True:
        is_sorted = True
        node = numbers.begin.next
        while node:
            if node.prev.value > node.value:
                node.prev.value, node.value = node.value, node.prev.value
                is_sorted = False
            node = node.next

        if is_sorted:
            break




def merge_sort(numbers):
    """Sorts a double linked list of numbers using merge sort."""    
    numbers.begin = merge_sort_node(numbers.begin)


def merge_sort_node(start):
    """Sorts double linked list nodes using merge sort."""
    if start.next is None:
        return start

    count = 0
    node = start
    while node:
        count += 1
        node = node.next   
    
    node = start
    for i in range(0, count // 2 - 1):
        node = node.next

    middle = node.next
    node.next = None
    middle.prev = None

    left = merge_sort_node(start)
    right = merge_sort_node(middle)

    return merge(left, right)


def merge(left, right):
    """Merges two double linked list nodes together."""
    if left is None:
        return right
    if right is None:
        return left

    if left.value > right.value:
        result = right
        result.next = merge(left, right.next)
    else:
        result = left
        result.next = merge(left.next, right)

    result.next.prev = result
    return result


def quick_sort(numbers, lo, hi):
    """Sorts a double linked list of numbers using quick sort."""    
    if lo < hi:
        n = quick_sort_partition(numbers, lo, hi)
        quick_sort(numbers, lo, n - 1)
        quick_sort(numbers, n + 1, hi)

def quick_sort_partition(numbers, lo, hi):
    pivot = get_node(numbers, hi)
    i = lo - 1

    for j in range(lo, hi):
        node_j = get_node(numbers, j)
        if node_j.value < pivot.value:
            i += 1
            if i != j:
                node_i = get_node(numbers, i)
                node_i.value, node_j.value = node_j.value, node_i.value

    node_hi = get_node(numbers, hi)
    node_i = get_node(numbers, i + 1)

    if node_hi.value < node_i.value:
        node_hi.value, node_i.value = node_i.value, node_hi.value

    return i + 1


def get_node(numbers, i):
    count = 0
    node = numbers.begin
    while node and count < i:
        node = node.next
        count += 1
    return node
