class Solution:
    def carFleet(self,target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, (target - p) / s) for p, s in zip(position, speed)]
    
    # Step 2: sort by position descending
        cars.sort(reverse=True)
    
        fleets = 0
        curr_time = 0
    
    # Step 3: iterate
        for pos, time in cars:
         if time > curr_time:
            fleets += 1
            curr_time = time
    
        return fleets