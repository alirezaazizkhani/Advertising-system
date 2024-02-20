from base_model import BaseAdvertising
from ad import Ad
from advertiser import Advertiser

if __name__ == "__main__":
    baseAdvertising = BaseAdvertising()

    advertiser1 = Advertiser(1, "name 1")
    advertiser2 = Advertiser(2, "name 2")

    ad1 = Ad(1, "title1", "img-url1", "link1", advertiser1)
    ad2 = Ad(2, "title2", "img-url2", "link2", advertiser2)

    print(baseAdvertising.describeMe())
    print(ad2.describeMe())
    print(advertiser1.describeMe())

    ad1.incViews()
    ad1.incViews()
    ad1.incViews()
    ad1.incViews()
    ad2.incViews()
    ad1.incClicks()
    ad1.incClicks()
    ad2.incClicks()

    print(f"advertiser2 name : {advertiser2.getName()}")
    advertiser2.setName("new name")
    print(f"advertiser2 name : {advertiser2.getName()}")

    print(f"number of clicks on ad1 : {ad1.getClicks()}")
    print(f"number of clicks on advertiser2's ads : {advertiser2.getClicks()}")

    print(f"number of total clicks : {Advertiser.getTotalClicks()}")
    print(Advertiser.help())