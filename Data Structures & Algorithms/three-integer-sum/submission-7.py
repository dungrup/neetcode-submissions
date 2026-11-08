class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []

        for idx, num in enumerate(nums):
            if num > 0:
                break

            if idx > 0 and num == nums[idx - 1]:
                continue
            
            l = idx + 1
            r = len(nums) - 1

            while l < r:
                s = num + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    output.append([nums[idx], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        
        return output

