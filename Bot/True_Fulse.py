described = False



def mes ():
    global described
    if not described:
        print('Правда')
        described = False
        if not described:
            print('Правда')
        else:
            print('не Правда')


mes()