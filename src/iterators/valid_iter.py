class ValidIter:
    """Help class that implements a valid range-like iterator."""
    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.number = 0
        return self
    
    def __next__(self):
        number = self.number
        if number < self.max:
            self.number += 1
            return number
        else:
            raise StopIteration
