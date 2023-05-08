class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()  
        stack = [0]     
        while stack:
            curr_room = stack.pop()  
            if curr_room not in visited:
                visited.add(curr_room)  
                for next_room in rooms[curr_room]:
                    if next_room not in visited:
                        stack.append(next_room)
        return len(visited) == len(rooms)