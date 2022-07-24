class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        if popped == pushed:
            return True
        pushed.remove(popped[0])
        newPushed = pushed
        
        popped_cut = popped[1:]
        if newPushed == popped_cut[::-1]:
            return True
        else:
            return False