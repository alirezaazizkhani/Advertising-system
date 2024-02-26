from base_model import BaseAdvertising
from advertiser import Advertiser

class Ad(BaseAdvertising):
    Ids = []
    def __init__(self, id, title, imgUrl, link, advertiser: Advertiser):
        super().__init__()
        self.setId(id)
        self._title = title
        self._imgUrl = imgUrl
        self._link = link
        self._advertiser = advertiser
    
    def setId(self, id):
        if id in Advertiser.Ids:
            raise ValueError("id already exist")
        else:
            Ad.Ids.append(id)
            super().setId(id)

    def getTitle(self):
        return self._title
    
    def setTitle(self, title):
        self._title = title

    def getImgUrl(self):
        return self._imgUrl
    
    def setImgUrl(self, imgUrl):
        self._imgUrl = imgUrl
    
    def getLink(self):
        return self._link

    def setLink(self, link):
        self._link = link

    def setAdvertiser(self, advertiser: Advertiser):
        self._advertiser = advertiser

    def incClicks(self):
        self._advertiser.incClicks()
        super().incClicks()
    
    def incViews(self):
        self._advertiser.incViews()
        super().incViews()

    def describeMe(self):
        return """
        Ad is a class for managing ads.
"""