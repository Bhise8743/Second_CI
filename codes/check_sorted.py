
def is_sorted(numbers):
    """
    Check whether a list is sorted in ascending order.

    Equal adjacent elements are allowed.
    An empty list or a single-element list is sorted.

    Returns:
        bool: True if sorted, otherwise False.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")

    return all(
        numbers[i] <= numbers[i + 1]
        for i in range(len(numbers) - 1)
    )


if __name__ == "__main__":
    values = input("Enter numbers separated by spaces: ")

    try:
        numbers = [int(value) for value in values.split()]
        print(is_sorted(numbers))
    except ValueError:
        print("Please enter valid integers.")
