n = int(input().strip())
scores = [int(scores_temp) for scores_temp in input().strip().split(' ')]
m = int(input().strip())
alice = [int(alice_temp) for alice_temp in input().strip().split(' ')]

scores = sorted(list(set(scores)))[::-1]
back = len(scores) - 1
for a in alice:
    while back >= 0 and a > scores[back]:
        back -= 1
    if scores[back] == a:
        print(back + 1)
    else:
        print(back + 2)