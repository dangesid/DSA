class Node:
    def __init__(self,data, next_node=None):
        self.data = data
        self.next  = next_node

def arr_to_LL(arr):
    if not arr:
        return None

    head = Node(arr[0])
    curr = head

    for i in  arr[1:]:
        new_node = Node(i)
        curr.next = new_node
        curr = new_node
    return head

arr = [2,6,1,8]

head = arr_to_LL(arr)

def print_ll(head):
    curr = head
    while curr is not None:
        print(curr.data, end ="-->")
        curr = curr.next
    print(None)

print_ll(head)
