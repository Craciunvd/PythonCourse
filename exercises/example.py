'''
Created on Sep 24, 2018

@author: craciunv
'''

mylist = [1,2,3]
mylist.pop()


def print_my_list(mylist):
    '''
    DOCSTRING: For documentation purposes
    INPUT:
    OUTPUT:
    '''
    print(mylist)
    
def say_hello(name='NAME'):
    print('hello '+name)

def add(n1,n2):
    return n1+n2

def dog_check(mystring):
    return 'dog' in mystring.lower()

def pig_latin(word):
    
    first_letter = word[0]
    
    #check if vowel
    if first_letter in 'aeiou':
        pig_word = word+'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'
    return pig_word

def myfunc(*args):
    
    return [x for x in args if x % 2 == 0]

def skyline(string):
    
    new_string = ''
    
    for index,letter in enumerate(string):
        if index % 2 == 0:
            new_string += letter.upper()
        else:
            new_string += letter.lower()
            
    return new_string
    
print_my_list(mylist)
say_hello('Vlad')
result = add(2, 3)
print('Result is '+str(result))
result = dog_check('My dog ran away')
print(str(result))
print(pig_latin('apple'))
print(pig_latin('word'))


print(myfunc(5,6,7,8))

print(skyline('Anthropomorphism'))











