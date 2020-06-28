class AccountDetailsUiPbUpdator:

    def update(self, uipb, pb):
        pb.accountNo = uipb.accountNo
        pb.ifscCode = uipb.ifscCode
        pb.recipientName = uipb.recipientName
        pb.bankName = uipb.bankName
        pb.branch = uipb.branch
        self.getGooglePayUiPbUpdator(pb=pb.googlePay, uipb=uipb.googlePay)

    def getGooglePayUiPbUpdator(self, pb, uipb):
        pb.upiId = uipb.upiId
