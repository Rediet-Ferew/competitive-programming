class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

        
class BrowserHistory:

    def __init__(self, homepage: str):
        self.home = ListNode(homepage)
        

    def visit(self, url: str) -> None:
        page = ListNode(url)
        
        self.home.next = page
        page.prev = self.home
        self.home = page

    def back(self, steps: int) -> str:
        
        while steps and self.home.prev:
            self.home = self.home.prev
            steps -= 1
        return self.home.val
    def forward(self, steps: int) -> str:
        while steps and self.home.next:
            self.home = self.home.next
            steps -= 1
        return self.home.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)