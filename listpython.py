# list = [1 , 2 , 3 , 4 , ]
# print(list)
# name = ["an", "lion", "tiger", 1, 2, 3,]
# print(name)
# print(len(name))
# print(name[2])
# print(name[1:4])
# print(name[2:len(name)-2])


# ##
# if "lion" in name:
#     print("yes")
# else:
#     print("No")

##
# if 2 in list:
#     print("yes")
# else:
#     print("No")

# ##
# if "tig" in name:
#     print("Yes")
# else:
#     print("No")

# print(name[1:4:2])

############################list comprehenssion
lists = [i for i in range(5)]
print(lists)
lis = [i for i in range(20) if i%2 ==0 ]
print(lis)
liste = [i*i for i in range(10)]
print(liste)