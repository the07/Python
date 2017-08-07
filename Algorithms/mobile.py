phone_numbers = []

for _ in range(int(input())):

    S = input()
    phone_numbers.append(S[-10:])

for i in sorted(phone_numbers):
    print('+91 {} {}'.format(i[:5], i[5:]))
