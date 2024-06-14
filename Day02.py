#Palindrome check
word = input('Enter word')
if word == word[::-1]:
    print(word,'is palindrome')
else:
    print(word,'is not palindrome')


#FIzz Buzz

for i in range(1,101):
    if i%3==0 | i%5==0:
        print('FizzBuzz')
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else:
        print(i)


#Nth Fibonacci Number

first = 0 
second = 1
lst = []
num = int(input('Enter num'))
if num == 0:
    lst.append(0)
elif num == 1:
    lst.append([0,1])
else:
    for i in range(num):
        lst.append(first)
        first , second = second , first+second
    print(first)


#Prime Number Checker

num =  int(input('Enter number'))
flag = False
if num == 1:
    print('1 is not prime number')
elif num > 1 :
    for i in range(2,num):
        if num%i==0:
            flag = True
            break
    if flag:
        print(num,'is not a prime number')
    else:
        print(num,'is a prime number')        


#Guess the Number Game

import random
randnum = random.randint(1,100)
print(randnum)
while(True):
    guess =  int(input('Guess number'))
    if guess > randnum:
        print('Guess is greater than actual number')
    elif guess < randnum:
        print('Guess is smaller than actual number')
    elif guess == randnum:
        print('You did it. Number was ',randnum)
        break

    
#Guess the Number Game

import random
randnum = random.randint(1,100)
print(randnum)
while(True):
    guess =  int(input('Guess number'))
    if guess > randnum:
        print('Guess is greater than actual number')
    elif guess < randnum:
        print('Guess is smaller than actual number')
    elif guess == randnum:
        print('You did it. Number was ',randnum)
        break

#List Comprehension

lstcomprehension = [i*i for i in range(1,11)]
print(lstcomprehension)

#Palindrome Sentences
import re
sentence = input('Enter sentence')
sent = re.sub(r'[^a-zA-Z]',' ',sentence).lower
if sent == sent[::-1]:
    print('Sentence is Palindrome')
else:
    print('sentence is not palindrom')


#Anagram Checker

one = input('Enter first word')
two = input('Enter second word')

one = one.replace(" ","").lower()
two = two.replace(" ","").lower()
print(sorted(one))
print(sorted(two))
if sorted(one) == sorted(two):
    print('words are anagram')
else:
    print('words are not anagram')

#Reverse order sentence

sentence = input('Enter sentence \n')
sentence = sentence.split()
reverse = sentence[::-1]
print('reverse sentence is ', " ".join(reverse))
