
class Counter:

    def getValue(self) :
        return self._strokes
    
    def click(self) :
        self._strokes = self._strokes + '|'

    def reset(self) :
        self._strokes = ""

    def __init__(self):
        self._limit = 0
    def setLimit(self, maximum) :
        self._limit = maximum

    