class BaseAdvertising():
    def __init__(self):
        self.__id = None
        self.__clicks = 0
        self.__views = 0
    
    def setId(self, id):
        self.__id = id

    def getClicks(self):
        return self.__clicks

    def getViews(self):
        return self.__views
    
    def incClicks(self):
        self.__clicks += 1
    
    def incViews(self):
        self.__views += 1

    def describeMe(self):
        return """
        BaseAdvertising is a base class for advertising and ad classes
"""


if __name__ == '__main__':
    pass