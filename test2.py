s = str ( input () )
a = list(s.split(' '))
min_abs = abs(float(a [0]))
for i in a:
    if abs(float(i)) < min_abs:
        min_abs = abs(float(i))
ind = 0
for i in a:
    if float(i) < 0:
        ind = a.index(i)
        break
x = 0
for i in a:
    if int(i) > 0:
        a.remove(i)
    elif int(i) < 0:
        a.remove(i)
        break
sum_abs = 0
for i in a:
    sum_abs += abs(float(i))
print (min_abs)
print (sum_abs)
print (a)
print (ind)
