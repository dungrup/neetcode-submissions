class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l , r = 0, len(numbers) - 1
        output = []

        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                output.append(l +1)
                output.append(r + 1)
                return output
            elif s < target:
                l += 1
            else:
                r -= 1

        return output

        


        

            