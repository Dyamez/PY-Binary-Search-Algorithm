from random_list_gen import make_random_list

sample_list = make_random_list(100)

def recursive_binary_search(lst, target):

    print(f"data: {lst}")

    if len(lst) == 0:
        return - 1
    else:
        mid = len(lst) // 2

        print(f"mid is {mid}")

        if lst[mid] == target:
            return mid
        else:
            if target < lst[mid]:
                return recursive_binary_search(lst[:mid], target)
            else:
                return recursive_binary_search(lst[mid + 1:], target)

sample_list = make_random_list(100)
sample_list = make_random_list(100)        
print(recursive_binary_search(sorted(sample_list), 35))
        