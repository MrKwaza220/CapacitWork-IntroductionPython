a_comp = complex(4, 8) # defines a_comp complex number
i1 = 5
i2 = 6
b_comp = complex(i1, i2) #complex(5, 6)

print (a_comp.real) #first numbwe which is 4
print (a_comp.imag) #second number which is 8

print(abs(a_comp)) #sqrt(a_comp.real**2 + a_comp.imag**2)
print(a_comp + b_comp) # adds a_comp complex number to a  prints the total
print(7+5j + 10+4j)  # adds 7 + 10 and 5 + 4 separately

print("\n +++++++++++++++++EXAMPLE++++++++++++++++++++ \n")
import cmath
#Initializing real numbers
x = 5
y = 3

z = complex(x, y)

#printing real numbers and imaginary part of complex number
print("The real part of complex number is : ", end="")
print(z.real)

print("The imaginary part of complex number is : ", end="")
print(z.imag)

