from CommonCode.List.List import List
from Protobuff.mobileUiPb_pb2 import MobileUiPb


class MobilePbConvertor:

    def convert(self, uipb, pb):
        uipb.code = pb.code
        uipb.number = pb.number

    def getMobileListtUiPb(self, pb):
        mobileList = List()
        for mobile in pb.mobile:
            mobileUipb = MobileUiPb()
            self.convert(pb=mobileUipb, uipb=mobile)
            mobileList.__append__(mobile)
        return mobileList
