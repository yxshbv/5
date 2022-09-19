s = str( input () )
a = list(s.split(' '))
b = []
ind = 0
for i in a:
    b.append(int(i))

max = b[0]
for i in b:
    if i > max:
        max = i
        ind = b.index(i)
b.append(0)
b[-1] = b[0]
b[0] = b[ind]
b[ind] = b[-1]
b.pop()
print(b)
