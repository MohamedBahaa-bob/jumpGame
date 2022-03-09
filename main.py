# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# correct solution in O(n^2), there is a better greedy solution in O(n)
"""class Solution:
    def canJump(self, nums) -> bool:
        # bottom up
        memo = [False] * len(nums)
        memo[len(nums) - 1] = True
        for i in range(len(nums) - 2, -1, -1):
            for j in range(nums[i], -1, -1):
                if i + j >= len(nums) - 1:
                    memo[i] = True
                    break
                elif memo[i + j]:
                    memo[i] = True
                    break
        return memo[0]"""


# greedy solution: O(n)
class Solution:
    def canJump(self, nums) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        if goal == 0:
            return True
        return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    obj = Solution()
    print(obj.canJump([3, 2, 1, 0, 4]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
