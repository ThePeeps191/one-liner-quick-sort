qsort = lambda l : l if len(l) <= 1 else qsort([x for x in l[1:] if x < l[0]]) + [l[0]] + qsort([x for x in l[1:] if x >= l[0]])

# Example
a = [1, 4, 2, 5, 2, 10, 24, 21, 2, 54]
print(qsort(a)) # Prints out: [1, 2, 2, 2, 4, 5, 10, 21, 24, 54]
