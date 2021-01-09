# helper functions

def left(index):
    '''Return index's left child index.
    '''
    return index * 2 + 1


def right(index):
    '''Return index's left child index.
    '''
    return index * 2 + 2


def parent(index):
    '''Return index's parent index.'''

    return (index - 1) // 2

class EmptyHeapException(Exception):
    print("Empty Heap")
    pass

class MinHeap:

    def __init__(self, L=None):
        '''Create a new MinHeap.
        This method is complete.'''

        if not L:
            self._data = []
        else:
            self._data = L
            self._min_heapify()


    def __len__(self):
        '''Return the length of the MinHeap.
        This method is complete.'''

        return len(self._data)


    def __str__(self):
        '''Return a string representation of the heap.
        This method is complete.'''

        return str(self._data)


    def insert(self, v):
        '''Insert v in self. Maintain heap property.'''
        self._data.append(v)
        self._percolate_up()

        return



    def extract_min(self):
        '''Remove minimal value in self. Restore heap property.
        Raise EmptyHeapException if heap is empty.'''

        #check if the heap is empty:
        if len(self._data) == 0:
            raise EmptyHeapException()

        minimal = self._data.pop(0)
        self._min_heapify()

        return minimal


    def _percolate_up(self):
        '''Restore heap property of self after
        adding new item'''
        i = len(self._data) - 1

        while i > 0:
            p = parent(i)
            if self._data[p] is not None and self._data[i] is not None:
                if self._data[p] > self._data[i]:
                    tmp = self._data[p]
                    self._data[p] = self._data[i]
                    self._data[i] = tmp
            i = p

        return

    def _percolate_down(self, i):
        ''' Restore heap property of subtree
        rooted at index i.
        '''

        # while larger than at least one child
        # swap with smaller child and repeat


        left_child = left(i)
        right_child = right(i)

        minimal = i
        length = len(self._data)


        #check either left or right child is smaller and if it exists.
        if left_child < length and self._data[left_child] < self._data[minimal]:
            minimal = left_child
        elif right_child < length and self._data[right_child] < self._data[minimal]:
            minimal = right_child

        #recursively call the function to swap parent and the smaller child.
        if minimal != i:
            tmp = self._data[i]
            self._data[i] = self._data[minimal]
            self._data[minimal] = tmp
            self._percolate_down(minimal)

        return

    def _min_heapify(self):
        '''Turn unordered list into min-heap.'''

        # for each node in the first half of the list
        # percolate down
        for i in range(len(self._data) // 2, -1, -1):
            self._percolate_down(i)