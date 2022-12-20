user_input = int(input())
rooms = list(map(int, input().split(" ")))
captain_no = 0
groups = {}
for room_no in rooms:
    if room_no in groups:
        groups[room_no] +=1
    else:
        groups[room_no] = 1
for room_no in groups:
    if groups[room_no] == 1:
        captain_no = room_no

print(captain_no)
