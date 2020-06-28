from Protobuff.namePb_pb2 import NamePb


class NamePbConvertor:

    def convert(self, uipb, pb):
        uipb.firstName = pb.firstName
        uipb.middleName.extend(pb.middleName)
        uipb.lastName = pb.lastName
        uipb.canonicalName = pb.canonicalName
        return
