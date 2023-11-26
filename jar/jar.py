class Jar:
    def __init__(self, capacity=12,size=0):
        self.capacity=capacity
        self.size=size

    def __str__(self):
        return (f"{'🍪'*self.size}")

    def deposit(self, n):
        self.size+=n

    def withdraw(self, n):
        self.size-=n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self,capacity):
        if capacity<1:
            raise ValueError('not a positive integer')
        self._capacity=capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self,size):
        if self.capacity<size or size<0:
            raise ValueError('jar overflow or cookie shortage')
        self._size=size
