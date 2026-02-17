class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        l=[]
        l.append((celsius + 273.15))
        l.append((celsius * 1.80 + 32.00))
        return l