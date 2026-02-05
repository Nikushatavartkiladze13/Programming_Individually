# float - წერტილოვანი რიცხვი ანუ ათწილადი მაგალითად 1.5 , 2.3;


number_1 = float(input("enter your number: "))
number_2 = float(input("enter your number: "))


# round() - ფუნქციით ჩვენ შევძელით რომ მიღებული შედეგი დაგვემრგვალებინა უახლოეს მთელ რიცხვამდე 
sum = round(number_1 + number_2)

# მაგ : 5 + 5 = 10

print(f"{number_1} + {number_2} = {sum}")