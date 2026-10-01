class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        curMax = 0
        maxMap = {} #{value: # of occurences}

        res = []

        for i in range(k):
            maxMap[nums[i]] = maxMap.get(nums[i], 0) + 1
            curMax = max(curMax, nums[i])
        
        l = 0
        res.append(curMax)
        for r in range(k, len(nums)):
            maxMap[nums[r]] = maxMap.get(nums[r], 0) + 1
            maxMap[nums[l]] -= 1

            tempMax = nums[r]
            if nums[l] == curMax and maxMap[nums[l]] == 0: #we just got rid of the max element
                #then we have to recompute the max
                for value in maxMap:
                    if value > tempMax and maxMap[value] > 0:
                        tempMax = value
                curMax = tempMax
            else:
                curMax = max([curMax, nums[r]])
            res.append(curMax)
            l += 1
        return res
