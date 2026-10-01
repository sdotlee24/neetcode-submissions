class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # [7, 1], [4, 2], [1, 2], [0, 1]
        # 2, 2, 1, 1


        # 1 + 2x = 4 + x x = 3
        
        res = 0

        cars = [[position[i], speed[i]] for i in range(len(speed))]
        cars.sort(key=lambda x: x[0], reverse=True)
        stck = []

        for i in range(len(speed)):
            stck.append((target - cars[i][0]) / cars[i][1])
            if len(stck) > 1 and stck[-1] <= stck[-2]:
                stck.pop()
        return len(stck)