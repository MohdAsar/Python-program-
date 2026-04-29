size = int(input("Enter size of array: "))
arr = []

for i in range(size):
    value = int(input("Enter element: "))
    arr.append(value)

position = int(input("Enter position to insert: "))
new_value = int(input("Enter value to insert: "))

if position>=0 and position <= size:
    arr.insert(position, new_value)
    print("Updated array:", arr)
else:
    print("Invalid position")

print("Final array:", arr)