
ab = {
    'Gaurav': 'thegauravks@gmail.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}

print(ab['Gaurav'])

del ab['Spammer']

print(len(ab))

for key, value in ab.items():
    print(key, value)

ab['Guido'] = 'guido@python.org'

if 'Gaurav' in ab:
    print(ab['Gaurav'])
