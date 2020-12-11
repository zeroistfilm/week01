num1 = input()
num2 = input()
 
num_list1 = list(map(int, str(num1)))[::-1]
num_list2 = list(map(int, str(num2)))[::-1]

total = 0
 
for i in range(0, len(num_list1)):
    sum = 0
    for j in range(0,len(num_list2)):
        result = num_list2[i]* num_list1[j] * pow(10,j)
        sum = sum + result
    total += sum * pow(10,i)

