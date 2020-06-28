from CommonCode.List.List import List
from Protobuff.mobilePb_pb2 import MobilePb


class MobileUiPbUpdator:

    def update(self, pb, uipb):
        pb.code = uipb.code
        pb.number = uipb.number

    def getMobileListtPb(self, uipb):
        mobileList = List()
        for mobile in uipb:
            mobilepb = MobilePb()
            self.update(pb=mobilepb, uipb=mobile)
            mobileList.__append__(mobile)
        return mobileList
