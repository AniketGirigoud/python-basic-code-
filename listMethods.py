# list = [1 , 2 , 3 , "ani", "lion" ]
# print(list)
lists = [12 , 14, 13, 11, 15]
print(lists.sort())
print(lists.sort(reverse=True))
print(lists.reverse())
print(lists.append(18))
print(lists.count(3))
print(lists.insert(2, 1000))


n = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
lists.extend(n)
print(lists)

k = lists + n 
print(k)


m = lists.copy()
print(m)