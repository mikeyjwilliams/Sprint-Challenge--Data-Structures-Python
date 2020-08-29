class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity

        #! I think some other datastructure
        #! is needed to hold the nodes for
        #! the buffer.

    def append(self, item):
        pass #! just pseudo code for now.
        # before appending... check
        #! if capacity >= 5
            #* append target item
            #* capacity increment
        #! else:
            #* starting at 0 incrementally
            #* pass through the buffer
            #* overwriting the old w/ new value given
            #* then increment pointer to next item
            #* to repeat


    def get(self):
        pass
        #!