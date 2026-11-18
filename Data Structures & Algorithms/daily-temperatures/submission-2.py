class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        max_temps = [] ## temp, idx

        for idx, temp in enumerate(temperatures):
            while max_temps and max_temps[-1][0] < temp:
                t, i = max_temps.pop()
                result[i] = idx - i
            
            max_temps.append([temp, idx])

        return result
            