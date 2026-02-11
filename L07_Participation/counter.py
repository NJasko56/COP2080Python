
class Counter:

    def getValue(self) :
        return self._value
    
    def click(self) :
        self._value = self._value + 1
        if self._value > self._limit :
            print("Limit Exceeded")

    def reset(self) :
        self._value = 0

    def __init__(self):
        self._limit = 0
    def setLimit(self, maximum) :
        self._limit = maximum

    