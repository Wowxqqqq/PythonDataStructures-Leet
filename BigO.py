# O(n)
# def print_items(n):
#     for i in range(n):
#         print(i)
#     for j in range(n):
#         print(j)
#
# print_items(10)

# O(n**2)
# Less efficient from a time complexity standpoint.
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

print_items(10)