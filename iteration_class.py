class Iteration:
    def __iter__(self):
        self.num = 0
        return self
    
    def __next__(self):
        if self.num < 20:
            self.num += 1
            return self.num
        
        else:
            raise StopIteration
        
obj = Iteration()
iterator = iter(obj)

for i in iterator:
    print(i)