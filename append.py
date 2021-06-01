names = [ ]

# Append add a new element in array.
names.append('Rodrigo')
names.append('Maria')
names.append('Joh')
names.append('Carlos')
names.append('Matheus')

# Remove an element in array
names.pop(1)

# Value array edit
names[1] = 'Carlos Eduardo'

# Remove by value
names.remove('Carlos')

# Verify if value exists
exists = 'Playstation' in names
print(exists)

print(names)