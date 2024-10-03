from Arr_to_LL import arr_to_LL, print_ll,arr

def len_ll(head):
    temp = head
    count = 0
    while temp is not None:
        count+=1
        temp = temp.next
    return count

if __name__ == "__main__":

    head = arr_to_LL(arr)
    # print_ll(head)
    length = len_ll(head)
    print(f"Length of linked list is {length}.")