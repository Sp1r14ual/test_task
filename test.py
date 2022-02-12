from random import randint


def randomize(n, arr_sizes):
    '''
    Generates random number within certain bounds and add this number to set
    so it will not be generated again 
    '''
    random_size = randint(1, UPPER_BOUND + ADD_BOUND)
    while random_size in arr_sizes:
        random_size = randint(1, UPPER_BOUND + ADD_BOUND)
    
    arr_sizes.add(random_size)
    
    return random_size



def sort_arr(arr, index):
    '''
    Returns normally sorted array if index is even
    and sorted reversely if index is odd
    '''
    return sorted(arr) if index % 2 == 0 else sorted(arr, reverse=True)


def solve(n):
    '''Main function for algorithm'''

    arrays = list()
    arr_sizes = set()
    #Set is for unique array sizes

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
