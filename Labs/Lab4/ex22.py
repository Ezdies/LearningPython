l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

result1 = filter(lambda x: x % 3 != 0, l)

print(list(result1))


l = ["mama", "kot69", "tw0jaStara"]

result2 = "".join(filter(lambda x: not x.isalpha(), l))

print(list(result2))
