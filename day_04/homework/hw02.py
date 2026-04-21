#  მომხმარებელს შემოატანინეთ სახელი შემდეგ გვარი და ტერმინალში დაბეჭდეთ მისი სრული სახელი და გვარი მოახდინეთ მათი კონკატინაცია 

first_name = input("enter your name: ").title().strip()
last_name = input("enter your lastname: ").title().strip()

print(first_name + " " + last_name)