class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        ls=[]
        ls.append(celsius+273.15)
        ls.append(celsius*1.80+32.00)  
        return ls      