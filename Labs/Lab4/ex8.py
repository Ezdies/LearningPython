l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

filtered = [x*2 for x in l if x % 2 == 1 and x % 3 != 0]

print(filtered)
