# Course: CS261 - Data Structures
# Student Name: Jeremy Vernon
# Assignment: 1
# Description: Python Fundamentals Review

import random

from a1_include import *

arr = StaticArray(5)


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------


def min_max(arr: StaticArray) -> ():
    """
    Searches for the min and max in an array.
    """
    minimum = arr.get(0)  # sets min to first element
    maximum = arr.get(0)  # sets max to first element
    # iterate over the elements in the array to check for < or >
    for i in range(arr.size()):
        if arr[i] < minimum:  # if element is less than the current min, min = new element
            minimum = arr[i]
        elif arr[i] > maximum:  # if element is greater than the current max, max = new element
            maximum = arr[i]
    return minimum, maximum


# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------


def fizz_buzz(arr: StaticArray) -> StaticArray:
    """
    Checks if elements are divisible by or by 5.
    If divisible by 3, replaces element with "fizz."
    If divisible by 5, replaces element with "buzz."
    If divisible by both 3 and 5, replaces element with "fizzbuzz."
    """
    # create a new array so that original elements are preserved.
    new_array = StaticArray(arr.size())
    for i in range(arr.size()):
        new_array.set(i, arr.get(i))
    # declare initial variables
    mod_3 = False
    mod_5 = False
    # iterate to check for divisible by 3 and/or divisible by 5
    for i in range(arr.size()):
        if new_array.get(i) % 3 == 0:
            mod_3 = True
        if new_array.get(i) % 5 == 0:
            mod_5 = True
        if mod_3 and mod_5:
            new_array.set(i, "fizzbuzz")
        elif mod_3:
            new_array.set(i, "fizz")
        elif mod_5:
            new_array.set(i, "buzz")
        # reset checks
        mod_3 = False
        mod_5 = False

    return new_array


# ------------------- PROBLEM 3 - REVERSE -----------------------------------


def reverse(arr: StaticArray) -> None:
    """
    Reverses the order of elements in an array.
    """
    # Sets the length as an integer of half the size of the array.
    length = int(arr.size() / 2)

    for index in range(length):
        # Gets the first and last unsorted elements
        beginning = arr.get(index)
        end = arr.get((arr.size() - 1) - index)
        # Swaps the first and last unsorted elements
        arr.set(index, end)
        arr.set((arr.size() - 1) - index, beginning)


# ------------------- PROBLEM 4 - ROTATE ------------------------------------


def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
    Shifts elements a certain number of steps.
    """
    length = arr.size()
    new_array = StaticArray(length) # Creates a new array to preserve original elements
    for i in range(length):
        pos = i + steps # Adds steps to index number
        if pos == length: # If index is 1 more than last index, change to first index
            pos = 0
        while pos > (length - 1): # If index is greater than the range, subtract by size of array
            pos -= length
        while pos < 0: # If index is less than the range, add by size of array
            pos += length
        new_array.set(pos, arr.get(i)) # Set position

    return new_array


# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------


def sa_range(start: int, end: int) -> StaticArray:
    """
    Creates an array of consecutive integers.
    """
    forward = True # Declares variable for direction
    # Sets the number of elements to create
    if end > start:
        length = abs((end - start) + 1)
    else:
        length = abs((start - end) + 1)
        forward = False
    arr = StaticArray(length) # Creates a length n array

    # Fills array with consecutive integers
    for index in range(length):
        arr.set(index, start)
        if forward:
            start += 1
        else:
            start -= 1

    return arr


# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------


def is_sorted(arr: StaticArray) -> int:
    """
    Checks if an array is sorted
    """
    length = arr.size() - 1

    # If only one element in the array
    if arr.size() == 1:
        return 1

    # Compares each element with the one after it to check for ascending order
    elif arr.get(length) > arr.get(0):
        for index in range(length):
            if arr.get(index) >= arr.get(index + 1):
                return 0
        return 1

    # Compares each element with the one after it to check for descending order
    elif arr.get(0) > arr.get(length):
        for index in range(length):
            if arr.get(index + 1) > arr.get(index):
                return 0
        return 2

    else:
        return 0


# ------------------- PROBLEM 7 - SA_SORT -----------------------------------


def sa_sort(arr: StaticArray) -> None:  # Need to fix
    """
    TODO: Write this implementation
    """
    length = arr.size()
    iteration_count = 0
    min_old_index = 0
    max_old_index = 0
    while iteration_count < (length / 2):
        min = arr[iteration_count]
        max = arr[iteration_count]

        for index in range(iteration_count, (length - iteration_count)):

            if arr[index] < min:
                min = arr[index]
                min_old_index = index
            elif arr[index] > max:
                max = arr[index]
                max_old_index = index

        max_pos = (length - 1) - iteration_count

        if arr[iteration_count] != min:
            if arr[min_old_index] != max:
                arr[min_old_index] = arr[iteration_count]
            else:
                arr[max_old_index] = arr[iteration_count]
            arr[iteration_count] = min
        if arr[max_pos] != max:
            if arr[max_old_index] != min:
                arr[max_old_index] = arr[max_pos]
            else:
                arr[min_old_index] = arr[max_pos]
            arr[max_pos] = max

        iteration_count += 1


# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------


def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    """

    length = arr.size()
    working_array = StaticArray(length)
    working_array.set(0, arr[0])
    for index in range(1, length):
        if arr[index] != arr[index - 1]:
            working_array.set(index, arr[index])


    count = 0
    if working_array.size() == 1:
        count = 1
    else:
        for index in range(working_array.size()):
            if working_array[index] != None:
                count += 1
    new_array = StaticArray(count)

    new_array_index = 0

    if working_array.size() == 1:
        new_array.set(0, working_array[0])
    else:
        for index in range(working_array.size()):
            if working_array[index] != None:
                new_array.set(new_array_index, working_array[index])
                new_array_index += 1
    return new_array


# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------


def count_sort(arr: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    """
    # finds the maximum element
    max = arr[0]
    for index in range(arr.size()):
        if abs(arr[index]) > max:
            max = abs(arr[index])

    # creates max+1 arrays for positives and negatives
    max += 1
    count_pos = StaticArray(max)
    count_neg = StaticArray(max)

    # records the number of iterations of an array element by setting the corresponding index position of the count array to the number of iterations
    # positive numbers
    for index in range(arr.size()):
        current = arr[index]
        if current > 0:
            if count_pos[current] == None:
                count_pos.set(current, 1)
            else:
                count_pos[current] += 1

        # zero
        elif current == 0:
            if count_pos[0] == None:
                count_pos[0] = 1
            else:
                count_pos[0] += 1

        # negative numbers
        else:
            if count_neg[abs(current)] == None:
                count_neg.set(abs(current), 1)
            else:
                count_neg[abs(current)] += 1
            count_neg.set(abs(current), 1)

    # sums non-empty spaces and sets empty spaces equal to zero
    length = 0
    # iterate through positive array
    for index in range(count_pos.size()):
        if count_pos[index] == None:
            count_pos[index] = 0
        else:
            length += count_pos[index]

    # iterate through negative array
    for index in range(count_neg.size()):
        if count_neg[index] == None:
            count_neg[index] = 0
        else:
            length += count_neg[index]

    # create array for the results
    result_array = StaticArray(length)

    # adds elements in positive array to results array from largest to smallest
    result_array_index = 0
    last = count_pos.size() - 1
    for index in range(count_pos.size()):
        while count_pos[last] > 0:
            result_array.set(result_array_index, last)
            result_array_index += 1
            count_pos[last] -= 1
        last -= 1

    # adds elements in negative array to results array from largest to smallest
    for index in range(count_neg.size()):
        while count_neg[index] > 0:
            result_array.set(result_array_index, -(index))
            result_array_index += 1
            count_neg[index] -= 1

    return result_array


# ------------------- PROBLEM 10 - SA_INTERSECTION --------------------------


def sa_intersection(arr1: StaticArray, arr2: StaticArray, arr3: StaticArray) \
        -> StaticArray:
    """
    TODO: Write this implementation
    """
    working_array_1 = StaticArray(arr1.size())
    length = 0
    for index1 in range(arr1.size()):
        for index2 in range(arr2.size()):
            if arr1[index1] == arr2[index2]:
                working_array_1.set(length, arr1[index1])
                length += 1
                break

    if length == 0:
        results_array = StaticArray(1)
    else:
        working_array_2 = StaticArray(arr3.size())
        length = 0
        for index3 in range(working_array_1.size()):
            for index4 in range(arr3.size()):
                if working_array_1[index3] == arr3[index4]:
                    working_array_2.set(length, arr3[index4])
                    length += 1
                    break

        if length == 0:
            results_array = StaticArray(1)
        else:
            results_array = StaticArray(length)
            results_array_index = 0
            for index5 in range(working_array_2.size()):
                if working_array_2[index5] != None:
                    results_array.set(results_array_index, working_array_2[index5])
                    results_array_index += 1

    return results_array


# ------------------- PROBLEM 11 - SORTED SQUARES ---------------------------


def sorted_squares(arr: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    """

    def count_sort_ascending(arr: StaticArray) -> StaticArray:
        """
        TODO: Write this implementation
        """
        # finds the maximum element
        max = arr[0]
        for index in range(arr.size()):
            if abs(arr[index]) > max:
                max = abs(arr[index])

        # creates max+1 arrays for positives and negatives
        max += 1
        count_pos = StaticArray(max)

        # records the number of iterations of an array element by setting the corresponding index position of the count array to the number of iterations
        for index in range(arr.size()):
            current = arr[index]
            if abs(current) > 0:
                if count_pos[abs(current)] == None:
                    count_pos.set(abs(current), 1)
                else:
                    count_pos[abs(current)] += 1

            # zero
            elif current == 0:
                if count_pos[0] == None:
                    count_pos[0] = 1
                else:
                    count_pos[0] += 1

        # sums non-empty spaces and sets empty spaces equal to zero
        length = 0
        # iterate through positive array
        for index in range(count_pos.size()):
            if count_pos[index] == None:
                count_pos[index] = 0
            else:
                length += count_pos[index]

        # create array for the results
        result_array = StaticArray(length)

        result_array_index = 0

        # adds elements in positive array to results array from largest to smallest
        for index in range(count_pos.size()):
            while count_pos[index] > 0:
                result_array.set(result_array_index, index)
                result_array_index += 1
                count_pos[index] -= 1

        return result_array

    result_array = count_sort_ascending(arr)
    for index in range(result_array.size()):
        result_array[index] **= 2

    return result_array


# ------------------- PROBLEM 12 - ADD_NUMBERS ------------------------------


def add_numbers(arr1: StaticArray, arr2: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    """
    num_1 = 0
    num_2 = 0
    length_1 = arr1.size()
    length_2 = arr2.size()

    for index in range(arr1.size()):
        num_1 += arr1[index] * (10 ** (length_1 - index))
    for index in range(arr2.size()):
        num_2 += arr2[index] * (10 ** (length_2 - index))

    result = num_1 + num_2

    if length_1 > length_2:
        length = length_1
    else:
        length = length_2

    result_arr = StaticArray(length)
    result_arr_index = 0
    while result > 0:
        num_3 = result / (10 ** length)
        if num_3 > 10:
            working_arr = StaticArray(result_arr.size() + 1)
            for index in range(result_arr.size()):
                working_arr.set(index, result_arr[index])
            result_arr = StaticArray(working_arr.size())
            for index in range(working_arr.size()):
                result_arr.set(index, working_arr[index])
            num_3 /= 10
            length += 1
        num_3 = int(num_3)
        result_arr.set(result_arr_index, num_3)
        result_arr_index += 1
        num_4 = num_3 * (10 ** length)
        result -= num_4
        length -= 1

    return result_arr


# ------------------- PROBLEM 13 - BALANCED_STRINGS -------------------------


def balanced_strings(s: str) -> StaticArray:
    """
    TODO: Write this implementation
    """
    working_array = StaticArray(len(s))
    working_array_index = 0
    a_count = b_count = c_count = 0
    new_s = ""
    for char in s:
        if char.lower() == "a":
            new_s += char
            a_count += 1
        elif char.lower() == "b":
            new_s += char
            b_count += 1
        else:
            new_s += char
            c_count += 1

        if a_count == b_count == c_count:
            working_array.set(working_array_index, new_s)
            working_array_index += 1
            new_s = ""

    result_length = 0
    for index in range(working_array.size()):
        if working_array[index] is not None:
            result_length += 1

    result_array = StaticArray(result_length)
    for index in range(result_array.size()):
        result_array.set(index, working_array[index])

    return result_array


# ------------------- PROBLEM 14 - TRANSFORM_STRING -------------------------


def transform_string(source: str, s1: str, s2: str) -> str:
    """
    TODO: Write this implementation
    """
    new_string = ""
    for index in range(len(source)):
        char = source[index]
        if char in s1:
            source = s2[index]
        else:
            if char.isupper():
                new_string += " "
            elif char.islower():
                new_string += "#"
            elif char.isdigit():
                new_string += "!"
            else:
                new_string += "="

    return new_string


# BASIC TESTING
if __name__ == "__main__":

    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(min_max(arr))

    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(min_max(arr))

    print('\n# min_max example 3')
    arr = StaticArray(3)
    for i, value in enumerate([3, 3, 3]):
        arr[i] = value
    print(min_max(arr))

    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)

    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)

    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100]:
        print(rotate(arr, steps), steps)
    print(arr)

    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-105, -99), (-99, -105)]
    for start, end in cases:
        print(start, end, sa_range(start, end))

    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print('Result:', is_sorted(arr), arr)

    print('\n# sa_sort example 1')
    test_cases = (
        [1, 10, 2, 20, 3, 30, 4, 40, 5],
        ['zebra2', 'apple', 'tomato', 'apple', 'zebra1'],
        [(1, 1), (20, 1), (1, 20), (2, 20)],
        [random.randrange(-30000, 30000) for _ in range(5_000)]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr if len(case) < 50 else 'Started sorting large array')
        sa_sort(arr)
        print(arr if len(case) < 50 else 'Finished sorting large array')

    print('\n# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)

    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [random.randrange(-499, 499) for _ in range(1_000_000)]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr if len(case) < 50 else 'Started sorting large array')
        result = count_sort(arr)
        print(result if len(case) < 50 else 'Finished sorting large array')

    print('\n# sa_intersection example 1')
    test_cases = (
        ([1, 2, 3], [3, 4, 5], [2, 3, 4]),
        ([1, 2], [2, 4], [3, 4]),
        ([1, 1, 2, 2, 5, 75], [1, 2, 2, 12, 75, 90], [-5, 2, 2, 2, 20, 75, 95])
    )
    for case in test_cases:
        arr = []
        for i, lst in enumerate(case):
            arr.append(StaticArray(len(lst)))
            for j, value in enumerate(sorted(lst)):
                arr[i][j] = value
        print(sa_intersection(arr[0], arr[1], arr[2]))

    print('\n# sorted_squares example 1')
    test_cases = (
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1, 0],
        [-3, -2, -2, 0, 1, 2, 3],
        [random.randrange(-10_000, 10_000) for _ in range(1_000_000)]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr if len(case) < 50 else 'Started sorting large array')
        result = sorted_squares(arr)
        print(result if len(case) < 50 else 'Finished sorting large array')

    print('\n# add_numbers example 1')
    test_cases = (
        ([1, 2, 3], [4, 5, 6]),
        ([0], [2, 5]),
        ([2, 0, 9, 0, 7], [1, 0, 8]),
        ([9, 9, 9], [9, 9, 9, 9])
    )
    for num1, num2 in test_cases:
        n1 = StaticArray(len(num1))
        n2 = StaticArray(len(num2))
        for i, value in enumerate(num1):
            n1[i] = value
        for i, value in enumerate(num2):
            n2[i] = value
        print('Original nums:', n1, n2)
        print('Sum: ', add_numbers(n1, n2))

    print('\n# balanced_strings example 1')
    test_cases = (
        'aaabbbccc', 'abcabcabc', 'babcCACBCaaB', 'aBcCbA', 'aBc',
        'aBcaCbbAcbCacAbcBa', 'aCBBCAbAAcCAcbCBBa', 'bACcACbbACBa',
        'CBACcbcabcAaABb'
    )
    for case in test_cases:
        print(balanced_strings(case))

    print('\n# transform_strings example 1')
    test_cases = ('eMKCPVkRI%~}+$GW9EOQNMI!_%{#ED}#=-~WJbFNWSQqDO-..@}',
                  'dGAqJLcNC0YFJQEB5JJKETQ0QOODKF8EYX7BGdzAACmrSL0PVKC',
                  'aLiAnVhSV9}_+QOD3YSIYPR4MCKYUF9QUV9TVvNdFuGqVU4$/%D',
                  'zmRJWfoKC5RDKVYO3PWMATC7BEIIVX9LJR7FKtDXxXLpFG7PESX',
                  'hFKGVErCS$**!<OS<_/.>NR*)<<+IR!,=%?OAiPQJILzMI_#[+}',
                  'EOQUQJLBQLDLAVQSWERAGGAOKUUKOPUWLQSKJNECCPRRXGAUABN',
                  'WGBKTQSGVHHHHHTZZZZZMQKBLC66666NNR11111OKUN2KTGYUIB',
                  'YFOWAOYLWGQHJQXZAUPZPNUCEJABRR6MYR1JASNOTF22MAAGTVA',
                  'GNLXFPEPMYGHQQGZGEPZXGJVEYE666UKNE11111WGNW2NVLCIOK',
                  'VTABNCKEFTJHXATZTYGZVLXLAB6JVGRATY1GEY1PGCO2QFPRUAP',
                  'UTCKYKGJBWMHPYGZZZZZWOKQTM66666GLA11111CPF222RUPCJT')
    for case in test_cases:
        print(transform_string(case, '612HZ', '261TO'))
