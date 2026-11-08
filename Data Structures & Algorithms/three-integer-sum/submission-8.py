class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()

        for idx, val in enumerate(nums):
            if val > 0:
                break
            
            if idx > 0 and val == nums[idx - 1]:
                continue

            l , r = idx + 1, len(nums) - 1
            while l < r:
                s = val + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    output.append([nums[l], nums[r], val])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return output

