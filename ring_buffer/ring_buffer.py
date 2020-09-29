class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.index = 0

    def append(self, item):
        # add item to list if storage has not met capacity
        if len(self.storage) < self.capacity:    
            self.storage.append(item)
        else:
            # if capacity has been met, replace index 0 of storage with new item
            self.storage[self.index] = item
            # put index at one, so it's the next item changed
            self.index += 1
        # if index has made it to capacity/the end, set it back to 0
        if self.index == self.capacity:
            self.index = 0

    def get(self):
        # return storage list
        return self.storage