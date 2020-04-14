from Protobuff.timeUiPb_pb2 import TimeUiPb


class TimeUiPbUpdator:

    def update(self, pb, uipb):
        pb.date = uipb.date
        pb.month = uipb.month
        pb.year = uipb.year
        pb.milliseconds = uipb.milliseconds
        pb.formattedDate = uipb.formattedDate
        pb.timezone = uipb.timezone
        return
