# 1).join() — შექმენი სია სახელებით და შეაერთე ისინი ერთ სტრიქონად მძიმით გამოყოფილი ფორმატით, შემდეგ დაბეჭდე ტექსტი „გუნდის წევრები: ...“.
list = ['saba','gega','luka','ivi']
print("გუნდის წევრები: " + ','.join(list))

# 2).split() — მომხმარებლისგან მიიღე წინადადება და დაშალე სიტყვებად; დაბეჭდე რამდენი სიტყვაა ტექსტში.
sentance = 'hello my name is saba'
print(len(sentance.split(' ')))

# 3).isupper() — შექმენი ფუნქცია, რომელიც შეამოწმებს, არის თუ არა შეყვანილი პაროლი მხოლოდ დიდი ასოებით დაწერილი.

def inspect(word):
    if word.isupper() == True:
        print('correct')
    else:
        print('incorrect')
    return word
password = 'HELLO'
print(inspect(password))

# 4).islower() — შეამოწმე, შეიცავს თუ არა ტექსტი მხოლოდ პატარა ასოებს, და თუ არა — დაბეჭდე „ტექსტი შერეულია“.

text = 'helloWORLD'

if text.islower() == True:
    print('all lower')
else:
    print('ტექსტი შერეულია')

# 5).swapcase() — მომხმარებლის მიერ შეყვანილ წინადადებაში შეცვალე ასოების რეგისტრი და დაბეჭდე ახალი ვარიანტი.

words = input('enter sentance:')
print(words.swapcase())

# 6).strip() — მიიღე სტრიქონი, რომელსაც ორივე მხარეს აქვს გამოტოვებები ან ტირეები, მოაშორე ისინი და დაბეჭდე გასუფთავებული ტექსტი.

WORd = '  __   hello    ___ '

print(WORd.strip(' _'))
# 7).count() — მიიღე ტექსტი და დაითვალე, რამდენჯერ გვხვდება მასში ასო "ა". დაბეჭდე შედეგი.

WOrd = 'გამარჯობა'
print(WOrd.count('ა'))

# 8).append() — შექმენი ცარიელი სია და for ციკლის საშუალებით დაამატე მასში 1-დან 10-მდე რიცხვები.

LISt = []
for i in range(1,11):
    LISt.append(i)
    print(LISt)

# 9)for loop + list — დაწერე ციკლი, რომელიც დაბეჭდავს მხოლოდ ლუწ რიცხვებს სიიდან და დაამატე ისინი ახალ სიაში.

num1 = [1,2,3,4,5,6,7,8,9]
total3 = []
for i in range(len(num1)):
    if i % 2 == 0:
        total3.append(i)
    
print(total3)

# 10)split - join: მომხმარებლისგან მიიღე წინადადება. დაშალე სიტყვებად (split), დათვალე რამდენი სიტყვაა, შემდეგ თითოეული სიტყვის პირველი ასო გადააქციე დიდად,
# შემდეგ შეაერთე ისევ (join) და დაბეჭდე შედეგი (წინადადება და სიტყვების რაოდენობა)“

sentance123 = input('enter a sentance: ')
wordssplit = sentance123.split()
amountwords = sentance123.len()
newsentance = []
for i in wordssplit:
    newsentance.append(i.capitalize())


