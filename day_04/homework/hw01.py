#  6) მომხმარებელს input ის საშუალებით შემოატანინეთ სახელი შემდეგ კი პროგრამა მას მიესალმოს 

fullname = input("enter your name and lastname: ").capitalize().strip()

first, last = fullname.split()

print(f"Hello, {first}")