class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        answer = []
        kelvin = celsius + (273.15)
        fah = celsius *1.80 + 32.00
        
        answer = [kelvin, fah]
        return answer
        
        