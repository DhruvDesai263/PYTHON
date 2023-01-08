
#A) Found which grade student will get based on SGPA.


def Grade(s):##grade counting function
    if s>=9:
        print('Grade is AA')
    elif s>=8:
        print('Grade is AB')
    elif s>=7:
        print('Grade is BB')
    elif s>=6:
        print('Grade is BC')
    elif s>=5:
        print('Grade is CC')
    elif s>=4:
        print('Grade is DD')
    else:
        print('Grade is FF')
SGPA = float(input("Enter the value which you want to count SGPA: "))
Grade(SGPA)#function call

#B) Find max from three numbers
        

def max(a,b,c):
    if a>b and a>c:
        print({a},  'is greater')
    elif b>c and b>a:
        print({b} ,'is greater')
    elif c>a and c>b:
        print({c} ,'is greater')
    else:
        print('equal')

#C) Calculate number of Uppercase and lowercase letters of string given by user

def ul(s):
    count1=0
    count2=0;
    for i in s:
        if ord(i)>=65 and ord(i)<=99:
            count1 = count1 + 1
        else:
            count2 = count2 + 1
    print('UC',count1)
    print('LC',count2)
    
#D) Find a Square of a given list using lambda function
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def sq(nums):
    square_nums = list(map(lambda x: x ** 2, nums))
    print(square_nums)
sq(nums)

n = int(input("Enter any Number  :"));
def table(n):
    for i in range(1,11):
     value = n * i
     print(n," * ",i," = ",value)

table(n)

#E) Enter value from user and print multiplication table

c = int(input())
sum=0
def su():
    sum=0
    list8 = []
    for i in range (0,6):
        print("enter element")
        c = int(input())
        list8.insert(i, c)
        sum += c
    print(sum)   
su()     

#F) Create a list by user given value and make sum of it using loop
Even = [i for i in range(1,51) if i%2==0]

print(Even)

Odd = [i for i in range(1,51) if i%2!=0]

print(Odd)


A = [i for i in range(1,101) if i%5==0]
print(A)