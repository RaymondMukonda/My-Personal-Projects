user = False

while not user:
    name = input('Please enter your name: ')
    surname = input('Please enter your surname: ')

    if surname.isalpha() and name.isalpha():
        user = True
    else:
        print('Please enter letters only: ')

    print(f'welcome {name} {surname}, its great having you abord: ')