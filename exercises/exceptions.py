'''
Created on Oct 2, 2018

@author: craciunv
'''

"""
for i in ['a', 'b', 'c']:
    try:
        print(i**2)
    except TypeError:
        print('Wrong input type for the pow operation! Please try again.')
"""     
       
"""
x = 5
y = 0

try:
    z = x/y
except ZeroDivisionError:
    print('You cannot divide by 0. Please choose a different number!')
finally:
    print('All done!')
"""
    
    
def ask():
    
    while True:
        
        try:
            user_input = int(input('Please insert number: '))
            result = user_input ** 2
        except:
            print("Invalid value inserted!")
            continue
        else:
            print('Square root is {}'.format(result))
            break
        finally:
            print('Square root operation finished.')
            
ask()
            