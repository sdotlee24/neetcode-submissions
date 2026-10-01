class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append([position[i], speed[i]])
        
        cars.sort(key=lambda x: x[0], reverse=True)
        stack = []
        for i in range(len(speed)):
            t = (target - cars[i][0]) / cars[i][1]
            if len(stack) == 0 or stack[-1] < t:
                stack.append(t)
        
        return len(stack)

