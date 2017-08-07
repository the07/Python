def validate(S):

    try:
        is_valid = True
        username, follow = S.split('@')
        domain, extension = follow.split('.')
        allowed = ['-','_']
        if len(extension) > 3:
            is_valid = False
        if not domain.isalnum():
            is_valid = False
        if username == '':
            is_valid = False
        for i in username:
            if not (i.isalnum() or i in allowed):
                is_valid = False
        return is_valid
    except ValueError:
        is_valid = False

N = int(input())
valid_email = []
while N > 0:
    N = N - 1
    S = input()
    if validate(S):
        valid_email.append(S)

print(sorted(valid_email))
