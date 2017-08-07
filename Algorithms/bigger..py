t = int(input())

while t > 0:
    s = list(str(input()))

    i = len(s) - 1
    while i > 0:
        if s[i] > s[i-1] and i > 1:
            s[i], s[i-1] = s[i-1], s[i]
            r = s[i:]
            r.sort()
            s = s[:max(1,i)]
            s = s + r
            print (''.join(s))
            break
        elif s[i] > s[i-1] and i == 1:
            new_val = s[0]
            s.sort()
            first_val = s[s.index(new_val)+1]
            s.pop(s.index(first_val))
            s.insert(0, first_val)
            print (''.join(s))
            break
        i = i - 1
    if i == 0:
        print ('no answer')
    t = t - 1
