def addminmuldiv(a, b):
    return a + b, a - b, a * b, a / b

# a, b, c, d = addminmuldiv(4, 5)
#
# print(a, b, c, d)

# 튜플, 배열이랑 비슷하다.
a = addminmuldiv(4, 5)
print(a[0])