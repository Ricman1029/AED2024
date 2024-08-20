n = 5
a = n * [0]
for i in range(n):
    a[i] = i + 1

print(a)

v = n * [0]
for i in range(n):
    v[a[i]] = a[i]