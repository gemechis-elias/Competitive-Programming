class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Create a list to store the number of passengers at each location
        passenger_count = [0] * 1001
        
        for trip in trips:
            passenger_count[trip[1]] += trip[0]
            passenger_count[trip[2]] -= trip[0]

        current_passengers = 0
        
        for count in passenger_count:
            current_passengers += count
            if current_passengers > capacity:
                return False
        
        return True
