N, D = map(int, input().split())
forecast = list(map(int, input().split()))
for _ in range(D):
    answer = -1
    desired_profit = int(input())
    for i in range(N):
        buy_value = forecast[i]
        for j in range(i+1, N):
            sell_value = forecast[j]
            if sell_value - buy_value == desired_profit:
                if answer == -1:
                    answer = (i,j)
                else:
                    diff = answer[1] - answer[0]
                    curr_diff = j - i
                    if curr_diff < diff:
                        answer = (i,j)
    answer = (answer[0]+1, answer[1]+1)
    print(*answer)                    
