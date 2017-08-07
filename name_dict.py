from operator import itemgetter

people = []
for _ in range(int(input())):

    *name, age, gender = input().split()
    people.append([name, age, gender])

for i in sorted(people, key = itemgetter(1)):
    if i[2] == 'M':
        print('Mr. {}'.format(' '.join(i[0])))
    else:
        print('Ms. {}'.format(' '.join(i[0])))
