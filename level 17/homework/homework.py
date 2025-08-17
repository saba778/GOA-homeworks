# 1) კომენტარის სახით ახსენით რაში გვჭირდება elif.
#  elif გალიყენება როდესაც ორ შედეგზე უფრო მეტი შედეგია. როდესაც ორი შედეგი არის გამოიყენება if და else. მაგალითად ტო ადამიანი 18 ჭელზე დიდია 10%
#  10% ფასდაკლებას  აძლევ,თუ ნაკლები 5%,თუ ზუსტად 18-ია 15%.

# 2) for loop-ის გამოყენებით გამოიტანეთ ყველა კენტი რიცხვი 20-დან 100-მდე.
for i in range(20,101):
    if i % 2  != 0:
        print(i)


# 3) შექმენით password ცვლადი სადაც შეინახავთ რაიმე პაროლს, შემდეგ მომხმარებელს შემოატანინეთ პაროლი,
#  სანამ  პაროლები არ დაემთხვევა გამოიტანეთ: "incorrect password" და თავიდან შემოაყვანინეთ პაროლი. , ხოლო თუ
#   დაემთხვევა გამოიტანეთ: "password is correct".  გამოიყენეთ  while loop  და if/elif/else.

password = "Rip_d"
print('enter password')
password1 = input()
if (password != password1):
    print("incorrect password")
elif (password == password1):
    print("password is correct")




# 4) while loop-ის დახმარებით გამოიტანეთ ყველა ლუწი რიცხვი 100-დან 20-მდე.

number = 100

while (number != 20):
    print(number)
    number = number - 2
