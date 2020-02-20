with open('Test1.txt', 'r') as file:
    File = file.read().split()
File = (sorted(File, key = len, reverse = False))
print("Oi 5 megaliteres lekseis sto keimeno")
for i in range(-1,-6,-1):
    print(File[i])
print("\n")
print("Oi 5 megaliteres lekseis xoris fonienta sto keimeno")

for i in range(-1,-6,-1):
    File[i] = (File[i].replace('a', ''))
    File[i] = (File[i].replace('e', ''))
    File[i] = (File[i].replace('i', ''))
    File[i] = (File[i].replace('o', ''))
    File[i] = (File[i].replace('u', ''))
    File[i] = (File[i].replace('y', ''))
    print (File[i])
