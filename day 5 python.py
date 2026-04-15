# Grading code Using Conditional Statements
'''marks = int(input())
if marks <= 100 and marks >= 90 :
    print('Grade A')
elif marks <= 89 and marks >= 80:
    print('Grade B')
elif marks <= 79 and marks >= 60:
    print('Grade C')
elif marks <= 69 and marks >= 40:
    print('Grade D')
elif marks > 101:
    print('Invalid')
elif marks <0 :
    print('Negative Value')
else:
    print('Fail')'''


# Check weather given Number is Positive odd/even and Negative odd/even

n = int(input())
if n>0 and n%2 == 0:
    print('Positive Even')
elif n<0 and n%2==0:
    print('Negative Even')
elif n<0 and n%2==1:
    print('Negavtive Odd')
else:
    print('Positive Odd')
