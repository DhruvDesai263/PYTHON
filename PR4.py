#A) Found which grade student will get based on SGPA.

print('A---------------------')
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
print('B---------------------')       
x=int(input('enter your number'))
y=int(input('enter your number'))
z=int(input('enter your number'))
def max(a,b,c):
    if a>b and a>c:
        print({a}, 'is greater')
    elif b>c and b>a:
        print({b} ,'is greater')
    elif c>a and c>b:
        print({c} ,'is greater')
    else:
        print('equal')
max(x,y,z)

#C) Calculate number of Uppercase and lowercase letters of string given by user
print('C---------------------')
def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test('The quick Brown Fox')    
#D) Find a Square of a given list using lambda function
print('D---------------------')
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
print('E---------------------')
number = int(input ("Enter the number of which the user wants to print the multiplication table: "))      
# We are using "for loop" to iterate the multiplication 10 times       
print ("The Multiplication Table of: ", number)    
for count in range(1, 11):      
   print (number, 'x', count, '=', number * count)   

#F) Create a list by user given value and make sum of it using loop
print('F---------------------')
def sum_of_list(l):
  total = 0
  for val in l:
    total = total + val
  return total

my_list = [1,3,5,2,4]
print ("The sum of my_list is", sum_of_list(my_list))

#G Use comprehension method

#Create a two separate list of even and odd numbers from 1 to 50
# Python program to count Even
# and Odd numbers in a List

# list of numbers
print('G1---------------------')
list1 = [10, 21, 4, 45, 66, 93, 1]

even_count, odd_count = 0, 0

# iterating each number in list
for num in list1:

	# checking condition
	if num % 2 == 0:
		even_count += 1

	else:
		odd_count += 1

print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)

#Get value which are divided by 5 from 1 to 100.
print('G2---------------------')
multiplesof5=[] 
for i in range(1, 101): 
    if i%5==0: 
        multiplesof5.append(i) 
print(multiplesof5) 
