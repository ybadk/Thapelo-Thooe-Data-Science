
list1 = [1, 2, 3]
list2 = [4, 5, 6]

res_lst = []

for i in range(0, len(list1)):
    res_lst.append(list2[i]+list1[i])
print(res_lst)

