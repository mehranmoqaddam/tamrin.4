import random
n = int(input("tedade adad random : "))
list1 = []
#list1 = adade ba tekrar
for i in range(n):
    r = (random.randint(0,100))
    list1.append(r)
list2 = set(list1)
#list2 = adade beedune tekrar
print("liste ba tekrar " , list1)
print("liste bi tekrar " , list2)

