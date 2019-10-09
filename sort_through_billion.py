import random

from typing import List
import numpy as np


class PriorityQueue(object):
    def __init__(self, qty: int = 1000):
        self.queue: List[int] = [0] * qty   ## create placeholder
    
    def _sort(self): ## Insertion sort O(n^2)
        for i in range(1, len(self.queue), 1):
            val: int = self.queue[i]
            j: int = i-1
            while j >=0 and self.queue[j] < val:
                self.queue[j+1] = self.queue[j]
                j -= 1
            self.queue[j+1] = val
        
        
    def insert(self, value: int): 
        max_number: int = 0 
        if self.queue[0] < value:
            self.queue[0] = value 
            self._sort()
        else:
            pass
        
        

# create random array
arr = np.random.randint(0,100000000000, size = 100000000)
np.random.shuffle(arr)

queue = PriorityQueue()
_ = [queue.insert(i) for i in arr]  ## insert into queue while maintaining priority 
 
 ## Top 1000 
 
print(queue.queue)
        
        
        
