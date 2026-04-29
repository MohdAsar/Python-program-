# Linear Search
arr = [10, 25, 35, 40, 55, 60]
x = 35
found = False

for i in range(len(arr)):
    if arr[i] == x:
        print("Linear Search: Found at index", i)
        found = True
        break

if not found:
    print("Linear Search: Not found")


# Binary Search
arr.sort()
x = 35
low = 0
high = len(arr) - 1
found = False

while low <= high:
    mid = (low + high) // 2
    if arr[mid] == x:
        print("Binary Search: Found at index", mid)
        found = True
        break
    elif arr[mid] < x:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print("Binary Search: Not found")