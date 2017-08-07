#take a word and remove all the vowels and capitalise the first word

state_names = ['Alabama', 'California', 'Oklahoma', 'Florida']
vowels = ['a','e','i','o','u']

for state in state_names:
    state_list = list(state)
    for letter in state_list:
        if letter.lower() in vowels:
            state_list.remove(letter)
    state_names[state_names.index(state)] = (''.join(state_list)).capitalize()

print (state_names)
