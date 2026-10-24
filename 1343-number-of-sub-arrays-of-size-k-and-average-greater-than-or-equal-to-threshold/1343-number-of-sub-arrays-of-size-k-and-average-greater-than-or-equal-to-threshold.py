class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        count = 0
        sum = 0

        for i in range(k):
            sum += arr[i]
        
        if sum / k >= threshold:
            count += 1
        
        for i in range(k, len(arr)):
            sum = sum - arr[i - k] + arr[i]
            
            if (sum / k) >= threshold:
                count += 1

        return count