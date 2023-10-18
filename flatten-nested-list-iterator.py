# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedList = nestedList
        
        self.nums = []
        def construct_nums(i, nested) -> None:
            if nested.isInteger():
                self.nums.append(nested.getInteger())
                return
            l = nested.getList()
            for i in range(len(l)):
                
                construct_nums(i, l[i])
        for i in range(len(self.nestedList)):
            construct_nums(i, self.nestedList[i])
       
        self.n = len(self.nums)
        self.idx = 0
    
    def next(self) -> int:

        ans = self.nums[self.idx]
        self.idx += 1
        return ans
    
    def hasNext(self) -> bool:
        if self.idx < self.n:
            return True
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())