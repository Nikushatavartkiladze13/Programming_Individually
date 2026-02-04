# split 

name = input("enter your password ; email ; FirstName : ").strip()

password,email,firstname = name.split(" ")

firstname = firstname.title()

print(f"Hello your password email and name is {password}, {email}, {firstname}")

# int()


number_1 = 50 
number_2 = 30 



print(number_1 + number_2)
print(number_1 - number_2)
print(number_1 * number_2)
print(number_1 // number_2)



user_number = int(input("enter your first number: "))
user_number_2 = int(input("enter your second number: "))


print(user_number + user_number_2)


