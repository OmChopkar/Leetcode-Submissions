class Solution(object):
    def isBalanced(self, num):
        intlist=[]
        for i in num:
            intlist.append(int(i))       

        even=0
        odd=0

        for i in range(len(intlist)):
            if i%2==0:
                even+=intlist[i]
            else:
                odd+=intlist[i]

        if even==odd:
            return True
        return False 