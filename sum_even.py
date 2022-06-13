#A four-digit integer is given. Find the sum of even digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Create a variable "sum_even" and assign it 0.

#Find the sum of the even digits in the variable "var_int".
var_int= 4352
k=var_int%10
z=(var_int//10)%10
y=(var_int//100)%10
w=var_int//1000
sum_even=0
sum_even=k*((k-1)%2)+z*((z-1)%2)+y*((y-1)%2)+w*((w-1)%2)
print(sum_even)