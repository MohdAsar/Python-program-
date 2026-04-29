empty_tuple = ()
int_tuple = (1, 2, 3)
string_tuple = ("apple", "banana", "cherry")
float_tuple = (1.1, 2.2, 3.3)
nested_tuple = (1, (2, 3), ["a", "b", "c"])

print("Empty Tuple:", empty_tuple)
print("Integer Tuple:", int_tuple)
print("String Tuple:", string_tuple)
print("Float Tuple:", float_tuple)
print("Nested Tuple:", nested_tuple)

print("\nIndexing:")
print("First element of int_tuple:", int_tuple[0])
print("Second element of string_tuple:", string_tuple[1])
print("Nested tuple second element:", nested_tuple[1])

print("\nNested Tuple Indexing:")
print("Second element of nested_tuple:", nested_tuple[1])
print("First element of second tuple inside nested_tuple:", nested_tuple[1][0])

print("\nNegative Indexing:")
print("Last element of string_tuple:", string_tuple[-1])
print("Second last element of float_tuple:", float_tuple[-2])

print("\nSlicing:")
print("First two elements of int_tuple:", int_tuple[:2])
print("Last two elements of string_tuple:", string_tuple[-2:])

print("\nModifying List Inside Tuple:")
nested_tuple[2].append("d")
print("Modified Nested Tuple:", nested_tuple)

sample_tuple = (1, 2, 3, 2, 4, 2, 5)

print("\nTuple Methods:")
print("Count of 2 in sample_tuple:", sample_tuple.count(2))
print("Index of first occurrence of 4:", sample_tuple.index(4))

del_tuple = (10, 20, 30)
print("\nDeleting Tuple:")
print("Tuple before deletion:", del_tuple)

del del_tuple

try:
    print(del_tuple)
except NameError:
    print("Tuple deleted successfully.")