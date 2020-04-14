Result = 0
def Result_Int(Num):
    global Result
    if(Num > 0):
        Reminder = Num %10
        Result = (Result *10) + Reminder
        Result_Int(Num //10)
    return Result

t = int(input())
for _ in range(t):
    n = int(input())
    print(Result_Int(n))