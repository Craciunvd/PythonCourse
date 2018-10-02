'''
Created on Sep 25, 2018

@author: craciunv
'''
from __builtin__ import str

def square(num):
    return num**2

my_nums = [1,2,3,4,5]

my_list = list(map(square,my_nums))

print(my_list)

square = lambda num: num**2

print(square(5))

def vol(rad):
    
    return 4/3 * 3.14 * rad ** 3

print('Volume of sphere with radius 3 is '+str(vol(3)))

def ran_check(num,low,high):
    
    if num >= low and num <= high:
        print('Number is in interval ['+str(low)+","+str(high)+"]" )
    else:
        print('Number is not in interval ['+str(low)+","+str(high)+"]" )
        
print(ran_check(4, 5, 9))

def ran_bol(num,low,high):
    
    return num >= low and num <= high

print(ran_bol(7, 5, 9))

def up_low(s):
    
    upper_letters = 0
    lower_letters = 0
    
    for letter in s:
        if letter.isupper():
            upper_letters += 1
        elif letter.islower():
            lower_letters += 1
        else: pass
            
    print('Upper letters: '+str(upper_letters)+' lower letters: '+str(lower_letters))
    
print(up_low('aaa AAAA 1'))

def unique_list(l):
    
    return list(set(l))

print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))
    
def multiply(numbers):
    
    mul_num = 1
    
    for number in numbers:
        
        mul_num *= number
        
    return mul_num

print(multiply([1,2,3,-4]))

def palindrome(s):
    
    return s == s[::-1]

print(palindrome('helleh'))

import string

def ispanagram(str1, alphabet= string.ascii_lowercase):
    
    for letter in alphabet:
        
        if letter not in str1:
            return False
        
    return True

print(ispanagram("The quick brown fox jumps over the lazy dog"))





























