# problem 1
a, b, c = (1, 2, 3)
print(a, b, c) # 1 2 3

# problem 2
a, _, c = (1, 2, 3)
print(_) # throwaway variable but still variable, so 2

# problem 3
a, b = (1, 2, 3)
# ValueError
# problem 4
a, b, c, d, e = (1, 2, 3)
# problem 5
a, *rest = [1, 2, 3, 4, 5]
print(rest) # [2, 3, 4, 5]
# problem 6first, *middle, last = "hello"
print(f"First: {first}, Middle: {middle}, Last: {last}")
#h, ['e', 'l','l'], o

# problem 7
a = 1
b = 2

b, a = a, b
print(a, b)

# problem 8
((x, y), z) = ((1, 2), 3)