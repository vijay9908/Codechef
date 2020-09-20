a, b = map(int, input().split())
a, b = max(a, b), min(a, b)
a = a % b

print(a, b)
