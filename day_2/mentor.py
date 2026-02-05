sep = ""

name = input("enter your name: ")

print("Hello,", name, sep="")

# strip 

name = input("enter your name and surname: ")
name = name.strip()
# name = name.capitalize()
name = name.title()


print("Hello,",name)
