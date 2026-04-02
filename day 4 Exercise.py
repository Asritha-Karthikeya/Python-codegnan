#Checking num is Zero or Non-Zero
N= int(input())
if N == 0:
    print("Zero")
else:
    print("Non-Zero")


#Checking num Positive or negative
Num = int(input())
if Num >= 0:
    print("Positive")
else:
    print("Negative")


#Check num is Even or Odd
num = int(input())
if num %2 ==0:
    print("Even")
else:
    print("odd")


#Check the person is eligible for vote or not
Age = int(input())
if Age >= 18:
    print("Eligible")
else:
    print("Not Eligible")


#Check number is divisible with 3 0r not
Val = int(input())
if Val % 3 == 0:
    print("Divisible")
else:
    print("Not Divisible")


#Check number divisible with 3 & 5 or not
val = int(input())
if val % 3 ==0 and val%5 ==0:
    print("Yes")
else:
    print("No")
    

#Finding Bigger num among 2
A = int(input())
B = int(input())
if A > B:
    print(A,"is Highest")
else:
    print(B,"is Highest")
