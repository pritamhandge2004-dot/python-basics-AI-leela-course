# String variable
greeting = "Hello world!"
print(greeting)
print(type(greeting))

# Numeric variables
integer_num = 5
float_num = 5.5
print(type(integer_num))
print(type(float_num))

# Boolean variable
truth_value = True
print(type(truth_value))

# Print values
print(integer_num)
print(float_num)
print(truth_value)

# Mathematical operations
number1 = 10
number2 = 3
print(number1, number2)
print(type(number1), type(number2))

sum_result = number1 + number2
print(sum_result)

print(number1 - number2)
print(number1 * number2)
print(number2 / number1)
print(number2 // number1)
print(number2 % number1)

print(type(number2/number1))

# Decimal operations
decimal1 = 4.2
decimal2 = 1.2
print(decimal1 + decimal2)
print(decimal1 - decimal2)

# Mixed operations
first_num = 6
second_num = 2.5
print(first_num + second_num)

# User input
name = input('Enter your first name: ')
print(name)
print(type(name))

text = input('Enter some text    ->')
print(text.upper())
print(text.title())
print(text.find('e'))
print(text.count('e'))
print(text.replace('e','z'))
print(len(text))

# Numeric operations
num1 = 4
num2 = 6
print(num1, num2)
print(type(num1), type(num2))

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num2 / num1)
print(num2 // num1)
print(num2 % num1)
print(4 ** 3)

print(12 // 4)
print(11 // 4)
print(10 // 4)
print(9 // 4)

print(12 % 4)
print(11 % 4)
print(10 % 4)
print(9 % 4)

print(6 * 5 + 2)
print(2 + 6 * 5)
print(6 * (5 + 2))

# Comparison operations
print(3 == 3)
print(3 == 2)
print(4 != 2)
print(4 > 3)
print(4 < 3)
print(4 >= 4)
print(4 >= 3)
print(4 <= 3)

# Assignment operations
value = 5
print(value)

value += 2
print(value)

value = 5
value -= 2
print(value)

value = 5
value *= 3
print(value)

value = 5
value /= 2
print(value)

# Logical operations
print(True and True)
print(True and False)
print(False and False)

print(True or True)
print(True or False)
print(False or False)

print(not True)
print(not False)

var = 6
print(var > 5 and var < 7)

var = 6
print(var > 4 or var < 5)

var = 6
print(not(var > 4 and var < 10))

print(abs(-3))
print(abs(-3.2))

print(round(4.56))
print(round(-4.98))

print(round(4.567, 1))
print(round(4.567, 2))

print(round(4.578, 1))
print(round(4.578, 2))

# String concatenation
str_num1 = 'Hello'
str_num2 = '7'
print(str_num1 + str_num2)

# Decision structures
height = 180
if height < 145:
    print('too short')
elif height < 185:
    print('height is ok')
else:
    print('too tall')

subscription = False
if subscription:
    print('Thank you for the subscription!')
else:
    print('Please subscribe')

subscription = True
if subscription:
    print('Thank you for the subscription!')
else:
    print('Please subscribe')

# Nested if
x = 8
if x > 10:
    print('x is greater than 10')
    if x > 20:
        print('x is greater than 20')
        if x > 30:
            print('x is greater than 30')
        else:
            print('x is less than 30')
    else:
        print('x is less than 20')
else:
    print('x is less than 10')

x = int(input("Enter any number within range 10: "))
print(x >= 4 and x <= 10)

# List operations
courses = ['ba', 'bcom', 'bsc', 'ma', 'mcom', 'msc']
print(courses[2])

print(courses[1:5])
print(courses[-1])
print(courses[-2])
print(courses[-3:-1])
print(courses[-3:])

courses.append('BE')
print(courses)

courses.insert(3, 'ME')
print(courses)

new_course = 'B.Pharm'
courses.append(new_course)
print(courses)

new_list = ['11th', '12th']
courses.append(new_list)
print(courses)
print(courses[-1])

courses.extend(new_list)
print(courses)

courses.pop()
print(courses)

courses.remove('ba')
print(courses)

fruits = ['mango', 'apple', 'orange', 'kiwi', 'pineapple', 'papaya']
print(fruits)
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)

num_list = [15, 6, 3, 12, 2, 200]
print(num_list)
num_list.sort()
print(num_list)

# Length and other functions
countries = ['Russia', 'India', 'US', 'Japan', 'Germany', 'Italy', 'Zambia']
print(len(countries))
print(len('Hello'))

print(max(num_list))
print(min(num_list))
print(sum(num_list))

print(max(countries))
print(min(countries))

# Loop structures
for item in countries:
    print(item)

for item in countries:
    print(item, len(item))

for item in countries:
    print(f'{item}, {item.upper()}, {len(item)}')

for index, item in enumerate(countries):
    print(index, item)

cubes = []
for i in range(6):
    cubes.append(i ** 3)
print(cubes)

# Nested list
fruit_list = [['mango','apple','pineapple'], ['custard_apple', 'orange']]
print(fruit_list)
print(len(fruit_list))

print(fruit_list[0])
print(fruit_list[1])

print(fruit_list[0][0])
print(fruit_list[1][0])
print(fruit_list[0][2])

# Let's define one tuple by putting some data in round brackets. Separate data must be separated by comma. 

subjects = ('Math', 'Science', 'English', 'History')
print(subjects)
print(type(subjects))     # Note that we get class 'tuple' as output.
# To access data, just like list, simply pass index within []

print(subjects[2])    # Index 2 = Position 3
# If you type subjects. you'll get only two suggestions, meaning tuples has only two functions defined specifically for them. Let's explore them 
# Check the last two entries when you run help()

# help(tuple)  # Commented out to avoid long output
# count() - returns number of occurances of value
# Here 'Math' is used only once, hence output is 1

print(subjects.count('Math'))
print(subjects.count('Geography'))    # 'Geography' not part of subjects. Output = 0
#  index() - returns the first index of value
# English is defined at third position (second index)

print(subjects.index('English'))
# Simple example

university = {
  "name": "Stanford",              # this is called dictionary item. This dictionary has 3 items. 
  "founder": "Leland Stanford",
  "established": 1885
}
print(university)
print(type(university))
# To access specific dictionary item, call it using its key 

print(university['name'])
# To get length of dictionary

print(len(university))    # 3 items
# To change value of an item, just override the value as follows

university['name'] = 'STANFORD UNIVERSITY'
print(university)
# Add new item in dictionary

university['location'] = 'California'
print(university)
# dict supports lot of functions

# help(dict)  # Commented out to avoid long output
# Another way to get item

print(university.get('name'))   # get() is predefined function for dict 
print(university.get('foundation'))  # foundation is not defined, so we get None
# keys() and values() functions gives us all the keys and values

print(university.keys())
print(university.values())
# Let's add new key value pair to dictionary and see if we get the updated list with .key()

university['ranking'] = 5
print(university.keys())
print(university.values())
# TO delete an item, use pop

teacher = {
    'name' : 'Robert',
    'age' : 35,
    'subject' : 'Physics'
}

print(teacher)

teacher.pop('subject')    # use pop function and pass key
print(teacher)
# del can also be used to delete an item

teacher = {
    'name' : 'Robert',
    'age' : 35,
    'subject' : 'Physics'
}

print(teacher)

del teacher['subject']     # syntax -> del dict_name['key']
print(teacher)
# clear() clears the dictionary without deleting the defined object. The dictionary just becomes empty (clear)

teacher = {
    'name' : 'Robert',
    'age' : 35,
    'subject' : 'Physics'
}

print(teacher)
teacher.clear()
print(teacher)
# Let's first define dictionary in a different way

organization = dict({'name': 'Microsoft', 'year': 1975, 'founder': 'Bill Gates'})     # dict is special keyword, wrap your dictionary within dict() 

print(organization)
print(type(organization))
# simple for loop
for item in organization:              # this loops over only keys
  print(item)
# simple for loop
for item in organization:              # this loops over only keys
  print(item, organization[item])      # for each key, let's access its value with organization[keyname]
# Shorter way to do the same is to use .items() function

for key, value in organization.items():
  print(key, value)
# Loop through only keys

for key in organization.keys():
  print(key)
# Loop through only values

for value in organization.values():
  print(value)
# You can sort dictionary 

for key in sorted(organization):     # sorted() sorts all keys alphabetically
  print(key)

university = {
    'name': 'Harvard',
    'year': 1636,
    'departments': {
        'arts': 'Humanities',
        'science': 'Engineering'
    }
    }
print(university)
print(university['departments'])
print(university['departments']['arts'])
for item, val in university.items():
  print(item, val)
print(type(university['departments']))
# Let's define simple function

def greetings():                    
    print('Hello everyone!')

# this won't output anything, because we haven't called the function yet
greetings()   # the above defined function is now called. Hence the output
# Let's call the function twice

greetings()
greetings()
# Let's pass some argument to the function

def greetings(name):
  print(f'Hello {name}!')    # Note, the function body is limited by indentation. As long as it is there, it's a part of function body. 

greetings('David')
greetings(25)
print(type(greetings))          # function has a type 'function'
# Let's define a function that can carry out multiplication

def multiply(first, second):
  print(first * second)

multiply(5, 8)           # note that colab auto suggests the function name when you press ctrl + tab after writing first few letters

def welcome(name):
    return (f'Welcome {name.upper()}!')
print(welcome('Learners'))

def hello(name):    
    message = "Hello "+name  
    return message  

name = input("Enter your name: ")    
print(hello(name))

def subtract():  
    x = 50  
    y = 20  
    z = x - y  
    return z  

print("The difference is:", subtract())

def multiply(a,b):  
    return a * b

a = int(input("Enter a: "))    # will give error if you pass string here
b = int(input("Enter b: "))    
    
print("Product = ", multiply(a,b))

p = int(input("Enter the principal amount? "))    
r = float(input("Enter the rate of interest? "))     # sometimes interest rate could be in fraction like 8.5 or something, so float
t = int(input("Enter the time in years? "))

def compound_interest(p,t,r):    
    return p * (1 + r/100)**t

  
print("Compound Interest: ", compound_interest(p,t,r))    

# for values of 1000, 2, 10 --> interest = 210
# For readability, you can call function by writing the name of arguments

def find_volume(length, width, height):        
    print(length, width, height)
    return length * width * height

v = find_volume(length=10, width=5, height=3)    # like this. this is readable. This is called KEYWORD ARGUMENTS.
print(v)

v = find_volume(height=3, length=10, width=5)     # even if order is changed, no problem. This is called KEYWORD ARGUMENTS.
print(v)

v = find_volume(3,10,5)     # This is not the same as above (in this case, length=3, width=10, height=5)
print(v)
# An "if statement" is written by using the if keyword, followed by condition and then :

x = 100
y = 50
if x > y:
  print("x is greater than y")

# Python relies on indentation (whitespace at the beginning of a line) to define scope in the code.
# If statement, without indentation (will raise an error)

x = 100
y = 50
if x > y:
    print("x is greater than y")  # Fixed: added indentation

# We can find if number is positive, negative or zero.

n = int(input(" Enter a number to check:"))

if n > 0:
  print("It's a positive number.")
elif n < 0:  # Changed from if to elif for better logic
  print("It's a negative number.")
else:
  print("The number is zero.")

# Using If statement, we can find smallest number among three

x = int(input("Enter the Value of x: "))  
y = int(input("Enter the Value of y: "))  
z = int(input("Enter the Value of z: "))  

if x < y and x < z:  
    print("x is smallest input.")  
elif y < x and y < z:  
    print("y is smallest input.")  
else:  
    print("z is smallest input.")

# The else keyword catches anything which isn't caught by the preceding conditions.
# If the condition provided in the if statement is false, then the else statement will be executed.

a = 100
b = 150
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

marks = int(input("Enter your marks? "))  
if marks >= 40:  
    print("You have passed the exam!!")  
else:  
    print("Sorry! you have failed!!")

# Demonstration of elif
# elif is nothing but else if i.e. if you want to give condition to else block as well

num = 5
if num == 1:
  print('num is one')
elif num == 2:
  print('num is two')
elif num == 3:
  print('num is three')
elif num == 4:
  print('num is four')
elif num == 5:
  print('num is five')
else:
  print('num not found')

# Check whether the inputted number is 100, 200 or 300. 

number = int(input("Enter the number?  "))  

if number == 100:  
    print("The number you entered is: 100 ")  
elif number == 200:  
    print("The number you entered is: 200") 
elif number == 300:  
    print("The number you entered is: 300")
else:  
    print(" You have entered a random number other than 100, 200 and 300.")  

score = int(input("Enter the score? "))  

if score > 90 and score <= 100:  
   print("Excellent! You got grade A+ ...")  
elif score > 80 and score <= 90:  
   print("Very Good! You got grade A ...")  
elif score > 70 and score <= 80:  
   print("Good! You got grade B+ ...")  
elif score > 60 and score <= 70:  
   print("You got grade B ...")  
elif score > 50 and score <= 60:  
   print("You got grade C ...")  
else:  
   print("Sorry you need to improve!")  

# Nested If
# You can have if statements inside if statements, this is called nested if statements.

x = 65

if x > 50:
  print("Above fifty,")
  if x > 60:
    print("and also above sixty!")
  else:
    print("but not above sixty.")

# If you have only one statement to execute, you can put it on the same line as the if statement.
if x > y: 
    print("x is greater than y")

# If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:
a = 200
b = 150
print("A") if a > b else print("B")

# Use for loop to iterate through a list
fruits = ['apple', 'banana', 'cherry', 'date']

for fruit in fruits:
    print(fruit)

# Use for loop to iterate through a tuple
colors = ('red', 'green', 'blue', 'yellow')

for color in colors:
    print(color)

# Use for loop to iterate through a dictionary
car = {'brand': 'Toyota', 'model':'Camry', 'year': 2020}

for item in car:
    print(item, car[item])

# Use for loop to iterate through a string
text = 'Python'
for char in text:
  print(char)

# range() comes handy when using for loop

for i in range(7):   # prints from 0 to 6
  print(i)

print('------------')

for i in range(5,12):   # prints from 5 to 11
  print(i)

# Use enumerator for getting index

animals = ['cat', 'dog', 'elephant', 'giraffe']
for index, animal in enumerate(animals):
  print(index, animal)

# If you want index, but don't want to use enumerate, there is another way

animals = ['cat', 'dog', 'elephant', 'giraffe']

for i in range(len(animals)):                # range(4) prints a list of numbers from 0 to 3. Here we are passing length of list to the range.
  print(i, animals[i])

# we can use condition inside for loop
animals = ['cat', 'dog', 'elephant', 'giraffe']

for animal in animals:
    if animal == 'dog':
        print(animal)
    else:
        print('Not dog')

# if item is 'elephant', skip the current iteration but continue with the next

animals = ['cat', 'dog', 'elephant', 'giraffe']
for animal in animals:
  if animal == 'elephant':
    continue
  print(animal)

city = input('enter your city name --- ')
print("let's print characters separately")
for char in city:
  print(char)

# Let's write a function that calculates cube of each number
numbers = [1, 2, 3, 4, 5, 6, 7]

def cube(item):
  return item * item * item

for i in numbers:
  print(i, cube(i))

# This gives the average of the given list.

numbers = [20, 40, 60, 80, 100]  
total = 0  
for i in numbers:  
    total = total + i     # or we can write total += i
average = total / len(numbers)
print("The average is:", average)  

# This gives multiplication table of number n given by user input

num = int(input("Enter the number "))  
for i in range(1,16):  
    c = num * i  
    print(f"{num} x {i} ====> {c}") 

# For loop inside for loop

colors = ["red", "green", "blue"] #outer loop  
shapes = ["circle", "square", "triangle"] #inner loop 

for color in colors:
  for shape in shapes:
    print(color, shape)



# NESTED loop

for i in range(2,6): # outer loop
    for j in range(10, 13): # inner loop
        print(i, j)

# Prints a pattern using hash symbol

rows = int(input("Enter the rows  :"))    # e.g. 4
for i in range(0, rows+1):               # Outer loop will print number of rows   (+1 because range excludes the second number)
    for j in range(i):                   # Inner loop will print number of hash symbols  
        print("#", end='')               # print() can take different arguments, by default end='\n' i.e. new line
    print()                               # Once inner loop is finished, we want the control to come to the next line, hence blank print()

# Prints the alphabet pattern

# User input for number of rows  
rows = int(input("Enter the rows : "))  
# Outer loop will print number of rows  
for i in range(1, rows+1):  
    # Inner loop will print letters 
    for j in range(i):  
        print(chr(65 + j), end = '')  # chr(65) = 'A', chr(66) = 'B', etc.
    print()  

# How to check length of list if there was no len() function

items = [10, 20, 30, 40, 50]  
count = 0  
for item in items:  
    count = count + 1
print("Total length - ", count)

# Check for some integer and print its index position using count identifier.
# Here we are trying to find position of 40

items = [10, 20, 30, 40, 50]  
count = 0  
for item in items:  
    count = count + 1
    if item == 40:  
        print("Item found")  
        break
print("found at position", count)

# If letter is 'b' then say 'Found the letter' else print the letter

letters = ['a', 'b', 'c', 'd', 'e']
for letter in letters:
    if letter == 'b':
        print('Found the letter')
        break
    else:
        print(letter)

# while x is less than 8, keep printing
x = 2
while x < 8:        # syntax is similar to for or if loop. Starts with while, ends with :, indentation for the while-block
    print(x)
    x += 2          # means x = x + 2

# When the break statement is encountered, it brings control out of the loop.
# When we want to end the block at certain point, we use break statement.

x = 1
while x < 15:
    if x == 7:
        break
    print(x)
    x += 2

# To keep running while loop forever, use while True
# The following program will keep asking you for input, until you write 'exit'

while True:
    color = input('Input favorite color: ')
    if color == 'exit':
        break
    print("Your favorite color is:", color)

# When you encounter the letter 'o', stop. Till then continue.
i = 0  
str1 = 'Wonderful'  
  
while i < len(str1):   
    if str1[i] == 'o':   
        i += 1  
        break  
    print('Current Letter :', str1[i])   
    i += 1

class Person:            # We are defining a class named Person (class has to be in lowercase)
    name = "Alex"          # name and age are called attributes of the class 
    age = 30

person = Person()           # person is an object of class
print(type(person))                  # we can cross check the data type of person (ignore the __main__ in output, it represents the current file)

# Object of a class can access attributes of the class

print(person.name)    
print(person.age)

# Let's define one method 
# Method is also part of class, so it should have the indentation as well

class Person:            
    name = "Maria"          
    age = 28

    def say_hello(self):       # self is nothing but the object that is calling this function.   
      print("Hello there!")

person = Person()           
person.say_hello()                 # when this is called, the person object is passed as self above

# The above code is correct, but we'd like to pass name and age when we create object. 
# So this is how we'll modify the code

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    
    def display_info(self):
        print("Person Name: ",  self.name)
        print("Person Age: ", self.age)
 

person1 = Person("Michael", 32)         # creating object named person1  --> the arguments are passed to init() automatically, and person1 automatically gets name and age properties as passed
person2 = Person("Sarah", 29)         # creating object named person2  --> here also the arguments are passed to inti() without explicit calling

person1.display_info()
person2.display_info()

class Animal:
    def __init__(self, species):
        self.species = species         # the right side species is coming from the argument in the init(). While with the left side species we are defining a new property for the object and assigning value to that property with right side species

    def introduce(self):
        print('I am a', self.species)

    def change_species(self, species):
        self.species = species

lion = Animal('lion')

# access method
lion.introduce()

# access attribute
print(lion.species)

# change species
lion.change_species('African lion')
lion.introduce()

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        print(f"Radius - {self.radius}")
        return 3.14159 * self.radius * self.radius

circle1 = Circle(7)
print(circle1.area())

class Cat:
  def __init__(self, breed, age, color):
    self.breed = breed
    self.age = age
    self.color = color
  def info(self):
    print(f"Breed - {self.breed}, Age - {self.age} years, Color - {self.color} ")

cat1 = Cat('Persian', 3, 'White')

cat1.info()

import random
# Let's see what this module is about with help()

# help(random)  # Commented out to avoid long output
# so we got list of all the functions that are written/stored in this module. 
# let's try using randint

print(random.randint(1, 10))   # generates random integer between 1 and 10 inclusive

# But if you import randint() specifically, then you can access it just like that. 
# e.g.

from random import randint       # use ctrl + tab to get suggestions after import
print(randint(20, 30))                     # we can use randint() now because in the above line, we are explicitly importing randint() function

# Continuing ahead

print(random.choice(['apple', 'banana', 'cherry']))
print(random.random())  # random float between 0 and 1
print(random.uniform(5.0, 10.0))

from datetime import date
print(date.today())
today = date.today()
print(today)
print(today.day, today.month, today.year)       # ctrl+tab after today.

from datetime import datetime
print(datetime.now())         # This gives current date and time
print(datetime.now().strftime("%d-%m-%Y %H:%M:%S"))