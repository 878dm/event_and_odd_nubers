#A four-digit integer is given. Find the sum of odd digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Create a variable "sum_even" and assign it 0.

#Find the sum of the odd digits in the variable "var_int".
var_int= 4352
k=var_int%10
z=(var_int//10)%10
y=(var_int//100)%10
w=var_int//1000
sum_even=0
sum_even=k*(k%2)+z*(z%2)+y*(y%2)+w*(w%2)
print(sum_even)