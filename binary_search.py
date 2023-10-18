# code your iterative algorithm here
from random_list_gen import make_random_list

random_list_of_data = make_random_list(100, 0, 100)

def binary_search(lst, target):
    first = 0
    last = len(lst) - 1
    found = False

    sorted_list = sorted(lst)
    while first <= last and not found:
        mid = (first + last) // 2

        if sorted_list[mid] == target:
            found = True
        else:
            if target < sorted_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
            
    return found

print(random_list_of_data)
print(binary_search(random_list_of_data, 35))
