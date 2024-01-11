#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of an element in a new list.

    Parameters:
    - my_list: Initial list.
    - search: Element to replace in the list.
    - replace: New element.

    Returns:
    - A new list with all occurrences of 'search' replaced by 'replace'.
    """
    new_list = [replace if element == search else element for element in my_list]
    return new_list

if __name__ == "__main__":
    # Test the function with the provided example
    my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
    new_list = search_replace(my_list, 2, 89)

    # Print the result and the original list
    print(new_list)
    print(my_list)
