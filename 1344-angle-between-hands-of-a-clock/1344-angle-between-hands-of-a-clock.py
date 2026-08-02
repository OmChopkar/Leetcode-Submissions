class Solution(object):
    def angleClock(self, hour, minutes):
        angle=(30*hour)-(5.5*minutes)
        angle=abs(angle)
        return min(angle,360-angle)