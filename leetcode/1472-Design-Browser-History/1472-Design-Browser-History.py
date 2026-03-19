class BrowserHistory(object):
    class Listnode(object):
        def __init__(self, val):
            self.val = val
            self.next = None
            self.prev = None   

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.current = self.Listnode(homepage)

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        new_node = self.Listnode(url)
        
        self.current.next = new_node
        new_node.prev = self.current
        self.current = new_node

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while steps>0 and self.current.prev:
            self.current=self.current.prev
            steps-=1
        return self.current.val
        
        
    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while steps>0 and self.current.next:
            self.current=self.current.next
            steps-=1
        return self.current.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)