arr = [10, 20, 30, 40, 50]

arr.append(60)
arr.insert(2, 25)
arr.extend([70, 80])
arr.remove(40)
arr.pop()

print("Index of 30:", arr.index(30))
print("Count of 20:", arr.count(20))

arr.sort()
arr.reverse()

copy_arr = arr.copy()
arr.clear()

print("Copied array:", copy_arr)
print("Original array after clear:", arr)