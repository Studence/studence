class EmailUiPbUpdator:

    def update(self, pb, uipb):
        pb.localPart = uipb.localPart;
        pb.domain = uipb.domain

