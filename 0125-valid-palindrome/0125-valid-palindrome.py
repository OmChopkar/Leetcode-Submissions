class Solution(object):
    def isPalindrome(self, s):
        cleaned_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        rev=""
        for i in range(len(cleaned_s)-1,-1,-1):
            rev+=cleaned_s[i]
        if rev==cleaned_s:
            return True
        return False