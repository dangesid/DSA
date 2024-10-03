from Arr_to_LL import arr_to_LL, print_ll
from Search_element import search_element_in_ll

if __name__ == "__main__":
    arr = [2, 3, 1, 8]  # Sample array
    head = arr_to_LL(arr)  # Convert array to linked list

    # Print the linked list created from the array
    print_ll(head)

    # Search for an element in the linked list
    target = 1  # Element to search for
    index = search_element_in_ll(head, target)

    if index != -1:
        print(f"Element {target} found at index: {index}")
    else:
        print(f"Element {target} not found in the linked list.")
