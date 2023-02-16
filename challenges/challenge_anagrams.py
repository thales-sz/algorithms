def is_anagram(first_string, second_string):
    first_sorted = "".join(quick_sort(list(first_string.lower()), 0, None))
    second_sorted = "".join(quick_sort(list(second_string.lower()), 0, None))

    if not first_string or not second_string:
        return (first_sorted, second_sorted, False)
    if first_sorted == second_sorted:
        return (first_sorted, second_sorted, True)
    else:
        return (first_sorted, second_sorted, False)


def quick_sort(word, start, end):
    # ref: Quicksort do Course da Trybe: 'Algoritmos que usam dividir e conq'
    if end is None:
        end = len(word) - 1
    if start < end:
        p = partition(word, start, end)
        quick_sort(word, start, p - 1)
        quick_sort(word, p + 1, end)
    return word


def partition(word, start, end):
    pivot = word[end]
    delimiter = start - 1
    for index in range(start, end):
        if word[index] <= pivot:
            delimiter = delimiter + 1
            word[index], word[delimiter] = (
                word[delimiter],
                word[index],
            )
    word[delimiter + 1], word[end] = (
        word[end],
        word[delimiter + 1],
    )
    return delimiter + 1
