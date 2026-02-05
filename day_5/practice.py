
# შევქმენით ფუნქცია main() სადაც შევინახეთ ცვლადი name და მომხმარებელს შემოვატანინეთ თავისი პაროლი შემდეგ კი გამოვიძახეთ მთავარ ფუნქციაში ანუ main-ში  ქვემოთ დაწერილი ფუნქცია user_password() რასაც არგუმენტად გადავეცი მომხმარებლის შეყვანილი ინფორმაცია ამჯერად პაროლი 

def main():
    name = input("enter your password : ")
    user_password(name)

# შევქმენით ფუნქცია არგუმენტით password შემდეგ კი ამ ფუნქციაში print()-ით დავბეჭდეთ ტექსტი და მომხმარებლის მიერ შეყვანილი ინფორმაცია მაგრამ გავითვალისწინეთ ის შემთხვევა თუ user_password გამოძახებისას იქნება ცარიელი მაშინ პარამტერის ნაცვლად ტექსტში ჩაიწერება password -ის მნიშვნელობა 

def user_password(password = "2010"):
    print(f"Hello your password is {password}")

# გამოვიძახეთ მთავარი ფუნქცია 

main()



user_1 = int(input("enter your age: "))


def user_age(to):
    if to >= 18:
        print("shen xar srulwlovani !")
    if to < 18: 
        print("shen ar xar srulwlovvani !")

user_age(user_1)