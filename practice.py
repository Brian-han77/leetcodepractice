
array1 = list(s)
print(array1)
sum = 0
#calculate com   plicated stuff
for i in range (len(array1)-1):
    if array1[i] == 0:
        continue
    if array1[i]+array1[i+1] == "IV":
        sum = sum + 4
        array1[i] = "0"
        array1[i+1] = "0"

    if array1[i]+array1[i+1] == "IX":
        sum = sum + 9
        array1[i] = "0"
        array1[i+1] = "0"
    if array1[i]+array1[i+1] == "XL":
        sum = sum + 40
        array1[i] = "0"
        array1[i+1] = "0"
    if array1[i]+array1[i+1] == "XC":
        sum = sum + 90
        array1[i] = "0"
        array1[i+1] = "0"
    if array1[i]+array1[i+1] == "CD":
        sum = sum + 400
        array1[i] = "0"
        array1[i+1] = "0"
    if array1[i]+array1[i+1] == "CM":
        sum = sum + 900
        array1[i] = "0"
        array1[i+1] = "0"
    else:
        continue

print(array1)


for i in range (len(array1)):
    if array1[i] == "0":
        continue
    if array1[i] == "I":
        sum = sum + 1
    if array1[i] == "V":
        sum = sum +  5
    if array1[i]== "X":
        sum = sum +  10
    if array1[i] == "L":
        sum = sum +  50
    if array1[i] == "C":
        sum = sum +  100
    if array1[i] == "D":
        sum = sum +  500
    if array1[i] == "M":
        sum = sum +  1000

print(sum)