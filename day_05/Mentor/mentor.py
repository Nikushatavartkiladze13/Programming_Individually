# round() - პითონში გამოიყენება რიცხვის დამრგვალებისთვის 

num1 = 5
num2 = 4

z = round(num1 / num2)

print(z)

# float - არის წერტილოვანი რიცხვი არის რიცხვი ათწილადების სახით, მაგ 1.25 , 1.83 აშ.

user_num = float(input("enter your number: ")) # float() მომხმარებლის შეყვანილ რიცხვს გადააქცევს ათწილადად

print(user_num)


# int() - მომხმარებლის შეყვანილ რიცხვს გადააქცევს მთელ რიცხვად 

number_1 = int(input("enter your number: "))
number_2 = int(input("enter your number: "))

sum = number_1 + number_2

print(f"{sum:,}") # ეს ფორმატირების მეთოდი გამოყოფს ათასებს მაგალითად 1000 -> 1,000