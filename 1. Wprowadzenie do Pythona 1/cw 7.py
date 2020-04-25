a = list(range(1, 11))
b = a[5:10]
a = a[0:5]

a = a + b
a.insert(0, 0)

c = a
c.reverse()
print(c)