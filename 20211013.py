class CQueue(object):

    def __init__(self):
        self.stack_in=[]
        self.stack_out=[]


    def appendTail(self, value):

        self.stack_in.append(value)
        """
        :type value: int
        :rtype: None
        """


    def deleteHead(self):
        """
        :rtype: int
        """



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()