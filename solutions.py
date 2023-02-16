#VARIABLES
'''Question 1: 
Ask the user for the radius of a circle and then print the area'''
radius = int(input('Enter the radius of the circle:\n>> '))
pi = 3.142
area = pi * radius ** 2
print('You entered',radius,'the radius of the circle is',int(area))

'''Question 2:
Convert Fahrenheit to celsius'''
far = int(input('please input the temperature in fahrenheit: ')) 
celsius = int((far - 32) *5/9)
print(far,'degrees fahrenheit in celsius is', celsius, 'degree celsius')

'''Question 3:
Obtain the sum of two integers'''
num_1 = int(input('please enter first number: '))
num_2 = int(input('please enter second number: '))
print ('the sum of '+str(num_1) + ' and ' + str(num_2) + ' is ' + str(num_1+num_2) )

'''Question 4:
Obtain the product of two integers'''
num_1 = int(input('please enter the first integer number: '))
num_2 = int(input('please enter the second integer number: '))
product = (num_1*num_2)
print('the product of ', num_1, 'and', num_2, 'is',product)

'''Question 5:
Bob, Ann, Jane and Ashwin want to order pizza - they know they will each eat 4
slices of pizza. The local pizza shop sells pizzas of only 6 slices. What is the 
minimum number of pizzas needed - Use floor division'''
total_slices = 4 * 4
no_of_pizzas = (total_slices + 5)//6
slices_left = no_of_pizzas *6 - total_slices
print ('number of pizzas required is', no_of_pizzas,'there will be', slices_left, 'slices left')

#CONDITIONAL STATEMENTS
'''Question 6:
Write code that asks the user to input a number between 1 and 5 inclusive.
The code will take the integer value and print the string value. So for example, if the
user inputs 2 the code will print two. Reject any input that is not a number in that range.'''
user_input = input('please enter a number between 1-5: ')
while not user_input.isdigit():
    print('Wrong input. Try again')
    user_input = input('please enter a number between 1-5: ')
user_input = int(user_input)
if user_input == 1:
    print ('one')
elif user_input == 2:
    print ('two')
elif user_input == 3:
    print ('three')
elif user_input == 4:
    print ('four')
elif user_input == 5:
    print ('five')
else:
    print ('entry is out of range')

'''Question 7:
Repeat the previous task but this time the user will input a string and
the code will output the integer value. Convert the string to lowercase first.'''
user_input = input('please enter a string between one to five: ')
user_input = user_input.lower()
if user_input == 'one':
    print (1)
elif user_input == 'two':
    print (2)
elif user_input == 'three':
    print (3)
elif user_input == 'four':
    print (4)
elif user_input == 'five':
    print (5)
else:
    print ('entry is out of range')

'''Question 8:
Create a variable containing an integer between 1 and 10 inclusive. Ask the
user to guess the number. If they guess too high or too low, tell them they
have not won. Tell them they win if they guess the correct number.'''
number = 7
user_input = input('Guess the number between 1-10: ')
if user_input.isdigit():
    user_input = int(user_input)
    if user_input == number:
        print ('You guessed correctly! You win!')
    elif user_input > number and user_input <= 10:
        print ('you guessed too high! Sorry you lose!')
    elif user_input < number and user_input >= 1:
        print ('you guessed too low! Sorry you Lose!')
    else:
        print ('Out of Range!')
else:
    print ('That\'s not even a number! What are you doing??')

'''Question 9:
Ask the user to input their name. Check the length of the name. If it is
greater than 5 characters long, write a message telling them how many characters
otherwise write a message saying the length of their name is a secret.'''
name = input('Please enter your name:> ')
len_name = len(name)
if len_name > 5:
    print ('Your name is', len_name, 'characters long.')
else:
    print ('I\'m not telling you the length of your name!')

'''Question 10:
Ask the user for two integers between 1 and 20. If they are both greater than
15 return their product. If only one is greater than 15 return their sum, if
neither are greater than 15 return zero.'''
input_1 = int(input('Please enter an integer between 1 and 20: '))
input_2 = int(input('Please enter another integer between 1 and 20: '))
product = input_1 * input_2
addition = input_1 + input_2 
if input_1 > 15 and input_2 > 15:
    print (product)
elif input_1 > 15 or input_2 > 15:
    print (addition)
else:
    print (0)

'''Question 11:
Ask the user for two integers, then swap the contents of the variables. So if
var_1 = 1 and var_2 = 2 initially, once the code has run var_1 should equal 2
and var_2 should equal 1.'''
var_1 = int(input('Please enter first integer: '))
var_2 = int(input('Please enter second integer: '))
print ('Before swapping var_1 =', var_1, 'and var_2 =', var_2)
var_1,var_2 = var_2,var_1
print ('After swapping var_1 =', var_1, 'and var_2 =', var_2 )

#LOOPS
'''Question 12:
Ask the user for two numbers between 1 and 100. Then count from the
lower number to the higher number. Print the results to the screen.'''
num_1 = int(input('Please enter a number between 1 and 100:> '))
num_2 = int(input('Please enter a number between 1 and 100:> '))

while num_1 < 1 or num_2 < 1 or num_1 > 100 or num_2 > 100 or num_1 == num_2:
    print('Numbers must be of different values between 1 and 100. Try again!')
    num_1 = int(input('Please enter a number between 1 and 100:> '))
    num_2 = int(input('Please enter a number between 1 and 100:> '))
print()
if num_1 < num_2:
    for i in range(num_1,num_2+1):
        print(i,end=' ')
else:
    for i in range(num_2,num_1+1):
        print(i,end=' ')

'''Question 13:
Ask the user to input a string and then print it out to the screen in
reverse order (use a for loop).'''
word = input('Please enter a word: ')
reverse_string = ''
for char in word:
    reverse_string = char + reverse_string
print (reverse_string)

'''Alternatively, we can also do it this way'''
print(word[::-1])

'''Question 14:
Ask the user for a number between 1 and 12 and then display a times
table for that number.'''
user_input = input('Please enter a number between 1 and 12:> ')
while (not user_input.isdigit()) or (int(user_input) < 1 or int(user_input) > 12):
    print('Must be an integer between 1 and 12!')
    user_input = input('Please make a selection:> ')
print()
user_input = int(user_input)
print(f'This is the {user_input} Times Table')
print('=========================')
print()
for i in range(1,13):
    print(f'{user_input} x {i} = {user_input * i}')

'''Question 15:
Can you amend the solution to question 3 so that it just prints out all
times tables between 1 and 12? (no  need to ask user for input).'''
for i in range(1,13):
    print('===============================')
    print()
    print(f'This is the {i} times table')
    print()
    for j in range(1,13):
        print(f'{i} x {j} = {j*i}')

'''Question 16:
Ask the user to input a sequence of numbers. Then calculate the mean
and print the result.'''
user_input = input('Please enter a number. Type exit to stop:> ')
numbers = []
while user_input.lower() != 'exit':
    while not user_input.isdigit():
        print('That is not a number! Numbers only please.')
        user_input = input('Try again:> ')
    numbers.append(int(user_input))
    user_input = input('Please enter next number:> ')
total =  0
for num in numbers:
    total += num 
print(f'Mean is {total/len(numbers)}')
print ('Mean is', sum(numbers)/len(numbers))

'''Question 17:
Write code that will calculate 15 factorial. (factorial is product of
positive ints up to a given number. e.g 5 factorial is 5x4x3x2x1).'''
n = 15
fact = 1
for i in range (1, n+1):
    fact = fact * i
print (fact)

'''Question 18:
Write code to calculate Fibonacci numbers. Create list containing
first 20 Fibonacci numbers, (Fib  numbers made by sum of preceeding
two. Series starts 0 1 1 2 3 5 8 13 ....)'''
#Number of fib numbers required
n = 20

#set a and b to the first two numbers in the sequence
a = 0
b = 1

#List in which to store the numbers
fib_nums = []

#Use a for loop to create the sequence, repeat n times
for i in range(n):
    fib_nums.append(a)
    a,b = b,a+b
print (f'The first {n} Fibonacci numbers are; {fib_nums}')

'''Question 19:

     *****
     *
     ****
     *
     *
     *
Can you draw this using python? (comment the solution code)'''
#We've got 6 rows and 5 columns. And then we use a nested for loop. For i in range 1 to 7 
#should give us the rows and for j in range 1 to 6 should give us the columns.
star = '*'
for i in range(1,7):
    for j in range(1,6):
        if i == 1 and j < 6:
            print(star,end='')
        elif i == 2 and j == 1:
            print()
            print(star)
        elif i == 3 and j < 5:
            print(star,end='')
        elif i == 4 and j == 1:
            print()
            print(star)
        elif i == 5 and j == 1:
            print(star)
        elif i == 6 and j == 1:
            print(star)

'''Question 20:
Write some code that will determine all odd and even numbers
between 1 and 100. Put the odds in a list named odd and the evens
in a list named even.'''
# Numbers required
n = 100

# Instantiate empty lists
evens = []
odds = []
# Using a for loop
for i in range(n+1):
    if not i % 2:
        evens.append(i)
    else:
        odds.append(i)
print(f'The evens are {evens}')
print()
print(f'The odds are {odds}')

#DICTIONARIES
'''Question 21:
Can you remember how to check if a key exists in a dictionary?
Using the capitals dictionary below write some code to ask the user to input
a country, then check to see if that country is in the dictionary and if it is
print the capital. If not tell the user it's not there.'''

capitals = {'France':'Paris','Spain':'Madrid','United Kingdom':'London',
            'India':'New Delhi','United States':'Washington DC','Italy':'Rome',
            'Denmark':'Copenhagen','Germany':'Berlin','Greece':'Athens',
            'Bulgaria':'Sofia','Ireland':'Dublin','Mexico':'Mexico City'}

user_input = input('Which country would you like to check?:> ')

user_input = user_input.lower()

while 'united kingdom' not in user_input and not user_input.isalpha():
    if user_input == 'united states':
        break
    print ('You must enter a string!')
    user_input = input('Which country would you like to check?:> ')
    
user_input = user_input.title()
if user_input in capitals:
    print (f'The capital of {user_input} is {capitals[user_input]}')
else:
    print('No data available!')

'''Question 22:
Write python code that will create a dictionary containing key, value pairs
that represent the first 12 values of the Fibonacci sequence
i.e {1:0,2:1,3:1,4:2,5:3,6:5,7:8 etc}'''
n = 12
a = 0
b = 1
d = dict()
for i in range(1,n+1):
    d[i] = a
    a,b = b, a+b
print(d)

'''Question 23:
Create a dictionary to represent the open, high, low, close share price data
for 4 imaginary companies. 'Python DS', 'PythonSoft', 'Pythazon' and 'Pybook'
the 4 sets of data are [12.87, 13.23, 11.42, 13.10],[23.54,25.76,21.87,22.33],
[98.99,102.34,97.21,100.065],[203.63,207.54,202.43,205.24]'''
companies = ['Python DS', 'PythonSoft', 'Pythazon', 'Pybook']
key_names = ['Open', 'High', 'Low', 'Close']
prices = [[12.87, 13.23, 11.42, 13.10],[23.54,25.76,21.87,22.33],
[98.99,102.34,97.21,100.065],[203.63,207.54,202.43,205.24]]

d_1 = {}
for i in range(len(key_names)):
    d_1[companies[i]] = dict(zip(key_names,prices[i]))
print(d_1)

'''Question 24:
Go to the python module web page and find a module that you like. Play with it,
read the documentation and try to implement it.'''
import datetime
today = datetime.date.today()
print(f"Today's date is {today}")
holiday = datetime.date(2020,12,25)
delta = holiday - today
print()
print(f"Just {delta.days} days until the holidays!")

'''Question 25:
Create a dictoinary containing as keys the letters from A-Z, the values should
be random numbers created from the random module.'''
import random
keys = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
d = dict()
for letter in keys:
    d[letter] = random.randint(1,100)
print(d)

'''Question 26:
Create a dictionary containing 4 suits of 13 cards
['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']'''
suits = ['Spades','Clubs','Hearts','Diamonds']
rank = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
deck = dict()
for i in suits:
    deck[i] = rank    
print(deck)

#FILES AND FUNCTIONS QUESTIONS

'''Question 27:
Create a function that will calculate the sum of two numbers. Call it sum_two.'''
def sum_two(a,b):
    '''This function returns the function of two numbers'''
    return a + b
print(f'The sum of 3 and 4 is sum is {sum_two(3,4)}')
print()

'''Question 28:
Write a function that performs multiplication of two arguments. By default the
function should multiply the first argument by 2. Call it multiply.'''
def multiply(a,b=2):
    '''Returns the produc of a and b. if b is not given, returns two'''    
    return a * b
print(f'Inputting 3 gives {multiply(3)}')
print(f'Inputting 3 and 5 gives {multiply(3,5)}')

'''Question 29:
Write a function to calculate a to the power of b. If b is not given
its default value should be 2. Call it power.'''
def power(a,b=2):
    '''Returns a ** b, if b is not given, it will return a**2'''    
    return a ** b
print(f'Inputting 8 gives {power(8)}')
print(f'Inputting 2 and 8 gives {power(2,8)}')

'''Question 30:
Create a new file called capitals.txt , store the names of five capital cities
in the file on the same line.'''
file = open('capitals.txt','w')
file.write('London, ')
file.write('Accra, ')
file.write('Washington DC, ')
file.write('Abuja, ')
file.write('Paris.')
file.close()

'''Question 31:
Write some code that requests the user to input another capital city.
Add that city to the list of cities in capitals. Then print the file to
the screen.'''
user_input = input('Please enter a capital city:> ')
file = open('capitals.txt','a')
file.write('\n' + user_input)
file.close()
file = open('capitals.txt','r')
print(file.read())
file.close() 

'''Question 32:
Write a function that will copy the contents of one file to a new file.'''
def copy_file(infile, outfile):
    '''Copies content of infile to a newfile, outfile'''
    
    with open(infile) as file_1:
        with open(outfile,'w') as file_2:
            file_2.write(file_1.read())
copy_file('capitals.txt','new_capitals.txt')
