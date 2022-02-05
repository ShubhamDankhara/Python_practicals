# Find runner-up from given list 
# D21CS108
# Shubham Dankhara

n = int(input())
score = map(int, input().split())
print(sorted(list(set(score)))[-2])
