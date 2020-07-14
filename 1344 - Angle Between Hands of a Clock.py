class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        if(hour==12):
            hour=0
        hour = hour + minutes/60
        hour_deg = hour*30
        min_deg = minutes*6
        return min(abs(hour_deg - min_deg), 360-abs(hour_deg - min_deg))