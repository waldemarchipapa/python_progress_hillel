number = int(input("Enter number:"))

number_1=number//10000
number_2=number//1000%10
number_3=number%10000//100%10
number_4=number%100//10
number_5=number%10

result = number_5 * 10000 + number_4 * 1000 + number_3 * 100 + number_2 * 10 + number_1
print(result)






