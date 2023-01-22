class DArray:
    #Initializing the Dynamic Array
    def __init__(self):
        self.capacity = 2
        self.length = 0
        self.index = -1
        self.array = self.create(self.capacity)

    def __len__(self):
        return self.length

    def __getitem__(self, i):
        if self.index < i:
            raise IndexError("List index out of range")
        return self.array[i]

    #A list like representation of our Dynamic Array
    def __repr__(self):
        if self.length == 0:
            return "[]"
        string = '['
        for i in range(self.length-1):
            string += str(self.array[i]) + ', '
        
        string += str(self.array[self.length-1]) + ']'
        return string

    #Create an array with given capacity, initially 2
    def create(self, cap):
        return [0] * cap
    
    #Increasing capacity by times 2, creating a new array with that capacity and copying all the elements into the new array
    def resize(self):
        if self.capacity == 0:
            self.capacity = 2
        else:
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

    #Inserting an element at a particular index
    def insert(self, ele, index):
        if index < 0 or index >= self.index:
            raise IndexError()
        if self.length == self.capacity:
            self.resize()
        #Right shifting elements to add the new elements
        for i in range(self.length - 1, index - 1, -1):
            self.array[i + 1] = self.array[i]

        self.array[index] = ele
        self.index += 1
        self.length += 1

    def pop(self):
        if self.index == -1:
            raise IndexError("Pop from empty list")
        self.remove(self.index)
        
    #Removing an element on a particular index
    def remove(self, index):
        if self.index < index < -1:
            raise IndexError("List index out of range")
        new_arr = self.create(self.length - 1)
        #Removing element by fixing j when index is found 
        j = 0
        for i in range(self.length):
            if i == index:
                j -= 1
            else:
                new_arr[j] = self.array[i]
            j += 1
        self.array = new_arr
        self.index -= 1
        self.length -= 1
        self.capacity -= 1

    def clear(self):
        self.capacity = 0
        self.length = 0
        self.index = -1
        self.array = self.create(self.capacity)


if __name__ == "__main__":
    arr = DArray()
    for i in range(10):
        arr.append(i)
    print(arr)
    arr.insert(50, 2)
    print(arr)
    arr.remove(4)
    print(arr)
    arr.pop()
    print(arr)
    arr.clear()
    print(arr)
    arr.append(10)
    print(arr)