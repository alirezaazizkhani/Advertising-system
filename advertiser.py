from base_model import BaseAdvertising

class Advertiser(BaseAdvertising):
    TotalClicks = 0
    Ids = []
    def __init__(self, id, name):
        super().__init__()
        self.setId(id)
        self.__name = name
    
    def setId(self, id):
        if id in Advertiser.Ids:
            print("id already exist")
            exit()
        else:
            Advertiser.Ids.append(id)
            super().setId(id)

    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name

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
        return  Advertiser.TotalClicks

    def incClicks(self):
        Advertiser.TotalClicks += 1
        super().incClicks()
    
    def describeMe(self):
        return """ 
        Advertiser is a class for managing advertisers by their name and id.
"""

if __name__ == '__main__':
    ex = Advertiser(10)
    ex.incClicks()

    ex2 = Advertiser(11)
    ex2.incClicks()
    ex2.incClicks()

    print(ex.getClicks())
    print(ex2.getClicks())
    print(Advertiser.getTotalClicks())