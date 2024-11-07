# HW 5
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

class MinBinaryHeap:
    '''
        >>> h = MinBinaryHeap()
        >>> h.getMin
        >>> h.insert(10)
        >>> h.insert(5)
        >>> h
        [5, 10]
        >>> h.insert(14)
        >>> h._heap
        [5, 10, 14]
        >>> h.insert(9)
        >>> h
        [5, 9, 14, 10]
        >>> h.insert(2)
        >>> h
        [2, 5, 14, 10, 9]
        >>> h.insert(11)
        >>> h
        [2, 5, 11, 10, 9, 14]
        >>> h.insert(14)
        >>> h
        [2, 5, 11, 10, 9, 14, 14]
        >>> h.insert(20)
        >>> h
        [2, 5, 11, 10, 9, 14, 14, 20]
        >>> h.insert(20)
        >>> h
        [2, 5, 11, 10, 9, 14, 14, 20, 20]
        >>> h.getMin
        2
        >>> h._leftChild(1)
        5
        >>> h._rightChild(1)
        11
        >>> h._parent(1)
        >>> h._parent(6)
        11
        >>> h._leftChild(6)
        >>> h._rightChild(9)
        >>> h.deleteMin()
        2
        >>> h._heap
        [5, 9, 11, 10, 20, 14, 14, 20]
        >>> h.deleteMin()
        5
        >>> h
        [9, 10, 11, 20, 20, 14, 14]
        >>> len(h)
        7
        >>> h.getMin
        9
    '''

    def __init__(self):
        self._heap=[]
        
    def __str__(self):
        return f'{self._heap}'

    __repr__=__str__

    def __len__(self):
        return len(self._heap)

    @property
    def getMin(self):
        # - YOUR CODE STARTS HERE -
        if len(self._heap) == 0:
            return None
        else:
            return self._heap[0]
    
    def _parent(self, index):
        parentIndex = index // 2
        if parentIndex >= 1:
            return self._heap[parentIndex - 1]
        else:
            return None

    def _leftChild(self, index):
        leftIndex = 2 * index
        if leftIndex <= len(self._heap):
            return self._heap[leftIndex - 1]
        else:
            return None

    def _rightChild(self, index):
        rightIndex = 2 * index + 1
        if rightIndex <= len(self._heap):
            return self._heap[rightIndex - 1]
        else:
            return None

    def insert(self, item):
        self._heap.append(item)
        k = len(self._heap)
        while k > 1 and self._heap[k - 1] < self._parent(k):
            #bubble sort it
            parK = k // 2
            self._heap[k - 1], self._heap[parK - 1] = self._heap[parK - 1], self._heap[k - 1]
            k = parK

    def deleteMin(self):
        if len(self)==0:
            return None        
        elif len(self)==1:
            value=self._heap[0]
            self._heap=[]
            return value 

        # - YOUR CODE STARTS HERE -
        else:
            # extract the minimum value from the heap
            minVal = self._heap[0]
            finalElement = self._heap.pop()
            self._heap[0] = finalElement
            k = 1
            # iterate through the heap starting from index 1
            while k * 2 <= len(self._heap):
                lcValue = self._leftChild(k)
                rcValue = self._rightChild(k)
                smallestChildIndex = k * 2
                # check if the right child exists and is smaller than the left child
                if rcValue is not None and rcValue < lcValue:
                    smallestChildIndex += 1
                # if the parent is greater than the smallest child, swap them
                if self._heap[k - 1] > self._heap[smallestChildIndex - 1]:
                    self._heap[k - 1], self._heap[smallestChildIndex - 1] = self._heap[smallestChildIndex - 1], self._heap[k - 1]
                    k = smallestChildIndex
                else:
                    k = len(self._heap) + 1  
            return minVal
        
class PriorityQueue:
    '''
        >>> priority_q = PriorityQueue()
        >>> priority_q.isEmpty()
        True
        >>> priority_q.peek()
        >>> priority_q.enqueue('sara',0)
        >>> priority_q
        [(0, 'sara')]
        >>> priority_q.enqueue('kyle',3)
        >>> priority_q
        [(0, 'sara'), (3, 'kyle')]
        >>> priority_q.enqueue('harsh',1)
        >>> priority_q
        [(0, 'sara'), (3, 'kyle'), (1, 'harsh')]
        >>> priority_q.enqueue('ajay',5)
        >>> priority_q
        [(0, 'sara'), (3, 'kyle'), (1, 'harsh'), (5, 'ajay')]
        >>> priority_q.enqueue('daniel',4)
        >>> priority_q.isEmpty()
        False
        >>> priority_q
        [(0, 'sara'), (3, 'kyle'), (1, 'harsh'), (5, 'ajay'), (4, 'daniel')]
        >>> priority_q.enqueue('ryan',7)
        >>> priority_q
        [(0, 'sara'), (3, 'kyle'), (1, 'harsh'), (5, 'ajay'), (4, 'daniel'), (7, 'ryan')]
        >>> priority_q.dequeue()
        (0, 'sara')
        >>> priority_q.peek()
        'harsh'
        >>> priority_q
        [(1, 'harsh'), (3, 'kyle'), (7, 'ryan'), (5, 'ajay'), (4, 'daniel')]
        >>> priority_q.dequeue()
        (1, 'harsh')
        >>> len(priority_q)
        4
        >>> priority_q.dequeue()
        (3, 'kyle')
        >>> priority_q.dequeue()
        (4, 'daniel')
        >>> priority_q.dequeue()
        (5, 'ajay')
        >>> priority_q.dequeue()
        (7, 'ryan')
        >>> priority_q.dequeue()
        >>> priority_q.isEmpty()
        True
    '''

    def __init__(self):
        self._items = MinBinaryHeap()
    
    def enqueue(self, value, priority):
        # - YOUR CODE STARTS HERE -
        self._items.insert((priority, value))
    
    def dequeue(self):
        # - YOUR CODE STARTS HERE -
        if self.isEmpty():
            return None
        return self._items.deleteMin()
    
    def peek(self):
        # - YOUR CODE STARTS HERE -
        if self.isEmpty():
            return None
        return self._items.getMin[1]

    def isEmpty(self):
        # - YOUR CODE STARTS HERE -
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)

    __repr__ = __str__

class Graph:
    """
        >>> d_g1={
        ... 'A':[('B',2),('C',6),('D',7)],
        ... 'B':[('C',3),('G',12)],
        ... 'C':[('D',2),('E',3)],
        ... 'D':[('C',1),('E',2)],
        ... 'E':[('G',5)],
        ... 'F':[('D',2),('E',4)]}
        >>> my_graph = Graph(d_g1)
        >>> my_graph.addEdge('G', 'C', 4)
        >>> my_graph
        {'A': [('B', 2), ('C', 6), ('D', 7)], 'B': [('C', 3), ('G', 12)], 'C': [('D', 2), ('E', 3)], 'D': [('C', 1), ('E', 2)], 'E': [('G', 5)], 'F': [('D', 2), ('E', 4)], 'G': [('C', 4)]}
        >>> my_graph.dijkstra_table('A')   # ---> order of key,value pairs does not matter 
        {'A': 0, 'B': 2, 'C': 5, 'D': 7, 'E': 8, 'F': inf, 'G': 13}
    """
    def __init__(self, graph_repr=None):
        if graph_repr is None:
            self.vertList = {}
        else:
            self.vertList = graph_repr

    def __str__(self):
        return str(self.vertList)

    __repr__ = __str__

    def addVertex(self, key):
        if key not in self.vertList:
            self.vertList[key] = []
            return self.vertList

    def addEdge(self, frm, to, cost=1):
        if frm not in self.vertList:
            self.addVertex(frm)
        if to not in self.vertList:
            self.addVertex(to)
        self.vertList[frm].append((to, cost))

    def dijkstra_table(self, start):
        # - YOUR CODE STARTS HERE -
        # fill list with inf
        dijTable = {node: float('inf') for node in self.vertList}
        # set cost of the start node to 0
        dijTable[start] = 0
        # initialize the priority queue from laqst class
        priorityQueue = PriorityQueue()
        priorityQueue.enqueue(start, 0)  
        #while loop
        while not priorityQueue.isEmpty():
            currCost, currNode = priorityQueue.dequeue()
            # check if the curr node is alrdy visite
            if currCost <= dijTable[currNode]:
                # check the neighbors of current node
                for neighbor, neighborCost in self.vertList[currNode]:
                    costToNeighbor = currCost + neighborCost
                    if costToNeighbor < dijTable[neighbor]:
                        #update the cost to the neighbor if necessary
                        dijTable[neighbor] = costToNeighbor
                        # add the neighbor to priority queue with updated cost
                        priorityQueue.enqueue(neighbor, costToNeighbor)
        updatedDijTable = {}
        # iterate over each node and cost pair 
        for node, cost in dijTable.items():
            # if the cost is still infinity, assign infinity to the node in the updated table
            if cost == float('inf'):
                updatedDijTable[node] = float('inf')
            #if not then assign the actual cost to the node in the updated table
            else:
                updatedDijTable[node] = cost
        # assign the updated table back to dijTable
        dijTable = updatedDijTable    
        return dijTable

def run_tests():
    import doctest

    # Run start tests in all docstrings
    doctest.testmod(verbose=True)
    
    # Run start tests per class
    #doctest.run_docstring_examples(MinBinaryHeap, globals(), name='HW5',verbose=True)   

if __name__ == "__main__":
    run_tests()

