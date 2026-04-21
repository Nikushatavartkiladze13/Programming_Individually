# dollars_to_float - ფუნქციამ უნდა მიიღოს str ტიპის მნიშვნელობა როგორც არგუმენტი და ფორმატირებული ამ მაგალითის მიხედვით $##.## სადაც ყოველი # ნიშანი რიცხვს წარმოადგენს. უნდა წაუშალოს დოლარის ნიშანი $ და დააბრუნოს მნიშნველობა როგორც float რიცხვი. ასე მაგალითად - თუ გადავეცით $50.00, ფუნქციამ უნდა დააბრუნოს 50.0
# percent_to_float - ფუნქციამ უნდა მიიღოს str ტიპის მნიშვნელობა როგორც არგუმენტი და ფორმატირებული ამ მაგალითის მიხედვით ##% სადაც ყოველი # ნიშანი რიცხვს წარმოადგენს. უნდა წაუშალოს პროცენტის ნიშანი % და დააბრუნოს მნიშნველობა როგორც float რიცხვი. ასე მაგალითად - თუ გადავეცით 15%, ფუნქციამ უნდა პროცენტული მაჩვენებელის float ვერსია - ანუ 0.15.
def main():
    dollars = input("How much was the meal? ")  
    percent = input("What percentage would you like to tip? ") 

    d = dollars_to_float(dollars)
    p = percent_to_float(percent)

    tip = d * p
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    return float(d.replace("$", ""))


def percent_to_float(p):
    return float(p.replace("%", "")) / 100


main()