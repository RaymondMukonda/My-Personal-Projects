people = [
    {
        'name': 'Rammy', 
        'number': '+06711057'

    },
    {
        'name': 'Mike', 
        'number': '+036711057'

    },
    {
        'name': 'Miyon',
        'number': '+076711057'

    }
]

name = input('Please enter your name: ')

for person in people:
    if person['name'] == name:
        number = person['number']
        print(f'{name} Number was found {number}')
        break
    else:
        print('not found')
        break