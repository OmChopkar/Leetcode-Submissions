class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        count=0
        for i in arr1:
            for j in arr2:
                if abs(i-j)<=d:
                    break
            else:
                count+=1
        return count
        