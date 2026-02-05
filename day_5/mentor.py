# if - თუ 

# > - მეტობა 
# < - ნაკლებობა 
# <= - ნაკლებია ან ტოლი 
# >= - მეტია ან ტოლი 
# == - მკაცრი ტოლობა 
# != - არ ტოლია

age = int(input("enter your age: "))

if age >= 18 :
    print("shen xar srulwlovani !")

if age < 18:
    print("shen ar xar srulwlovani !")

# def - ფუნქციის გასაღები 

def nika():
    
    print("მივიდეს ონკანთან ")
    print("მოუშვას ონკანი")
    print("დაასხას წყალიი")
    print("მომიტანოს მე ოთახში")

nika()

print("hello")


name = input("enter your name: ")


def user_name(to = "usaxelo"):
    print(f"hello {to}!")


user_name(name)
