#Starwind (ataraxygale)'s modulo calculator

#user inputs modulo a%b variables
def moduloInput():
    while True:
        try:
            # user input
            print('Enter a and b modulo values: \n')
            a = int(input('Enter value a: '))
            b = int(input('Enter value b: '))
            return a, b

        except ValueError:
            print('You need to enter an integer or float\n')

#manual break down of shortcut calculations for each modulo combination
#outputs a Live Check with standard a%b equation
# along with my manual shortcut calculations for clarity
def starwind_modulo():
    a, b = moduloInput()
    #if a is pos, b is pos and a >= b #checked
    if a > 0 and a > b and b > 0:
        print('Live check with a%b: ', a % b)
        moduloVal = a % b
        return f'Calculated by Starwind: {moduloVal}'
    #if a is pos, b is pos and a <= b #checked
    elif a > 0 and a < b and b > 0:
        print('Live check with a%b: ', a % b)
        moduloVal = a
        return f'Calculated by Starwind: {moduloVal}'
    #if a is pos, b is neg and a > abs(b)
    elif a > 0 and a > abs(b) and b < 0:
        print('Live check with a%b: ', a % b)
        moduloVal = a - a//b*b
        return f'Calculated by Starwind: {moduloVal}'
    #if a is pos, b is neg and a < abs(b)
    elif a > 0 and a < abs(b) and b < 0:
        print('Live check with a%b: ', a % b)
        moduloVal = b + a
        return f'Calculated by Starwind: {moduloVal}'
    #if a is neg, b is pos and abs(a) < b #checked
    elif a < 0 and abs(a) < b and b > 0:
        print('Live check with a%b: ', a % b)
        moduloVal = b + a
        return f'Calculated by Starwind: {moduloVal}'
    #if a is neg, b is pos and abs(a) > b #checked
    elif a < 0 and abs(a) > b and b > 0:
        print('Live check with a%b: ', a % b)
        moduloVal = b - (abs(a)%b)
        return f'Calculated by Starwind: {moduloVal}'
    #if a and b are equal (pos or neg) #checked
    elif a == b or a==0:
        print('Live check with a%b: ', a % b)
        moduloVal = 0
        return f'Calculated by Starwind: {moduloVal}'

#prompts user if they'd like to enter a new modulo combination or exit the program
def continueModulo():
    while True:
        print('\nWould you like to run another modulo?')
        inp = input('Enter y or n: ')
        print('')

        if inp.lower().strip() == 'y':
            print(starwind_modulo())
        elif inp.lower().strip() == 'n':
            print('Hope this was helpful! Thank you (•̀ᴗ•́)و')
            exit()
        else:
            print('Please enter y or n\n')


print(starwind_modulo())
continueModulo()


