class Solution(object):
    def getMinDistance(self, nums, target, start):
        mindist=float('inf')
        for i in range(len(nums)):
            if nums[i]==target:
                dist=abs(i-start)
                if dist<mindist:
                    mindist=dist
        return mindist