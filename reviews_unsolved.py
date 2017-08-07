import time
import datetime

d = datetime.date(2016,6,15)
unixtime = time.mktime(d.timetuple())
e = datetime.date(2016,7,15)
unixtime2 = time.mktime(e.timetuple())

def calculate_score(timestamp, length):
    """Returns the score of a user"""

    score = 0
    if unixtime < timestamp < unixtime2:
        score += 20
    else:
        score += 10

    if length > 100:
        score += 20
    else:
        score += 10

    return score


n, m = map(int, input().split())
passions = []
while n > 0:
    n = n - 1
    passions.append(str(input()).lower())
N = 2 * m
reviews = {}
while m > 0:
    m = m - 1
    ID, rdate = map(int, input().split())
    review = str(input()).lower()
    reviews[ID] = [rdate, review]

passion_review = []

score = 0
answer = '-1'
for j in passions:
    for i in reviews:
        if j in reviews[i][1]:
            curr_score = calculate_score(reviews[i][0], len(reviews[i][1]))
            if curr_score > score:
                score = curr_score
                answer = i
            elif curr_score == score:
                if answer > i and answer != '-1':
                    answer = i
    passion_review.append(answer)

print(passion_review)
