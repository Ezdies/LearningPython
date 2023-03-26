l = ["ala", "123", "ala127"]

filtered = [''.join(char for char in string if not char.isdigit()) for string in l]

print(filtered)

