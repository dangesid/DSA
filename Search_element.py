def search_element_in_ll(head,target):
    temp = head
    index = 0
    while temp is not None:
        if temp.data == target:
            return index
        temp = temp.next
        index+=1
    return -1


