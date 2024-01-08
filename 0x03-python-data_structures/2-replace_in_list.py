#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list

    my_list[idx] = element
    return my_list

# Example usage:
if __name__ == "__main__":
    original_list = [1, 2, 3, 4, 5]
    index_to_replace = 2
    new_element = 10

    modified_list = replace_in_list(original_list, index_to_replace, new_element)

    print("Original list:", original_list)
    print("Modified list:", modified_list)

