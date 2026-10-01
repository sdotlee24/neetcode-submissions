class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def traverse(i, subTot):
            if i == len(coins) or subTot > amount:
                return 0
            if subTot == amount:
                return 1
            if (subTot, i) in memo:
                return memo[(subTot, i)]

            val = traverse(i, subTot+coins[i]) + traverse(i+1, subTot)
            memo[(subTot, i)] = val

            return val

        return traverse(0, 0)