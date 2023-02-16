def find_duplicate(nums):
    try:
        list_of_numbers = sorted(nums)
        for i in range(len(list_of_numbers) - 1):
            if list_of_numbers[i] == list_of_numbers[i + 1]:
                return list_of_numbers[i]
    except (TypeError, AssertionError):
        return False
    finally:
        return False


def binary_search(numbers):
    list_of_numbers = sorted(numbers)
    left = 0
    right = len(numbers) - 1
    while left < right:
        mid = (left + right) // 2
        if list_of_numbers[mid] == list_of_numbers[mid + 1]:
            return list_of_numbers[mid]
        elif list_of_numbers[mid] == list_of_numbers[mid - 1]:
            return list_of_numbers[mid]
        elif (
            list_of_numbers[mid] - list_of_numbers[left]
            < list_of_numbers[right] - list_of_numbers[mid]
        ):
            left = mid + 1
        else:
            right = mid + 1
    return False
