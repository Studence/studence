class EmailPbConvertor:

    def convert(self, uipb, pb):
        uipb.localPart = pb.localPart
        uipb.domain = pb.domain

