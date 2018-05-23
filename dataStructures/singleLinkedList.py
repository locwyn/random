class Node(object):
    def __init__(self, name, data, nextNode):
        self.name = str(name)
        self.data = data
        self.nextNode = nextNode
    def getName(self):
        return self.name
    def getData(self):
        return self.data
    def getNextNode(self):
        return self.nextNode
    def __str__(self):
        return self.name
