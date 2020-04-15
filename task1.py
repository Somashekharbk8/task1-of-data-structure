#create empty list
a = []

b = [5,6,8,9]
a.append(8)
a.append(9)
a.append(1)
a.append(5)
a.append(6)
a.append(7)
a.append(8)


c = a+b
count = c.count(8)
print(c)
print(count)

#find the avg

a = [8, 9, 1, 5, 6, 7, 8, 5, 6, 8, 9]
n = int(len(a)//2)
avg = sum(a)/n
#print(n)
print(avg)
print(sum(a))
print(min(a))
print(max(a))

mean = sum(a)/len(a)
print(mean)

#median
a.sort()
median = a[len(a)//2]
print(median)

#remove the Duplicates
a = [8, 9, 1, 5, 6, 7, 8, 5, 6, 8, 9]
a = tuple(set(a))
print(a)


