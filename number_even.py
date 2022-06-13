#A four-digit integer is given. Find the number of even digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Print the number of even digits in the variable "var_int".
var_int= 4352
k=var_int%10
z=(var_int//10)%10
y=(var_int//100)%10
w=var_int//1000
sum=((k+1)%2+(z+1)%2+(y+1)%2+(w+1)%2)
print(sum)
