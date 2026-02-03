
# int - integer - მთელი რიცხვი   
# int()
# user_age_1 = int(input("enter your age: "))
# user_age_2 = int(input("enter your age: "))


# print(user_age_1 + user_age_2)



# number_1 = 20 
# number_2 = 40 

# print(number_1 + number_2)
# print(number_1 - number_2)
# print(number_1 * number_2)
# print(number_2 // number_1) 




# split 


user_information = input("enter your Name and Lastname; Email; Password: ")


name,lastname,email,password = user_information.split(" ")

name = name.title()
lastname = lastname.title()

print(f"hello your name is {name} {lastname} your email {email} your password is {password}")













