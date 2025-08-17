# 1) კომენტარის სახით ახსენით რა განსხვავებაა  while loop-სა და for loop-ს შორის.
# while loop-ი გამოიყენება როდესაც არ იცი რამდენჯერ უნდა გაიმეოროს კოდმა ერთი და იგივე რამე.გამალითად რაიმე გაიმეოროს სანამ ერთი მონაცემი არ დაემთხვება სახვას
# for loop-ი გამოიყენება როდესაც გინდა რომ მაგალითად 5-დან 23-მდე გამოითვალო რამდენი კენტი რიცხვია
# 2) for loop-ის დახმარებით გამოიტანეთ ყველა ლუწი რიცხვი 10-დან 50-მდე.
for i in range(10,50,2):
    print(i)

# 3) while loop-ის დახმარებით გამოიტანეთ ყველა კენტი რიცხვი 0-დან 20-მდე.
for i in range(1,20,2):
    print(i)

# 4) მომხმარებელს შემოატანინეთ რაიმე სიტყვა და ამ სიტყვას for loop-ით გადაუარეთ, გამოიტანეთ ამ სიტყვის ყველა ასო.
print("enter your name")
word = input()
for i in word:
    print(i)

# 5) მომხმარებელს შემოატანინეთ თავისი ასაკი, თუ მისი ასაკი ნაკლებია 18-ზე გამოიტანეთ "you are a child", თუ ტოლია 18-ის გამოიტანეთ
#  "you just became an adult", ხოლო დანარჩენ შემთხვევებში გამოიტანეთ "you are an adult". გამოიყენეთ if/else.
print("enter your age")
age = int(input())
if (age > 18):
    print('your are fully grown')

elif (age == 18):
    print('you just became fully grown')
elif (age < 18):
    print('you are not fully grown')





1