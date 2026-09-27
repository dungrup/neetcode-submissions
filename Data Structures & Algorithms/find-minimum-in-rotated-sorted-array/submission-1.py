class Solution:
    def findMin(self, nums: List[int]) -> int:
        output = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] <= nums[r]:
                output = min(output, nums[l])
                break
        
            m = (l + r) // 2
            output = min(output, nums[m])
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1

        return output

            
        