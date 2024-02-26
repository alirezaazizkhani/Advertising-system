from base_model import BaseAdvertising

class Advertiser(BaseAdvertising):
    _totalClicks  = 0
    _ids = []
    def __init__(self, id, name):
        super().__init__()
        self.setId(id)
        self._name = name
    
    def setId(self, id):
        if id in Advertiser._ids:
            print("id already exist")
            exit()
        else:
            Advertiser._ids.append(id)
            super().setId(id)

    def getName(self):
        return self._name
    
    def setName(self, name):
        self._name = name

    def help():
        return """
        Advertiser class has four fields: 
        id : the id of the advertiser.
        name : the name of the advertiser
        clicks : number of clicks of the advertiser's ads
        views : number of views of the advertiser's ads
"""

    @staticmethod
    def getTotalClicks():
        return Advertiser._totalClicks

    def incClicks(self):
        Advertiser._totalClicks += 1
        super().incClicks()
    
    def describeMe(self):
        return """ 
        Advertiser is a class for managing advertisers by their name and id.
"""