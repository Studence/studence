class AddressPbConvertor:

    def convert(self, uipb, pb):
        uipb.street = pb.street
        uipb.landmark = pb.landmark
        uipb.area = pb.area
        uipb.city = pb.city
        uipb.state = pb.state
