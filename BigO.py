# O(n)
def print_items(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)

print_items(10)

# O(n**2)
# Less efficient from a time complexity standpoint.
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

print_items(10)

# Drop Non-Dominants
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

    for k in range(n):
        print(k)

print_items(10)

# O(1)
# Most efficient of all BigO
def add_items(n):
    return n + n + n

# O(log n)
# Second most efficient

# O(a + b)
# When it has two different parameters.
# Cannot just classify both parameters as n and then drop constant to get O(n).
def print_items(a, b):
    for i in range(a):
        print(i)
    for j in range(b):
        print(j)