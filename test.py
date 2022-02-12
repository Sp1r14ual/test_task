from random import randint


def randomize(n, arr_sizes):

    random_size = randint(1, UPPER_BOUND + ADD_BOUND)
    while random_size in arr_sizes:
        random_size = randint(1, UPPER_BOUND + ADD_BOUND)
    
    arr_sizes.add(random_size)
    
    return random_size



def sort_arr(arr, index):

    return sorted(arr) if index % 2 == 0 else sorted(arr, reverse=True)


def solve(n):

    arrays = list()
    arr_sizes = set()


    for i in range(1, n + 1):

        new_arr = list()

        random_size = randomize(n, arr_sizes)
        
        for _ in range(random_size):
            new_arr.append(randint(LOWER_BOUND, UPPER_BOUND))

        new_arr = sort_arr(new_arr, i)

        arrays.append(new_arr)

    return arrays


n = int(input())

UPPER_BOUND = n
LOWER_BOUND = -UPPER_BOUND
ADD_BOUND = 10

solution = solve(n)
for i in range(len(solution)):
    print(solution[i])


# nsk.school.handh.ru
# docs.google.com/document/d/1lfpe1JDCuGMQ3cFyn5oNk2PqRO94z6IqCq6yoTaUsYo