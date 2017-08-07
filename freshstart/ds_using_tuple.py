zoo = ('python', 'elephant', 'penguin')
print('Number of animals in the zoo is', len(zoo))

new_zoo = 'monkey', 'camel', zoo
print('Number of cages in new zoo is', len(new_zoo))
print('Animals in new zoo are', new_zoo)
print('Items brought from old zoo are ', new_zoo[2])
print('Last animal brough from the zoo is', new_zoo[2][2])

for items in new_zoo:
    print(items)
