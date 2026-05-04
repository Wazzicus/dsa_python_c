import random
list = random.sample(range(10), 5)
print(list)
print(list[2:])
print(list[:3])

list.append(5)
list.append(6)
list.append(7)
list.append(8)
print(list)
print(list[:])
list_a = list[-1]
print(list_a)