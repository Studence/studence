class AccountDetailsPbConvertor:

    def convert(self,uipb, pb):
        uipb.accountNo = pb.accountNo
        uipb.ifscCode = pb.ifscCode
        uipb.recipientName = pb.recipientName
        uipb.bankName = pb.bankName
        uipb.branch = pb.branch
        self.getGooglePayUiPbUpdator(pb=pb.googlePay, uipb=uipb.googlePay)

    def getGooglePayUiPbUpdator(self, pb, uipb):
        uipb.upiId = pb.upiId
