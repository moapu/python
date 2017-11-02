# container to save the values
recursive_cache = {}


def recursion(n):
    # if the values exits in the container, it simply returns it
    if n in recursive_cache:
        return recursive_cache[n]

    # base cases
    if n == 1:
        value = 2
    elif n == 2:
        value = -3
    elif n == 3:
        value = 1
    elif n > 3:
        # formula for if 'n' is larger than 3
        # calls itself here [recursion]
        value = (-2 * recursion(n - 1)) + (3 * recursion(n - 2)) - recursion(n - 3)

    # saves the value to the container
    recursive_cache[n] = value
    return value


# runs through number 1-58 and prints out the values for each number
for n in range(1, 59):
    print("{} ->> [{}]".format(n, recursion(n)))
