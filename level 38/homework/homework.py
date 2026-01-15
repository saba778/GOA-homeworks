# 2)შექმენით 5 ელემენტიანი Tuple და unpacking ის გამოყენებით თითოეულ ელემენტს მიანიჭეთ შესაბამისი ცვლადი
 
n1 = ('saba','gega','emir')
friend1,friend2,friend3 = n1

n2 = ('cow','dog','cat')
animal1,animal2,aminal3 = n2

n3 = ('georgia','france','australia')
a1,a2,a3 = n3

n4 = ('maths','georgian','english')
l1,l2,l3 = n4

n5 = ('water','bleach','soul')
y1,y2,y3 = n5

# 3)ახსენით კომენტარებით რა არის tuple და რით განსხვავდება ის list ისგან
# tuple და list ერთმანეთს გავნენ იმით რომ ორივენი ინახავენ რამოდენიმე სხვა რამეს,იმით განსხვავდებიან რომ tuple გარედან ვერ შეცვლი

# 4)შექმენით 6 ელემენტიანი tuple და გამოიყენეთ .index() და .count() მეთოდები

tup = ('random','fyban','giliw','maybe','iutlebsaf','worth')

print(tup.count())
print(tup.index(3))

# 5) კომენტარებით ახსენით რა არის *rest
# rest გამოიყენება რომ როცა unpacking-ს იყენებ რომ თუ არ გინდა დარჩენი ელემენტებს მიანიჭო ცვლადი შეგიძლია rest გამოიყენო