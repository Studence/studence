class AddressUiPbUpdator:

    def update(self, uipb, pb):
        pb.street = uipb.street
        pb.landmark = uipb.landmark
        pb.area = uipb.area
        pb.city = uipb.city
        pb.state = uipb.state
