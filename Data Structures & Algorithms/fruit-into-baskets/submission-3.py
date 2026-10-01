class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # [0, 1, 0, 3, 3, 3] , select fruit 0, 3 => res = 5
        
        #condition: lenght(seen(fruits)) <= 2

        #seen : (0, 1, 0, 3)
        res = 0 
        count = defaultdict(int)
        l = 0
        for r in range(len(fruits)):
            count[fruits[r]] += 1
            while len(count) > 2:
                count[fruits[l]] -= 1
                if count[fruits[l]] == 0:
                    count.pop(fruits[l])
                l += 1

            res = max(res, r-l+1)

        return res
            

        