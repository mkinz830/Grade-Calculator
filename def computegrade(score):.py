#creating or declaring the variable 'score'
#you are setting the value to the input

def computegrade(scr):
    x = 'Error'
    if scr >= 0.9:
        x = 'A'
    elif scr >= 0.8:
        x='B'
    elif scr >= 0.7:
        x='C'
    elif scr >= 0.6:
        x='D'

    elif scr < .6:
        x ='F'
    else:
        x ="Out of Range"
    print (x)