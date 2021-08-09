#!/usr/bin/python
import bisect

class Node:
    def __init__(self, val, parent):
        self.childs = []
        self.value = val
        self.parent = parent
        self.currentDepth = 0
    
    def add(self, val):
        point = bisect.bisect([child.value for child in self.childs], val)
        self.childs.insert(point, Node(val, self))
    
    def getNDepthChildren(self, n):
        if(n == 0):
            return([self])
        result = []
        for child in self.childs:
            result += child.getNDepthChildren(n-1)
        return(result)
    
    def getNDepthValues(self, n):
        return [(child.value,) for child in self.getNDepthChildren(n)]
    
    def find(self, val):
        depth = 0
        children = self.getNDepthChildren(depth)
        while children != []:
            for i in range(len(children)):
                if val == children[i].value:
                    return children[i]
            depth += 1
            children = self.getNDepthChildren(depth)
        return None
    
    def getAncestor(self):
        if self.parent == None:
            return self
        else:
            return self.parent.getAncestor()
        
    def getAncestorList(self):
        if self.parent == None:
            return [self.value]
        return (self.parent.getAncestorList() + [self.value])
    
    