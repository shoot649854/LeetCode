class Solution:
    def __init__(self) -> None:
        pass
    
    def containsDuplicate(self, nums):
        hashMap = set()

        for i in nums:
            if i in hashMap:
                return True
            else:
                hashMap.add(i)
        return False
    
    def caseCheck(self):
        cases = [[1, 2, 3, 1], 
                 [1, 2, 3, 4], 
                 [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]]
        for i in cases:
            result = self.containsDuplicate(i)
            print("Case: %s -> Contains Duplicate: %s" % (i, result))


solution = Solution()
solution.caseCheck()
