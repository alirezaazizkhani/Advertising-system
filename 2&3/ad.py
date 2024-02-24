from base_model import BaseAdvertising
from advertiser import Advertiser

class Ad(BaseAdvertising):
    Ids = []
    def __init__(self, id, title, imgUrl, link, advertiser: Advertiser):
        super().__init__()
        self.setId(id)
        self.__title = title
        self.__imgUrl = imgUrl
        self.__link = link
        self.__advertiser = advertiser
    
    def setId(self, id):
        if id in Advertiser.Ids:
            print("id already exist")
            exit()
        else:
            Ad.Ids.append(id)
            super().setId(id)

    def getTitle(self):
        return self.__title
    
    def setTitle(self, title):
        self.__title = title

    def getImgUrl(self):
        return self.__imgUrl
    
    def setImgUrl(self, imgUrl):
        self.__imgUrl = imgUrl
    
    def getLink(self):
        return self.__link

    def setLink(self, link):
        self.__link = link

    def setAdvertiser(self, advertiser: Advertiser):
        self.__advertiser = advertiser

    def incClicks(self):
        self.__advertiser.incClicks()
        super().incClicks()
    
    def incViews(self):
        self.__advertiser.incViews()
        super().incViews()

    def describeMe(self):
        return """
        Ad is a class for managing ads.
"""

if __name__ == '__main__':
    ad1 = Ad(1)
    ad2 = Ad(2)
    ad3 = Ad(3)

    advertiser1 = Advertiser(1)
    advertiser2 = Advertiser(2)  

    ad1.setAdvertiser(advertiser1)
    ad2.setAdvertiser(advertiser1)
    ad3.setAdvertiser(advertiser2)

    ad1.incClicks()
    ad1.incViews()
    
    ad2.incClicks()
    ad2.incViews()

    ad3.incClicks()
    ad3.incViews()

    print(Advertiser.getTotalClicks())
    print(advertiser1.getClicks())
    print(ad1.getViews())
    print(advertiser2.getClicks())