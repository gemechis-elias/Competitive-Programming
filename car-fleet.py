class Solution:
    def carFleet(self, target: int, position, speed) -> int:
        cars = [(position[i], (target - position[i]) / speed[i]) for i in range(len(position))]
        cars.sort(reverse=True)
        
        current_fleet_time = 0
        num_fleets = 0
        
        for pos, time in cars:
            if time > current_fleet_time:
                num_fleets += 1
                current_fleet_time = time
            
        return num_fleets