import re


def check(txt):
    if (re.search("^[-+]?(0|[1-9])+[0-9]*$", txt)):
        return 'int'
    #elif (re.search("^([-+]?[0-9]+[\.]+|[-+]?[1-9]+[\.]{0,1})[0-9]+$", txt)):
    elif (re.search("^[-+]?[0-9]{1}[\.]{1}[0-9]+$", txt)):
        return 'float'
    else:
        return 'str'


input1 = input()
input2 = input()

def pow(input1,input2):

    if (check(input1) == 'int'):
        input1 = int(input1)
    elif (check(input1) == 'float'):
        input1 = float(input1)
    else:
        print('Write number!! input1')
        return False


    if (check(input2) == 'int'):
        input2 = int(input2)
    elif (check(input2) == 'float'):
        input2 = float(input2)
    else:
        print('Write number!! input2')
        return False

    print ((input1 + input2)**2)



pow(input1,input2)
