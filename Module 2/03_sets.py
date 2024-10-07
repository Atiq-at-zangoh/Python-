
#  SETS

set_a = {1, 2, 3, 4, 5, 4, 1}
print(set_a)
print(type(set_a))

set_a.discard(4)
print(set_a)

set_a.remove(1)
print(set_a)

set_a.add(1)
print(set_a)

set_a.pop()
print(set_a)


set_b = {4, 5, 6, 7, 8, 9}

# Set operations

print(set_a | set_b)

print(set_a & set_b)

print(set_a - set_b)

print(set_a ^ set_b)

print(set_a.union(set_b))
print(set_a.intersection(set_b))
print(set_a.difference(set_b))
print(set_a.symmetric_difference(set_b))


print(set_a.issubset(set_b))
print(set_a.issuperset(set_b))
print(set_a.isdisjoint(set_b))

