# if , else , elif 



password = input("enter your password: " )
repeat_password = input("enter your again password: ")

def user_password(firstpassword,lastpassword):
    if firstpassword != lastpassword:
        print("your password is incorrect")
    else: 
        print("good!")
    

user_password(password,repeat_password)





age = int(input("enter your age: "))


def user_age(asaki):
    if asaki >= 18:
        print("you are srulwlovan")
    elif asaki < 6:
        print("you are kindergarden student")
    else: 
        print("you are not srulwlovan")

user_age(age)





score = int(input("enter your score: "))

def user_score():

    if score >= 90 and score <= 100:
        print("Grade A")
    elif score >=80  and score < 90:
        print("Grade B")
    elif score >= 70 and score < 80:
        print("Grade C")
    elif score >= 60 and score < 70:
        print("Grade D")
    else:
        print("azrze arxar vafshe imena")


user_score()





xelfasi = int(input("sheiyvane amtvis xelfasi: "))



def user_xellfasi():
    if xelfasi >= 1200 and xelfasi <= 1300:
        print("shen iyide gaming laptop")
    elif xelfasi >= 1100 and xelfasi < 1200:
        print("shen iyide HP laptop")
    elif xelfasi >= 1000 and xelfasi < 1100:
        print("shen iyide lenovo laptop")
    elif xelfasi >= 900 and xelfasi < 1000:
        print("shen iyide plansheti")
    else:
        print("veferi veriyide puri mainc weige saxshi rom shian bagnebs")


user_xellfasi()







