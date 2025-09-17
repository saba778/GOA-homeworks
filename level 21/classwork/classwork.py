# 1) კომენტარეის სახით ახსენით რას ნიშნავს immutable და mutable.
# mutable არის მონაცემი რომლის წევრი შეიძლება შეცვალო გარედან, მაგალითად list არის mutable.
# immutable არის მონაცემი რომლის წევრის გარედან შეცვლა არ შეიძლება, მაგალითად string.

# 2) შექმენით სია 10 ელემენტით და შემდგომ ჩაანაცვლეთ მეხუთე ელემენტი "goa"-თი.

x=[1,2,3,4,5,6,7,8,9,10]
x[4]= "goa"
print(x)

# 3) შექმენით ცვლადი სადაც მომხმარებელი შეინახავს რიცხვს, შემდეგ მომხმაერებელს შემოატანინეთ რიცხვი, სანამ მომხმარებელი არ გამოიცნობს თქვენს შენახულ რიცხვს გამოიტანეთ: "არასწორია თავიდან ცადე" და თავიდან შემოატანინეთ input, თუ გამოიცნობს გამოიტანეთ: "შენ გამოიცანი რიცხვი".


number = 5

number2 = int(input('type a number from 1-10:'))
while number2 != number:
    print("არასწორია თავიდან ცადე")
    number2 = int(input('type a number from 1-10:'))
print("შენ გამოიცანი რიცხვი")


# 4) გაამარტივეთ და კომენტარის სახით დაწერეთ რას გამოიტანს ქვემოთ მოეცემული კოდი:
#print(True and False or False or True and (False and False) or (True and True) or (False or True) or False or True and False) ეს კოდი არ გაუშვათ.

# ჯერ and უნდა გამოვთვალოთ
# print(false or false or false or true or true or false or false)
# საბოლლო პასუხი არის true