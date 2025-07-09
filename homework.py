# 2) and და or ოპერატორზე გააკეთეთ 10-10 მაგალითი და თითოეული მაგალითი ახსენით კომენტარებით
#or
True or False #true
False or True #true
False or False #false
True or True #true
10==3 or 3-9==3 #false
20-12==8 or 22==1 #true
2334-321==2134 or 1==1 #true
11121+3331-3121==41 or 5==21 #false
44==44 or 32-34+2==0 #true
293==342 or 2334==3 # false
#and
True and False #false
False and False #false
False and True #false
True and True #true
1==3 and 3-42==4 #false
1-1==0 and 31-41==10 #false
32-31+9==10 and 9==19-10 #true
73==923 and False #false
True and 5==76-71 #true
True and 67==70-3 #true

# 3)შედარებით ოპერაციებზე გააკეთეთ თითოზე 10-10 მაგალითი და ესენიც ახსენით კომენტარის სახით
# or
print(1>3 or 4>3) #true. 1 false 1 true
print(4>9 or 4>9) #false. both false
print(3==3 or 9>1) # both true
print(2+9>10 or 4==3) #true. 1 true,1 false
print(3>9 or 3-9>2) #false, both false
print(499==9 or 78425>38) #false.both false
print(87+2-9>81 or 6>1) #true,1 true,1 false
print(382000000>21 or 76<212) # true,both true
print(0>3 or 9871-9871>3) #false,both false
print(31-333+333==444 or 1323>987) #true, 1 true,1 false
# and
print( 3>2 and 3<5) #true
print( 3213>23112 and 31<31) #false
print( 2390>2390 and 23-231<3123) #false
print( 938904>384988 and 243<5232) #true
print( 9843>423 and 4<5) #false
print( 8743>42 and 42444<44444444444444444444) #true
print( 312>54 and 76<87)#true
print( 98634>433 and 432<464)#true
print( 372>421 and 42<121) #false
print( 32<41 and 331<982) #true

# 4) შედარების და ლოგიკური ოპერატორებზე ორივეზე ერთად შეასრულეთ 10-10 მაგალითით და ესეც ახსენით კომენტარის სახით
# or
print(1+1>3 or 4>3) #true
print(4>9 or 4>9-3) #false
print(3==3 or 9>1+7) #true
print(2+9>10-3 or 4==3) #true
print(3>9+2 or 3-9>2) #true
print(499-31==9 or 8888-78425>38) #false
print(87+2-9>81 or 3+6>1) #true
print(382000000-6544444>21 or 76<212) #true
print(0>3-2 or 9871-9871>3) #false
print(31-333+333==444 or 1323>987-44) #true
# and
print(3>2 and 3<5) #true
print(3213>23112 and 31<31) #false
print(2390>2390 and 23-231<3123) #false
print(938904>384988 and 243<5232) #true
print(9843>423 and 4<5) #true
print(8743>42 and 42444<44444444444444444444-4444444444444) #true
print(312-54>54 and 76<87-10) #true
print(98634-54333>433 and 432<464) #true
print(372>421-29 and 42<121-33) #false
print(32<41-7 and 331<982-487) #true
