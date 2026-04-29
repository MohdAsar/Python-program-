d = {
    'name': 'Rohit Sharma',
    'centuries': 29,
    'sr': 130.44,
    'team': 'India'
}

d['avg'] = 49.55
d.pop('sr')

print("Keys:", d.keys())
print("Values:", d.values())
print("Is 'team' a key?", 'team' in d)

d.clear()
print("Dictionary after clear:", d)