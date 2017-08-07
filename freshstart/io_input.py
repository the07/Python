def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

forbidden = ('!', '?', '.', ',', ' ')
something = input('Enter text:').lower()
for i in forbidden:
    if i in something:
        something = something.replace(i, '')
print(something)
if is_palindrome(something):
    print('yes')
else:
    print('No')
