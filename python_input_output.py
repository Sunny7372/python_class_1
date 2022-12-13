# declare & assign variables in python
int_var =18
float_var = 18.25
string_var ='ineuron batch2' # or another way "ineuron batch2"
bool_var = True # if we want to assign false then it should be like False


# Function in python for display output
# Function does what ? they might or might not accept some parameter
print(" Hello world ")

# print variable values in python
print(" value of int_var = ", int_var)
print("value of float_var =",float_var)

# how to check the data type of  any variable
# we can use type() function
print(" type of int_var ?",type(int_var))
print(type(float_var))

# how to do the type casting
# int(), float(), str(), bool()
int_var = int_var + 10 # int_var = 18 + 10
casted_int_var = float(int_var)
print(casted_int_var)
# how to take the inputs in python
# we can use input() function
name = input(" enter the name of user")
age = input(" enter the age of user")
print("user name =",name)
print(" user age =",age)