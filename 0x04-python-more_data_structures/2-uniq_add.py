#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list (only once for each integer).

    Parameters:
    - my_list: List of integers.

    Returns:
    - Sum of all unique integers in the list.
    """
    unique_sum = sum(set(my_list))
    return unique_sum

if __name__ == "__main__":
    # Test the function with the provided example
    my_list = [1, 2, 3, 1, 4, 2, 5]
    result = uniq_add(my_list)

    # Print the result
    print("Result: {:d}".format(result))

