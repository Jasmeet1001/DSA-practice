class DArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.length = 0
        self.index = -1
        self.array = self.create(self.capacity)

    def __len__(self):
        return self.length

    def __getitem__(self, i):
        if self.index < i:
            raise IndexError("List index out of range")
        return self.array[i]

    def create(self, cap):
        return [0] * cap
    
    def resize(self):
        self.capacity *= 2
        new_arr = self.create(self.capacity)
        for i in range(self.length):
            new_arr[i] = self.array[i]
        self.array = new_arr

    def append(self, ele):
        if self.length == self.capacity:
            self.resize()
        self.index += 1
        self.length += 1
        self.array[self.index] = ele

    def insert(self, ele, index):
        if index < 0 or index >= self.index:
            raise IndexError()
        if self.length == self.capacity:
            self.resize()
        
        for i in range(self.length - 1, index - 1, -1):
            self.array[i + 1] = self.array[i]

        self.array[index] = ele
        self.index += 1
        self.length += 1

    def pop(self):
        if self.index == -1:
            raise IndexError("Pop from empty list")
        self.array[self.index] = 0
        self.index -= 1
        self.capacity -= 1
        self.length -= 1
        
    def remove(self, index):
        if self.index == -1:
            raise IndexError("Remove from empty list")
        for i in range(index, self.length - 1):
            self.array[i] = self.array[i + 1]
        self.array[self.length - 1] =  0
        self.index -= 1
        self.capacity -= 1
        self.length -= 1



arr = DArray(2)
arr.append(2)
for i in range(len(arr)):
    print(arr[i])
