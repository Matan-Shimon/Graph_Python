
class Edge_Data:
    def __init__(self, src, dest, weight, tag) -> None:
        if weight < 0:
            raise Exception("edge weigh must be positive")
        self.src = src
        self.dest = dest
        self.tag = tag
        self.weight = weight

    def getSrc(self):
        return self.src

    def getDest(self):
        return self.dest

    def getWeight(self):
        return self.weight

    def getTag(self):
        return self.tag

    def setTag(self, t):
        self.tag = t

    def setWeight(self, w):
        self.weight = w


