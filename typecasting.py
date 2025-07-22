 #simple typecasting
a = "2"
b = "5"
print(int(a) + int(b))

#Explicit typecasting no 1 
number = 17
float = 9.9
string_number = int(number)
sum= float + string_number
print("The sum of both the number is:", sum)

# explicit typecasting no 2 
string = "28"
number = 9
string_number = int(string)
sum = number + string_number
print("The sum of both the number is:", sum) 

#implicit typecasting 
a = 9 
b = 8.9
c = a+b 
print(c)