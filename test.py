from random import randint

def solve(n):

    UPPER_BOUND = n
    LOWER_BOUND = -UPPER_BOUND
    ADD_BOUND = 10


    arrays = list()
    arr_sizes = set()


    for i in range(1, n + 1):

        new_arr = list()

        random_size = randint(1, UPPER_BOUND + ADD_BOUND)
        while random_size in arr_sizes:
            random_size = randint(1, UPPER_BOUND + ADD_BOUND)
        
        arr_sizes.add(random_size)
        for _ in range(random_size):
            new_arr.append(randint(LOWER_BOUND, UPPER_BOUND))
        
        if i % 2 == 0:
            new_arr.sort()
        else:
            new_arr.sort(reverse=True)

        arrays.append(new_arr)

    return arrays



solution = solve(int(input()))
for i in range(len(solution)):
    print(solution[i])


# nsk.school.handh.ru
# docs.google.com/document/d/1lfpe1JDCuGMQ3cFyn5oNk2PqRO94z6IqCq6yoTaUsYo