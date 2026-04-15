# 1
a = int(input())
b = int(input())
print(a + b)

# 2

a = int(input())
b = int(input())
print( a // b)
print( a % b)

#3

n = int(input())
if n % 2 == 0:
    print("Even")
else:
    print("Odd")

#4
a = int(input())
b = int(input())
a = a + b
b = a - b
a = a - b
print(a, b)

#5
a = int(input())
b = int(input())
c = int(input())
if a >= b and a >= c:
    print(a)
elif  b >= c:
    print(b)
else:
    print(c)

#6

n = int(input())
print(n ** 2)


#7
a = int(input())
b = int(input())
if a % b == 0:
    print("Divisible")
else:
    print("Not Divisible")


#8

length = int(input())
breadth = int(input())
print(length * breadth)


#9

n = int(input())
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")


#10

a=int(input())
b=int(input())
if a==b:
    print('Equal')
else:
    print('Not Equal')

#11
a=int(input())
if a>=18:
    print('Eligible')
else:
    print('Not Eligible')


#12

num = int(input())
if num % 3 == 0 and num % 5 == 0:
    print("Multiple of both 3 and 5")
else:
    print("Not a multiple of both 3 and 5")

#13

a = int(input())
b = int(input())
c = int(input())
if a > b:
    if a > c:
        print( a)
    else:
        print( c)
else:
    if b > c:
        print(b)
    else:
        print(c)

#15
mark = int(input())
if mark<=100 and mark>=90 :
    print('A')
elif mark<90 and mark>=75:
    print('B')
elif mark <75 and mark >=50:
    print('C')
else:
    print('Fail")
          

#18
units = int(input())
bill = 0

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)
else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

print(bill)

#20
year = int(input())
if year%100==0:
    print('Centuary Year')
    if year% 400==0:
        print('Leap centuary Year')
    else:
        print('Not Leap Century Year')
else:
    print('Not Cenuary Year')

    
