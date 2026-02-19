def main():
    x = int(input("enter your x: "))
    if is_even(x):
        print("x is Even")
    else:
        print("x is Odd")


def is_even(n):
    
    if n % 2 == 0:
        return True
    else: 
        return False
    

main()


def main_1():
    age = int(input("enter your age: "))
    if asaki(age):
        print("srulwlovani xar")
    else:
        print("arasrulwlovani xar")


def asaki(n):
    if n >= 18:
        return True
    else:
        return False
    
main_1()

