class Solution:
   def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    # def dailyTemperatures(temperatures):
    n = len(temperatures)
    result = [0] * n
    stack = []  # will store indices

    for i, temp in enumerate(temperatures):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_index = stack.pop()
            result[prev_index] = i - prev_index
        stack.append(i)

    return result

# Example
# print(dailyTemperatures([30,38,30,36,35,40,28]))  # Output: [1,4,1,2,1,0,0]
# print(dailyTemperatures([22,21,20]))              # Output: [0,0,0]
    
        