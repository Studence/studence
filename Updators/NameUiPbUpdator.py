from Protobuff.namePb_pb2 import NamePb


class NameUipbUpdator:

    def update(self, pb, uipb):
        pb.firstName = uipb.firstName
        pb.middleName.extend(uipb.middleName)
        pb.lastName = uipb.lastName
        pb.canonicalName = uipb.canonicalName
        return
