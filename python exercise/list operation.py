lst = [5, 10, 15, 20, 25]

lst.append(30)
lst.insert(2, 12)
lst.extend([35, 40])
lst.remove(10)
lst.pop()

print("Index of 15:", lst.index(15))
print("Count of 5:", lst.count(5))

lst.sort()
lst.reverse()

copy_lst = lst.copy()
lst.clear()

print("Copied list:", copy_lst)
print("Original list after clear:", lst)