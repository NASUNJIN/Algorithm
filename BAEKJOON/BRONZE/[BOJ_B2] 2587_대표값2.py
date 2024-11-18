list = [] 
for i in range(0, 5):
    list.append(int(input()))

list.sort()

hub = 0
for i in range(0, 5):
    hub = hub + list[i]

print(hub//5)
print(list[2])