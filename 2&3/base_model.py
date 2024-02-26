class BaseAdvertising():
    def __init__(self):
        self._id = None
        self._clicks = 0
        self._views = 0
    
    def setId(self, id):
        self._id = id

    def getClicks(self):
        return self._clicks

    def getViews(self):
        return self._views
    
    def incClicks(self):
        self._clicks += 1
    
    def incViews(self):
        self._views += 1

    def describeMe(self):
        return """
        BaseAdvertising is a base class for advertising and ad classes
"""