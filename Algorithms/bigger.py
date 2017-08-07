## Input a string, output the next lexicographically larger string

def nextPermutation(a):
    i = len(a) - 1
    while i > 0 and a[i - 1] >= a[i]:
        i = i - 1
    if i <= 0:
        return False

    j = len(a) - 1
    while (a[j] <= a[i-1]):
        j = j - 1

    a[i-1], a[j] = a[j], a[i-1]
    string1 = a[:i]
    string2 = a[i:]
    string2.reverse()

    a = string1 + string2

    return a

if __name__ == "__main__":

    t = int(input())
    while t > 0:

        s = list(str(input()))
        y = nextPermutation(s)
        if y:
            print (''.join(y))
        else:
            print ('no answer')

        t = t - 1        
