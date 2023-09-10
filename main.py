import ctypes

class MyList:

    def __init__(self):
        self.size = 1
        self.n = 0
        # C type array with size = self.size
        self.A = self.__make_array(self.size)

    def __make_array(self, capacity):
        # creates a C type array(static, referential) with size capacity
        return(capacity*ctypes.py_object)()
    
    def __len__(self):
        return self.n

    def __str__(self):
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ','
        
        return '[' + result[:-1] + ']'
    
    def append(self, item):
        if self.n == self.size:
            # resize
            self.__resize(self.size * 2)
        
        # append
        self.A[self.n] = item
        self.n = self.n + 1
    
    def __resize(self, new_capacity):
        # create a new array with new capacity
        B = self.__make_array(new_capacity)
        self.size = new_capacity
        # copy the content of A to B
        for i in range(self.n):
            B[i] = self.A[i]
        # reassign A
        self.A = B

    def __getitem__(self, index):
        if 0 <= index < self.n:
            return self.A[index]
        else:
            return 'IndexError - Index out of range'
    
    def pop(self):
        if self.n == 0:
            return 'Empty List'
        print(self.A[self.n - 1])
        self.n = self.n - 1
    
    def clear(self):
        self.n = 0
        self.size = 1
    
    def __delitem__(self, pos):
        # delete
        if 0 <= pos < self.n:
            for i in range(pos, self.n - 1):
                self.A[i] = self.A[i + 1]
            self.n = self.n - 1

    def find(self, item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
            
        return 'ValueError - not in list'

    def insert(self, pos, item):
        if self.n == self.size:
            self.__resize(self.size * 2)
        for i in range(self.n, pos, -1):
            self.A[i] = self.A[i - 1]
        self.A[pos] = item
        self.n = self.n + 1

    def remove(self, item):
        pos = self.find(item)
        if type(pos) == int:
            self.__delitem__(pos)
        else:
            return pos

L = MyList()

