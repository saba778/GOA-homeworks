# 1)შედარების ოპერაციებზე გააკეთეთ 10-10 მაგალითი თოთოეულ მაგალითს კომენტარის სახით მიუწერეთ რას დააბრუნებს ჩვენი კოდი
#true
print(10>9)
print(10>8)
print(10>7)
print(10>6)
print(10>5)
print(10>4)
print(10>3)
print(10>2)
print(10>1)
print(10>0)
#false
print(10<9)
print(10<8)
print(10<7)
print(10<6)
print(10<5)
print(10<4)
print(10<3)
print(10<2)
print(10<1)
print(10<0)
# 2)კომენტარის სახით ახსენით რა არის boolean'ი
# boolean არის მონაცემთა ტიპი რომელიც მხოლოდ არის true და false

# 3)რას ნიშნავს კომპიუტერის ენაზე 1 და 0 
# 1 ნიშნავს true-ს და 0 არის false-ი

# 4)კომენტარის სახით ახსენით and oპერატორი
# and ოპერატორს როცა იყენებ ყველაფერი true and true-ს გარდა ყველაფერი გამოვა false (true and false,false and false,false and true)

# 5)კომენტარის სახით ახსენით or ოპერატორი
# or ოპერატორი არის როგორც and ოპერატორი მაგრამ შებრუნებული, ყველაფერი არის true (false or false-ის გარდა)

# 6)and oპერატორის გამოყენებით დაწერეთ 10 მაგალითი თითოეულს გვერდით კომენტარის სახით დაუწერეთ თუ რას გამოიტანს იქამდე სანამ კონსოლში გაუშვებთ
True and False #false
False and True #false
False and False #false
True and True #true
print((2>1) and False) #false
print((1<9) and True) #true

# 7)or oპერატორის გამოყენებით დაწერეთ 10 მაგალითი თითოეულს გვერდით კომენტარის სახით მიუწერეთ თუ რას გამოიტანს ეს კოდი იქამდე სანამ კონსოლში გამოიძახებთ
True or False #true
False or True #true
False or False #false
True or True #true
print((2>1) or False) #true
print((1<9) or True) #true

# 8) შედარების და ლოგიკური ოპერაციები გააერთიანეთ და მათზეც გააკეთეთ 5 მაგალითი
print(5 == 3)#false
print(10 == 10)#true
print(9 == 98)#false
print(50 == 2)#false
print(3 == 0) #false
# 9) 9) შექმენით ცვლადი რომელშიც შეინახავთ თქვენთვის სასურველ რიცხვს შემდეგ ამ ცვლადის მნიშვნელობა გაზარდეთ 
# 10'ით პრინტით გამოიძახეთ ეს ცვლადი და მოახდინეთ მასზე შედარების ოპერაცია ისე რომ გამოიტანოს True
num = 10
num2 = num + 10
print(num2 > 2)

# 10)შექმენით ცვლადი temperature სადაც შეინახავთ 30 გრადუსს თუ 30 გრადუსზე მეტი იქნება რაიმე რიცხვი გამოიტანეთ  True 
temp = 30
print(temp < 31)
