# Find Captain Room Number
# D21CS108
# Shubham Dankhara


k = int(input())
room_number = list(map(int, input().split()))
captain_room_number = (sum(set(room_number)) * k - sum(room_number))  // (k - 1)
print(captain_room_number)